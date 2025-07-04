import os
from nicegui import ui
import psutil
import shutil

def shutdown():
    os.system("sudo shutdown -h now")

def restart():
    os.system("sudo reboot")

@ui.refreshable
def memory():
    #print("CPU usage (%):", psutil.cpu_percent(interval=1))
    ram = psutil.virtual_memory()
    #print("RAM usage (%):", ram.percent)
    #print("RAM used (GB):", round(ram.used / 1e9, 2))
    with ui.row().classes('items-center'):
        ui.circular_progress(value=ram.percent,min=0,max=100)
        ui.label('Memory')

@ui.refreshable
def CPU():
    cpu = psutil.cpu_percent(interval=1)
    #print("CPU usage (%):", cpu)
    with ui.row().classes('items-center'):
        ui.circular_progress(value=cpu,min=0,max=100)
        ui.label('CPU')


@ui.refreshable
def disk():
    disk_info = shutil.disk_usage('/')
    pdisk = disk_info.used/disk_info.total * 100
    #print(pdisk)
    #print(f"Total: {disk_info.total / (1024**3):.2f} GB")
    #print(f"Used: {disk_info.used / (1024**3):.2f} GB")
    #print(f"Free: {disk_info.free / (1024**3):.2f} GB")
    with ui.row().classes('items-center'):
        ui.circular_progress(value=int(pdisk),min=0,max=100)
        ui.label('Disk Used')        
