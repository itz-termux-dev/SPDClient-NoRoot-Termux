# SPDClient-NoRoot-Termux

> [!CAUTION]
> **WARNING: This tool deals with low-level device partitions. Incorrect usage can permanently HARD BRICK your device. This tool is currently in BETA TESTING. I am not responsible for any damages, data loss, or bricked phones resulting from its use. Proceed at your own risk and with extreme caution. Always backup your boot and vbmeta partitions before making changes.**
> 

A powerful, standalone Unisoc (Spreadtrum) flashing protocol interface engineered specifically for Termux environments without requiring root privileges or a desktop computer.

## Description

**SPDClient-NoRoot-Termux** bridges the gap for mobile hardware restoration on devices utilizing Unisoc architectures (such as the T606, T612, T616, and T618 chipsets). By utilizing a purely low-level communication framework, this tool handles low-level diagnostic instructions, initialization, and device management protocols natively from a secondary Android phone via a standard OTG connection.

## The No-Root Advantage

Standard hardware flashing utilities rely on raw read/write permissions over system serial and USB nodes (`/dev/bus/usb/`), which are strictly protected by Android security policies and typically demand full administrative (root) access. 

This tool achieves its completely **No-Root framework** by:
* **User-Space Interception:** Leveraging Android's native Host API via the `termux-usb` system bridge.
* **File Descriptor Passing:** Programmatically catching the open connection's raw File Descriptor (`TERMUX_USB_FD`) immediately after user authorization.
* **Direct I/O Injection:** Mapping communication frames straight into standard user-space file handles inside Python, completely bypassing the need to modify kernel permissions or system paths.

## Key Features

* **High-Speed Connection Snipe:** Built-in loop architecture designed to capture the narrow BootROM execution windows before a device times out or reboots.
* **Automated HDLC Packaging:** Native implementation of high-level data link control framing protocols, handling automatic command structures and packet boundary escaping.
* **Hardware-Level Initialization Handling:** Fully structured routing engine prepared to coordinate multi-stage FDL1 (SRAM RAM/EMMC initialization) and FDL2 (High-speed flashing engine execution) download handlers.
* **Exploit Vector Routing:** Integrated with modular support to inject vulnerability structures (such as CVE-2022-38694) to bypass verification constraints directly within the BootROM environment.

# How To Use

1. First download the tool from the steps below

2. Then completely power off your target phone

3. Then type the command you want to run in inthe terminul while being in the tool's folder, and press enter

4. After the the text appers saying "Scanning for Unisoc BootROM/Loader interface", hold booth volume buttons of the target phone, and while holding them, connect the cable to it

5. If you are using a OTG adaptor, connect the OTG to the host phone and type c part of the usb cable to the target phone

6. If you are using a type c to type c cable, you can connect any sids to the phones

7. After you connect booth phone, if the target phone gets detected by the scrip, you will see a Termux:api popup on the host phone asking to allow access to the connected usb device

8. Press "OK" on that popup as soon as it appers, as you will have only ~2 to ~3 befor your target phone times out and reboots

9. If your timing is perfect, the flashing will begin, and it will go on for atlest 2 to 5 minutes

10. After it finises, you can safly unplug the phone and safly reboot

# Installation Guid

First install [Termux](https://f-droid.org/repo/com.termux_1022.apk) and [Termux:api](https://f-droid.org/repo/com.termux.api_1002.apk) from Fdroid or GitHub, dont use termux from playstore, that is a outdated version and it doesn't have the nessary pakages for the tool to run

# Give Termux storage permission
```bash
termux-setup-storage
```
# update and upgrade packages
```bash
pkg update && pkg upgrade
```
# Install the tool
```bash
pkg install python python3 python-pip termux-api usbutills git curl
```
```bash
git clone https://github.com/itz-termux-dev/SPDClient-NoRoot-Termux.git
cd SPDClient-NoRoot-Termux
pip install colorama
pip install .
```

# Command Examples

# 1. Run a basic handshake test to verify BootROM connectivity
```bash
python3 spd.py bypass --address 0x5500
```
# 2. Check connections on a standard entry-level SC9863A chipset configuration
```bash
python3 spd.py bypass --address 0x4000
```
# 3. Test the universal bridge interface on an alternative baseband hex offset
```bash
python3 spd.py bypass --address 0x65000800
```
# 4. Flash a patched boot image to fix a soft-brick loop

```bash
python3 spd.py write --partition boot patched_boot.img
```
# 5. Clear FRP
```bash
python3 spd.py erase --partition frp
```
# 6. Flash a custom recovery image (like TWRP)
```
python3 spd.py write --partition recovery twrp_recovery.img
```
# 7. Dump the device's stock boot partition
```
python3 spd.py read --partition boot stock_boot_backup.img
```
# 8. Clear the metadata block structure
```bash
python3 spd.py erase --partition metadata
```

For any suggestions or bug report please contact on sameenataj427@gmail.com. thank you
