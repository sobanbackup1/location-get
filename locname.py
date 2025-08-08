import requests
import math
#this script is only for educational purpose don't use it to harm others 
#you need to install tarccar client on the both phone 
TRACCAR_URL = "https://url-of-your-tarccar-or may be your localhost where your server run"
USERNAME = "usename you used to log in traccar"
PASSWORD = "password for tarccar"

DEVICE_IDS = [1, 1]  # Replace with your actual device IDs you can find it just ask ai 
RADIUS_KM = 3

BARK_KEY = "here should be your bark api from your phone app the string of different character"
BARK_URL = f"https://api.day.app/{BARK_KEY}"

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon/2)**2)
    return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))

def send_bark(title, body):
    payload = {"title": title, "body": body}
    requests.post(BARK_URL, json=payload)

def get_devices():
    resp = requests.get(f"{TRACCAR_URL}/api/devices", auth=(USERNAME, PASSWORD))
    return {d["id"]: d["name"] for d in resp.json()}

def get_latest_position(device_id):
    resp = requests.get(f"{TRACCAR_URL}/api/positions?deviceId={device_id}&limit=1", auth=(USERNAME, PASSWORD))
    data = resp.json()
    if data:
        return data[0]["latitude"], data[0]["longitude"]
    else:
        return None, None

devices = get_devices()
lat_lon = {}

for device_id in DEVICE_IDS:
    lat, lon = get_latest_position(device_id)
    lat_lon[device_id] = (lat, lon)

if None in [lat_lon[DEVICE_IDS[0]][0], lat_lon[DEVICE_IDS[0]][1], lat_lon[DEVICE_IDS[1]][0], lat_lon[DEVICE_IDS[1]][1]]:
    print("❌ Could not get position for one or both devices.")
else:
    lat1, lon1 = lat_lon[DEVICE_IDS[0]]
    lat2, lon2 = lat_lon[DEVICE_IDS[1]]
    distance = haversine(lat1, lon1, lat2, lon2)
    print(f"Distance between {devices[DEVICE_IDS[0]]} and {devices[DEVICE_IDS[1]]}: {distance:.2f} km")

    if distance <= RADIUS_KM:
        message = f"{devices[DEVICE_IDS[0]]} and {devices[DEVICE_IDS[1]]} are within {distance:.2f} km."
        print("✅ ALERT:", message)
        send_bark("Traccar Proximity Alert", message)
    else:
        print("❌ Devices are farther than 3 km.")
