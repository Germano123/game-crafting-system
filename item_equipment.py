from item import Item
from typing import List
from effect import Effect

# this class handles equipment itens
class Equipment(Item):
    def __init__(self, name):
        Item.__init__(self, name)
        self.effects: List[Effect] = []
