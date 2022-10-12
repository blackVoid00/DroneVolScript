from dronekit import connect
import requests
import json

vehicle = connect('/dev/ttyAMA0', wait_ready=True)
print("Mode: %s" % vehicle.mode.name)


def arm_and_takeoff(aTargetAltitude):

    print "Basic pre-arm checks"

    while not vehicle.is_armable:
        print " Waiting for vehicle to initialise..."
        time.sleep(1)

    print "Arming motors"

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print " Waiting for arming..."
        time.sleep(1)

    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude)

    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt

        if vehicle.location.global_relative_frame.alt >= aTargetAltitude*0.95:
            print "Reached target altitude"
            break
        time.sleep(1)


arm_and_takeoff(20)

vehicle.mode = VehicleMode("GUIDED")

playload = {"email": "hello@gmail.com", "password": "Hello"}
url = "https://soraeir.herokuapp.com/login"
r = requests.post(url, json=playload)
data = r.json()
headers = {"x-access-token": data["token"]}
url2 = "https://soraeir.herokuapp.com/api/gpsdata"
r2 = requests.get(url2, headers=headers)
data2 = r2.json()
long = data2[0]['longitude']
lat = data2[0]['latitude']
alt = data2[0]['altitude']
a_location = LocationGlobalRelative(long, lat, alt)
vehicle.simple_goto(a_location)
