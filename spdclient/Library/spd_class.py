import os
import sys
import struct
from spdclient.Library.hdlc import HDLC
from spdclient.Library.exploit import UnisocExploit

class SpdController:
    def __init__(self):
        self.fd = int(os.environ.get("TERMUX_USB_FD", -1))
        if self.fd == -1:
            print("[-] Error: No Termux USB File Descriptor detected.")
            sys.exit(1)
        self.exploit = UnisocExploit(self)

    def write(self, data: bytes):
        # Uses standard system write operations mapped directly to the OS file handle
        os.write(self.fd, data)

    def read(self, length: int = 4096) -> bytes:
        try:
            return os.read(self.fd, length)
        except Exception:
            return b""

    def connect_handshake(self) -> bool:
        # BSL_CMD_CONNECT = 0x00
        packet = HDLC.frame_packet(0x00)
        for _ in range(10):  # Retry sequence to match high speed connection drops
            self.write(packet)
            res = self.read()
            if b"\x7e" in res:
                return True
        return False

    def erase_partition(self, partition_name: str) -> bool:
        # BSL_CMD_ERASE_FLASH = 0x0A
        # Unisoc expects partition structures wrapped inside raw byte parameters
        encoded_name = partition_name.encode('utf-8').ljust(32, b'\x00')
        packet = HDLC.frame_packet(0x0A, encoded_name)
        self.write(packet)
        res = self.read()
        return True
