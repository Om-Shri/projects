## Drink water reminder
##  WINDOWS SYSTEM.
import time
from plyer import notification
sedule = input("Enter hours for notification (1,2,3,4...) :")

hours = int(sedule)*3600

while True:
    notification.notify(
        title="Reminder",
        message="Drink one glass of water.You are dehydrated.",
    )
    for i in range(hours,-1,-1):
        print(f"Remaining seconds = {i}")
        time.sleep(1)
