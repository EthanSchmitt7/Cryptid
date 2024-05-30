from dataclasses import dataclass


@dataclass
class Component:
    def pack(self):
        self.__dict__
