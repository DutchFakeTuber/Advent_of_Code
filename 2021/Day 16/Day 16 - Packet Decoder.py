# Standard libraries
from __future__ import annotations
from dataclasses import dataclass
from typing import Union

# Local variables
from Packet_Decoder import DATA


@dataclass(frozen=True)
class LiteralPacket:
    version: int
    value: int

@dataclass(frozen=True)
class OperatorPacket:
    version: int
    type_id: int
    sub_packets: tuple[Packet, ...]

    @property
    def value(self) -> int: ...

Packet = Union[LiteralPacket, OperatorPacket]
    
def getLiteral(index: int, data: str) -> tuple[int, int]:
    bits: str = ''
    while True:
        bits += data[index+1:index+5]
        if int(data[index]) == 0:
            index += 5
            break
        else:
            index += 5
    return index, int(bits, 2)

def executor(index: int, data: str) -> tuple[int, Packet]:
    version = int(data[index:index+3], 2)
    index += 3
    type_id = int(data[index:index+3], 2)
    index += 3
    if type_id == 4:
        index, literal = getLiteral(index, data)
        return index, LiteralPacket(version=version, value=literal)

    else:
        sub_packets = []
        operatorMode = int(data[index])
        index += 1
        if operatorMode == 0:
            n_subs = int(data[index:index+15], 2)
            index += 15
            done = index + n_subs
            while index < done:
                index, sub_packet = executor(index, data)
                sub_packets.append(sub_packet)
        
        else:
            n_subs = int(data[index:index+11], 2)
            index += 11
            for _ in range(n_subs):
                index, sub_packet = executor(index, data)
                sub_packets.append(sub_packet)
        return index, OperatorPacket(
            version=version, type_id=type_id, sub_packets=tuple(sub_packets)
        )

def sumVersions(packet: Packet) -> int:
    if isinstance(packet, Packet):
        return packet.version
    elif isinstance(packet, OperatorPacket):
        return packet.version + sum([sumVersions(pack) for pack in packet.sub_packets])
    else:
        Exception("INVALID PACKET")

def partOne() -> int:
    data = ''.join(bin(int(char, 16))[2:].zfill(4) for char in DATA)
    packet = executor(0, data)
    return sumVersions(packet)


def partTwo(self) -> int: ...

def main() -> None:
    print(partOne())
    print(partTwo())

if __name__ == "__main__":
    main()