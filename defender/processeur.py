import psutil

def monitor_system_resources():
    cpu_threshold = 80 # Threshold for CPU usage
    mem_threshold = 80 # Threshold for memory usage
    disk_threshold = 80 # Threshold for disk usage
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    if cpu_usage > cpu_threshold:
        print(f'WARNING: CPU usage is {cpu_usage}%!')
       
    if mem_usage > mem_threshold:
        print(f'WARNING: Memory usage is {mem_usage}%!')
    if disk_usage > disk_threshold:
        print(f'WARNING: Disk usage is {disk_usage}%!')

monitor_system_resources()