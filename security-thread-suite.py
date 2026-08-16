import threading
import time

active_hosts = []
list_lock = threading.Lock()
emergency_swittch = threading.Event()
file_path = r"C:\Users\hp\Desktop\targets.txt"
with open(file_path , "w") as f:
    f.write("""192.168.1.1
192.168.1.2
CRITICAL_SERVER
192.168.1.4
192.168.1.5""")
def scan_target(target):
    if emergency_swittch.is_set():
        print("The scan is skipped")
        return
    print(f"[{threading.current_thread().name}] Investigating: {target}")
    time.sleep(0.5)

    if target != "CRITICAL_SERVER":
        with list_lock:
            active_hosts.append(target)
    elif target == "CRITICAL_SERVER":
        print("⚠️⚠️⚠️ Warning CRITICAL_SERVER is detected please terminat")
        emergency_swittch.set()
with open(file_path,"r") as file:
    target = [target.strip() for target in file]
threads = []
for t_name in target:
    t = threading.Thread(target=scan_target, args=(t_name,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print(f"\n[+] Final Verified Active Hosts List: {active_hosts}")
