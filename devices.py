readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def list_devices(devices):
    for device in devices:
        print(f"Device: {device['name']}, Temperature: {device['temp']}")

def average_temp(devices):
    total_temp = sum(device['temp'] for device in devices)
    return total_temp / len(devices) if devices else 0

def hottest(devices):
    return max(devices, key=lambda device: device['temp']) if devices else None

def to_status(device):
    return {
        "name": device["name"],
        "room": device["room"],
        "temp": device["temp"],
        "online": device["online"]
    }

def by_room(devices):
    room_dict = {}
    for device in devices:
        room = device["room"]
        if room not in room_dict:
            room_dict[room] = []
        room_dict[room].append(device["name"])
    return room_dict