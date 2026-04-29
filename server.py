# ============================================================
#  server.py — Serveur GPS en Python Flask
#
#  Ce serveur fait 3 choses :
#    1. Reçoit les positions GPS envoyées par l'ESP32
#    2. Les stocke dans une base de données SQLite
#    3. Les sert à l'interface web (carte Leaflet)
#
#  Installation :
#    pip install flask flask-cors
#
#  Lancement :
#    python server.py
#
#  Le serveur démarre sur : http://localhost:5000
# ============================================================

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Autorise les requêtes venant du navigateur

DATABASE = "gps_data.db"

# ─────────────────────────────────────────────────────────────
#  BASE DE DONNÉES
# ─────────────────────────────────────────────────────────────

def init_db():
    """Crée la table si elle n'existe pas encore."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS positions (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id  TEXT    NOT NULL,
            lat         REAL    NOT NULL,
            lng         REAL    NOT NULL,
            speed       REAL    DEFAULT 0,
            altitude    REAL    DEFAULT 0,
            satellites  INTEGER DEFAULT 0,
            timestamp   TEXT,
            created_at  TEXT    DEFAULT (datetime('now'))
        )
    """)
    conn.commit()
    conn.close()
    print("[DB] Base de données initialisée : gps_data.db")


def get_db():
    """Ouvre une connexion à la base de données."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # permet d'accéder aux colonnes par nom
    return conn


# ─────────────────────────────────────────────────────────────
#  ROUTES API
# ─────────────────────────────────────────────────────────────

@app.route("/api/position", methods=["POST"])
def receive_position():
    """
    Reçoit une position GPS depuis l'ESP32.
    Corps attendu (JSON) :
    {
        "vehicle_id": "vehicule_01",
        "lat": 14.6928,
        "lng": -17.4467,
        "speed": 45.2,
        "altitude": 12.0,
        "satellites": 6,
        "timestamp": "2026-04-18T10:23:00Z"
    }
    """
    data = request.get_json()

    # Vérification des champs obligatoires
    if not data:
        return jsonify({"error": "Corps JSON manquant"}), 400

    if "lat" not in data or "lng" not in data:
        return jsonify({"error": "lat et lng sont obligatoires"}), 400

    # Insertion en base de données
    conn = get_db()
    conn.execute("""
        INSERT INTO positions (vehicle_id, lat, lng, speed, altitude, satellites, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("vehicle_id", "inconnu"),
        data["lat"],
        data["lng"],
        data.get("speed",      0),
        data.get("altitude",   0),
        data.get("satellites", 0),
        data.get("timestamp",  datetime.utcnow().isoformat() + "Z")
    ))
    conn.commit()
    conn.close()

    print(f"[GPS] Reçu → Lat={data['lat']:.6f}  Lng={data['lng']:.6f}  "
          f"Speed={data.get('speed', 0):.1f} km/h  "
          f"Sats={data.get('satellites', 0)}")

    return jsonify({"status": "ok"}), 200


@app.route("/api/positions", methods=["GET"])
def get_positions():
    """
    Retourne les dernières positions d'un véhicule.
    Paramètres URL optionnels :
      ?vehicle_id=vehicule_01   filtrer par véhicule
      ?limit=50                 nombre de positions (défaut 100)
    """
    vehicle_id = request.args.get("vehicle_id", None)
    limit      = request.args.get("limit", 100, type=int)

    conn = get_db()

    if vehicle_id:
        rows = conn.execute("""
            SELECT * FROM positions
            WHERE vehicle_id = ?
            ORDER BY id DESC LIMIT ?
        """, (vehicle_id, limit)).fetchall()
    else:
        rows = conn.execute("""
            SELECT * FROM positions
            ORDER BY id DESC LIMIT ?
        """, (limit,)).fetchall()

    conn.close()

    positions = [dict(row) for row in rows]
    positions.reverse()  # ordre chronologique pour la carte

    return jsonify(positions), 200


@app.route("/api/last", methods=["GET"])
def get_last_position():
    """
    Retourne uniquement la dernière position connue.
    Utilisé par l'interface web pour rafraîchir le marqueur.
    """
    vehicle_id = request.args.get("vehicle_id", None)

    conn = get_db()

    if vehicle_id:
        row = conn.execute("""
            SELECT * FROM positions
            WHERE vehicle_id = ?
            ORDER BY id DESC LIMIT 1
        """, (vehicle_id,)).fetchone()
    else:
        row = conn.execute("""
            SELECT * FROM positions
            ORDER BY id DESC LIMIT 1
        """).fetchone()

    conn.close()

    if row is None:
        return jsonify({"error": "Aucune position enregistrée"}), 404

    return jsonify(dict(row)), 200


@app.route("/api/vehicles", methods=["GET"])
def get_vehicles():
    """Retourne la liste de tous les véhicules enregistrés."""
    conn = get_db()
    rows = conn.execute("""
        SELECT DISTINCT vehicle_id FROM positions
    """).fetchall()
    conn.close()

    vehicles = [row["vehicle_id"] for row in rows]
    return jsonify(vehicles), 200


