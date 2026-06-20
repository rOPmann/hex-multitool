import platform, os, sys, psutil, cpuinfo, time, GPUtil
from core.display import csh, print_banner

import threading
import itertools
import sys
import time
import os

def loading_animation(stop_event):
    try:
        for c in itertools.cycle(["|", "/", "-", "\\"]):
            if stop_event.is_set():
                break

            sys.stdout.write(f"\r{csh('Loading')} {c}   ")
            sys.stdout.flush()
            time.sleep(0.1)

        sys.stdout.write("\r\033[K")
        sys.stdout.flush()
    except KeyboardInterrupt:
        return


def gpu_info():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "No GPUs found"
    for gpu in gpus:
        print(csh(f"GPU:           {gpu.name}"))
        print(csh(f"Total VRAM:    {round(gpu.memoryTotal)} MB / {int(gpu.memoryTotal // 1000)} GB"))
        print(csh(f"Used VRAM:     {round(gpu.memoryUsed)} MB"))
        print(csh(f"Usage:         {gpu.load * 1000}%"))
        print(csh(f"GPU Temp.:     {gpu.temperature}°C"))



def sysinfo():
    try:
        stop_event = threading.Event()
        t = threading.Thread(target=loading_animation, args=(stop_event,))
        t.start()

        
        
        ram = psutil.virtual_memory()
        uptime = time.time() - psutil.boot_time()

        h = int(uptime // 3600)
        m = int((uptime % 3600) // 60)
        s = int(uptime % 60)
        d = int(h // 24)
        h = h % 24

        gpu = GPUtil.getGPUs()

        cpu = cpuinfo.get_cpu_info()

        # stop loading sobald fertig
        stop_event.set()
        t.join()
        time.sleep(0.05)

        os.system("cls" if os.name == "nt" else "clear")
        print_banner()
        print("\n\n")

        print(csh(f"      {os.getlogin()}@hex"))
        print(csh("────────────────────────"))
        print(csh("Operating System: " + platform.system()))
        print()

        print(csh("────── RAM ──────"))
        print(csh(f"Total RAM:     {round(ram.total / (1024**3), 2)} GB"))
        print(csh(f"Used RAM:      {round(ram.used / (1024**3), 2)} GB"))
        print(csh(f"Usage:         {ram.percent}%"))

        print(csh("────── CPU ──────"))
        print(csh(f"CPU:           {cpu['brand_raw']}"))
        print(csh(f"Cores:         {psutil.cpu_count(logical=False)}"))
        print(csh(f"Threads:       {psutil.cpu_count(logical=True)}"))
        print(csh(f"Frequency:     {round(psutil.cpu_freq().current)} MHz"))

        print(csh("────── GPU ──────"))

        if not gpu:
            print(csh("No GPU found"))
        else:
            for g in gpu:
                print(csh(f"GPU:           {g.name}"))
                print(csh(f"VRAM:          {g.memoryUsed}/{g.memoryTotal} MB"))
                print(csh(f"Temp:          {g.temperature}°C"))

        print(csh("..."))
        return "home"

    except KeyboardInterrupt:
        stop_event.set()
        t.join()

        os.system("cls" if os.name == "nt" else "clear")

        return "home"