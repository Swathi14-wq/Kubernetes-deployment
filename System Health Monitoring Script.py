import psutil
import logging
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80
logging.basicConfig(filename='system_health.log', level=logging.WARNING)
def monitor_system_health():
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    running_processes = len(psutil.process_iter())

    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'CPU usage exceeded threshold: {cpu_usage}%')
    if mem_usage > MEM_THRESHOLD:
        logging.warning(f'Memory usage exceeded threshold: {mem_usage}%')
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'Disk usage exceeded threshold: {disk_usage}%')
    if running_processes > 100:
        logging.warning(f'Too many running processes: {running_processes}')

    print(f'CPU usage: {cpu_usage}%')
    print(f'Memory usage: {mem_usage}%')
    print(f'Disk usage: {disk_usage}%')
    print(f'Running processes: {running_processes}')
monitor_system_health()
