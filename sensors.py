import psutil

class Sensors:
    def battery(self):
        battery = psutil.sensors_battery()
        print(f"\nBattery = {battery.percent}\nPower Plugged = {battery.power_plugged}")
        