from datetime import datetime
import time
import winsound
#Set alarm time (24-hour format)
alarm_time = input("Enter alarm time (HH:MM:SS): ")
print("Alarm set for", alarm_time)
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time, end="\r")
    if current_time == alarm_time:
        print("\nWake up! Alarm ringing...")
        for i in range(5):
            winsound.Beep(1000, 1000)
        break
    time.sleep(1)