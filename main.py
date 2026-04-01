import os
import subprocess

# نقطة البداية لتشغيل الخدمات
def start_services():
    services = [
        "services/service1.py",
        "services/service2.py",
        "services/logger.py"
    ]

    for service in services:
        print(f"Starting {service}...")
        subprocess.Popen(["python3", service], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
    print("Starting Za-System...")
    start_services()
