import os
from datetime import datetime
file_path = "C:/Users/hp/Desktop/credit_cards.txt"
honypot_alart = "C:/Users/hp/Desktop/honeypot_alerts.txt"
time = datetime.now().strftime("%Y-%m-%d ______ %H:%M:%S")
if not os.path.exists(file_path):
    F_text = "MY bank account is 10000701114234"
    with open(file_path , "w") as file:
        file.write(F_text)
else:
    print("Intrusion detected! Logging event...")
    alart = f"ALERT: Honeypot file accessed!--[{time}]"
    with open(honypot_alart , "a") as file:
            file.write(alart)
print("\n--- SECURITY ALERT REPORT ---")
if os.path.exists(honypot_alart):
    with open(honypot_alart , "r") as file:
        for line in file:
            if "ALERT" in line:
                print(f"🚨 ALERT FOUND: {line.strip()}")





        