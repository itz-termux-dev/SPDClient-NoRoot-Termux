import sys
import argparse
from spdclient.Library.spd_class import SpdController

def main():
    parser = argparse.ArgumentParser(description="SPDClient-NoRoot Engine")
    parser.add_argument("action", choices=["erase", "read", "bypass"])
    parser.add_argument("--partition", help="Target partition name")
    parser.add_argument("--address", type=lambda x: int(x, 16), help="Hex code address boundary for exploit")
    
    args = parser.parse_args()
    spd = SpdController()
    
    print("[*] Contacting Unisoc BootROM...")
    if not spd.connect_handshake():
        print("[-] Handshake Failed.")
        sys.exit(1)
    print("[+] Connected successfully!")

    if args.action == "bypass":
        print("[*] Deploying CVE-2022-38694 exploit payload...")
        spd.exploit.inject_cve_2022_38694(args.address, b"\x00" * 256)
        print("[+] Custom pointer overwrite sequence initiated.")
        
    elif args.action == "erase" and args.partition:
        print(f"[*] Sending instruction to wipe partition: {args.partition}...")
        spd.erase_partition(args.partition)
        print("[+] Erase sequence finalized.")

if __name__ == "__main__":
    main()

