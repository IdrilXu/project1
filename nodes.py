from dataclasses import dataclass

@dataclass
class DomainNode:
    value: str
    def __repr__(self):
        return f'{self.value}'

@dataclass
class SeperateNode:
    node_1: any
    node_2: any

    def __repr__(self):
        return f"({self.node_1},{self.node_2}"