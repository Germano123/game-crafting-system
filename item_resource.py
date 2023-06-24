from typing import List
from item import Item
from property import Property

# this class handles essential materials
class Resource(Item):
    def __init__(self, name: str, properties: List[Property]):
        Item.__init__(self, name)
        self.properties: List[Property] = properties
