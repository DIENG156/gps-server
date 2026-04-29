# ============================================================
#  simulate_esp32.py — Simule l'ESP32 qui envoie des données GPS
#
#  Envoie des positions GPS vers le serveur Flask toutes les
#  2 secondes pour tester la carte sans l'ESP32 physique.
#
#  Lancement :
#    python simulate_esp32.py
#
#  Prérequis : le serveur server.py doit être lancé
# ============================================================

import requests
import time
import math

SERVER_URL = "http://localhost:5000/api/position"
VEHICLE_ID = "vehicule_01"

# Point de départ : Dakar (modifiez selon votre ville)
START_LAT = 14.6928
START_LNG = -17.4467

print("=" * 45)
print("  Simulateur ESP32 — Envoi vers Flask")
print(f"  Serveur : {SERVER_URL}")
print("  Appuyez sur Ctrl+C pour arrêter")
print("=" * 45)

step = 0

while True:
    # Simuler un déplacement en cercle autour du point de départ
    angle     = step * 0.05               # avancer de 0.05 rad à chaque étape
    lat       = START_LAT + 0.005 * math.sin(angle)
    lng       = START_LNG + 0.005 * math.cos(angle)
    speed     = 30 + 10 * math.sin(angle) # vitesse entre 20 et 40 km/h
    satellites = 6 + (step % 3)           # entre 6 et 8 satellites

    payload = {
        "vehicle_id": VEHICLE_ID,
        "lat":        round(lat,   6),
        "lng":        round(lng,   6),
        "speed":      round(speed, 1),
        "altitude":   12.0,
        "satellites": satellites,
        "timestamp":  time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }

    try:
        response = requests.post(SERVER_URL, json=payload, timeout=3)

        if response.status_code == 200:
            print(f"[OK]  Lat={lat:.6f}  Lng={lng:.6f}  "
                  f"Speed={speed:.1f} km/h  Sats={satellites}")
        else:
            print(f"[ERR] Code HTTP : {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("[ERR] Serveur inaccessible. Vérifiez que server.py est lancé.")

    step += 1
    time.sleep(2)  # attendre 2 secondes entre chaque envoi