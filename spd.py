import os
import sys
import subprocess
import time

def start_unisoc_bridge():
    print("--- Unisoc Universal No-Root Bridge ---")
    print("Scanning for Unisoc BootROM/Loader interface...")
    while True:
        try:
            output = subprocess.check_output(["termux-usb", "-l"]).decode().strip()
            if "/dev/bus/usb/" in output:
                address = [line.strip() for line in output.split('\n') if "/dev/bus/usb/" in line][0]
                if address:
                    print(f"\n[+] Caught interface target at: {address}")
                    cmd = f"termux-usb -r {address} -e 'export TERMUX_USB_FD=$1; python3 spd_main.py {' '.join(sys.argv[1:])}'"
                    os.system(cmd)
                    return
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception:
            pass
        time.sleep(0.1)

if __name__ == "__main__":
    start_unisoc_bridge()

