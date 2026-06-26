import struct

class HDLC:
    @staticmethod
    def frame_packet(cmd_type: int, payload: bytes = b"") -> bytes:
        # Structure payload: Command Type (2 bytes big-endian) + Data Length + Data
        packet_data = struct.pack(">H", cmd_type) + payload
        
        # Calculate a basic 16-bit checksum if required by target configuration
        # For simplicity, we implement raw unescaped frame preparation
        framed = bytearray([0x7E])
        for byte in packet_data:
            if byte in (0x7E, 0x7D):
                framed.append(0x7D)
                framed.append(byte ^ 0x20)
            else:
                framed.append(byte)
        framed.append(0x7E)
        return bytes(framed)

    @staticmethod
    def deframe_packet(packet: bytes) -> tuple:
        if not packet.startswith(b"\x7e") or not packet.endswith(b"\x7e"):
            return False, b""
        
        unwrapped = bytearray()
        i = 1
        while i < len(packet) - 1:
            if packet[i] == 0x7D:
                unwrapped.append(packet[i+1] ^ 0x20)
                i += 2
            else:
                unwrapped.append(packet[i])
                i += 1
                
        cmd_type = struct.unpack(">H", unwrapped[0:2])[0]
        return cmd_type, bytes(unwrapped[2:])
