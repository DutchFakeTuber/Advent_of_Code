from __future__ import annotations
from types import NoneType
from typing import Union
from dataclasses import dataclass

TEST: str = open("test.txt")
DATA: str = open("input.txt")

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
    def value(self) -> int:
        match self.type_id:
            case 0: # SUM 
                return sum([sub_packet.value for sub_packet in self.sub_packets])
            case 1: # PRODUCT
                product = 1
                for sub_packet in self.sub_packets:
                    product *= sub_packet.value
                return product
            case 2: # MIN
                return min([sub_packet.value for sub_packet in self.sub_packets])
            case 3: # MAX
                return max([sub_packet.value for sub_packet in self.sub_packets])
            case 4: # LITERAL
                 pass
            case 5: # GREATER THAN
                return 1 if self.sub_packets[0].value > self.sub_packets[1].value else 0
            case 6: # LESS THAN
                return 1 if self.sub_packets[0].value < self.sub_packets[1].value else 0
            case 7: # EQUAL TO
                return 1 if self.sub_packets[0].value == self.sub_packets[1].value else 0
            case _: # NONE OF THE ABOVE
                raise ValueError("Invalid Type ID")

Packet = Union[LiteralPacket, OperatorPacket]

class ProcessPackets:
    def __init__(self, data: str=DATA):
        self.data = ''.join(bin(int(char, 16))[2:].zfill(4) for char in data)
    
    def getVersion(self) -> int:
        version = int(self.data[0:3], 2)
        self.data = self.data[3:]
        return version

    def getTypeID(self) -> int:
        type_id = int(self.data[0:3], 2)
        self.data = self.data[3:]
        return type_id
    
    def getLiteral(self) -> int:
        literal = ''
        while True:
            literal += self.data[1:5]
            if int(self.data[0]) == 0:
                self.data = self.data[5:]
                literal: int = int(literal, 2)
                return literal
            self.data = self.data[5:]

    def executor(self) -> Packet:
        version = self.getVersion()
        type_id = self.getTypeID()
        if type_id == 4:
            value = self.getLiteral()
            return LiteralPacket(
                version=version,
                value=value
            )
        else:
            subPackets: list = []
            opMode = self.data[0]
            self.data = self.data[1:]
            if opMode == '0':
                number_bits = int(self.data[0:15], 2)
                self.data = self.data[15:]
                done = len(self.data) - number_bits
                while len(self.data) > done:
                    subP = self.executor()
                    subPackets.append(subP)
            
            else:
                number = int(self.data[0:11], 2)
                self.data = self.data[11:]
                for _ in range(number):
                    subP = self.executor()
                    subPackets.append(subP)
            return OperatorPacket(
                version=version,
                type_id=type_id,
                sub_packets=tuple(subPackets)
            )
    
    def versionCounter(self, packet: Packet) -> int:
        if isinstance(packet, LiteralPacket):
            return packet.version
        elif isinstance(packet, OperatorPacket):
            return packet.version + sum([self.versionCounter(pack) for pack in packet.sub_packets])
        else:
            raise Exception("Invalid packet")

    def partOne(self):
        packets = self.executor()
        return self.versionCounter(packets)

    def partTwo(self) -> int:
        packet = self.executor()
        return packet.value

def main() -> None:
    print(ProcessPackets().partOne())
    print(ProcessPackets().partTwo())

if __name__ == "__main__":
    main()