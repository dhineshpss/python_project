import psutil 


def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

for i in range(5):  # Check CPU usage 5 times
    print   ("Checking CPU usage...")
    check_cpu_usage()
    print("-" * 30)