@app.route("/api/clear", methods=["DELETE"])
def clear_positions():
    """Vide toutes les positions (utile pendant les tests)."""
    conn = get_db()
    conn.execute("DELETE FROM positions")
    conn.commit()
    conn.close()
    print("[DB] Toutes les positions supprimées.")
    return jsonify({"status": "cleared"}), 200


# ─────────────────────────────────────────────────────────────
#  PAGE WEB (carte Leaflet intégrée)
# ─────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Sert la page web avec la carte GPS en temps réel."""
    return render_template_string(HTML_MAP)


# ─────────────────────────────────────────────────────────────
#  TEMPLATE HTML DE LA CARTE
# ─────────────────────────────────────────────────────────────

HTML_MAP = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GPS Tracker — Carte en temps réel</title>

  <!-- Leaflet.js (carte interactive) -->
  <link  rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: sans-serif; background: #1a1a2e; color: #eee; }

    #header {
      padding: 12px 20px;
      background: #16213e;
      display: flex;
      align-items: center;
      gap: 16px;
      border-bottom: 1px solid #0f3460;
    }
    #header h1 { font-size: 18px; font-weight: 500; }
    #status {
      margin-left: auto;
      font-size: 13px;
      padding: 4px 12px;
      border-radius: 20px;
      background: #0f3460;
    }
    #status.online  { background: #1a6b3a; color: #7dffb3; }
    #status.offline { background: #6b1a1a; color: #ffb3b3; }

    #info-bar {
      display: flex;
      gap: 24px;
      padding: 10px 20px;
      background: #16213e;
      font-size: 13px;
      color: #aaa;
      border-bottom: 1px solid #0f3460;
    }
    #info-bar span { color: #fff; font-weight: 500; }

    #map { height: calc(100vh - 100px); }
  </style>
</head>
<body>

  <div id="header">
    <h1>GPS Tracker</h1>
    <div id="status">En attente...</div>
  </div>

  <div id="info-bar">
    Latitude : <span id="info-lat">—</span>
    Longitude : <span id="info-lng">—</span>
    Vitesse : <span id="info-speed">—</span>
    Satellites : <span id="info-sats">—</span>
    Mis à jour : <span id="info-time">—</span>
  </div>

  <div id="map"></div>

  <script>
    // Initialiser la carte centrée sur Dakar (modifiez selon votre zone)
    const map = L.map("map").setView([14.6928, -17.4467], 13);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "© OpenStreetMap"
    }).addTo(map);

    // Marqueur de la position actuelle
    const icon = L.divIcon({
      html: '<div style="width:16px;height:16px;background:#4af;border:3px solid #fff;border-radius:50%;box-shadow:0 0 6px #4af"></div>',
      iconSize: [16, 16],
      iconAnchor: [8, 8]
    });

    let marker   = null;
    let polyline = L.polyline([], { color: "#4af", weight: 3 }).addTo(map);
    let lastId   = 0;

    // Rafraîchir toutes les 2 secondes
    setInterval(fetchPosition, 2000);
    fetchPosition();

    async function fetchPosition() {
      try {
        const res  = await fetch("/api/last");
        if (!res.ok) return;
        const data = await res.json();

        const lat   = data.lat;
        const lng   = data.lng;
        const latlng = [lat, lng];

        // Mettre à jour le marqueur
        if (!marker) {
          marker = L.marker(latlng, { icon }).addTo(map);
          map.setView(latlng, 15);
        } else {
          marker.setLatLng(latlng);
        }

        // Ajouter au tracé si nouvelle position
        if (data.id !== lastId) {
          lastId = data.id;
          polyline.addLatLng(latlng);
        }

        // Mettre à jour la barre d'info
        document.getElementById("info-lat").textContent   = lat.toFixed(6) + " °";
        document.getElementById("info-lng").textContent   = lng.toFixed(6) + " °";
        document.getElementById("info-speed").textContent = (data.speed || 0).toFixed(1) + " km/h";
        document.getElementById("info-sats").textContent  = data.satellites || "—";
        document.getElementById("info-time").textContent  = new Date().toLocaleTimeString();

        const s = document.getElementById("status");
        s.textContent = "En ligne";
        s.className   = "online";

      } catch (e) {
        const s = document.getElementById("status");
        s.textContent = "Hors ligne";
        s.className   = "offline";
      }
    }
  </script>
</body>
</html>
"""

# ─────────────────────────────────────────────────────────────
#  DÉMARRAGE
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    init_db()
    print("\n╔══════════════════════════════════════╗")
    print("║   Serveur GPS Flask démarré          ║")
    print("║   Interface web : http://localhost:5000  ║")
    print("║   API POST      : /api/position      ║")
    print("║   API GET       : /api/positions     ║")
    print("╚══════════════════════════════════════╝\n")
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=False)