import psutil
import os
import time
import platform
import datetime

def cpu_usage():
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")

def memory_usage():
    mem = psutil.virtual_memory()
    print(f"Memory Usage: {mem.used / (1024**3):.2f} GB / {mem.total / (1024**3):.2f} GB ({mem.percent}%)")

def uptime():
    boot_time = psutil.boot_time()
    boot_datetime = datetime.datetime.fromtimestamp(boot_time)
    now = datetime.datetime.now()
    uptime_duration = now - boot_datetime
    print(f"System boot time: {boot_datetime}")
    print(f"System uptime: {uptime_duration}")

def os_info():
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python Version: {platform.python_version()}")

while True:
    cpu_usage()
    memory_usage()
    uptime()
    os_info()
    print("-" * 40)
    time.sleep(5)  # run every 5 seconds

