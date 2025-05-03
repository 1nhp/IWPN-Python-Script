# Battery Notify system
from init import *

while True:
    # Define variables and use psutil to grab battery data from acpi
    battery = psutil.sensors_battery()
    status = battery.power_plugged
    percentage = battery.percent
    
    # Check if the device is plugged in
    if status == None and last_status != None: message(reason = 1)
    
        # Incase if it doesnt work do this
    elif status == True and last_status != 1: message(reason = 1)

    # Check if the device's battery is full Note this might be different on some laptops
    if percentage > float(full_battery_level) and last_percentage < float(full_battery_level): message(reason = 5)

    if status == False:

        # Check if the device's battery is below 15
        if percentage < float(low_battery_level) and last_percentage > float(low_battery_level): message(reason = 3)

        # Check if the device's battery is below 3
        if percentage < float(empty_battery_level) and last_percentage > float(empty_battery_level): message(reason = 4)            

        # Check if the device is unplugged
        if last_status != False: message(reason = 2)

    # Put delay to prevent high cpu / ram usage
    time.sleep(0.1)
    last_status = status
    last_percentage = percentage