import os

battery_dir = "/sys/class/power_supply/BAT0"

status = open(f"{battery_dir}/status").read()

current = int(open(f"{battery_dir}/charge_now").read())
max = int(open(f"{battery_dir}/charge_full").read())

battery_percentage = round((current / max) * 100, 2)
charging_message = "charging" if status == "Charging" else "not charging"
print(f"Battery is at {battery_percentage}% and is {charging_message}")