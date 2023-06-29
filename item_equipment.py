from item import Item
from item_resource import Resource
from typing import List
from effect import Effect

# this class handles equipment itens
class Equipment(Item):
    def __init__(self, name: str, effects: List[Effect]):
        Item.__init__(self, name)
        self.effects: List[Effect] = effects

    def __str__(self):
        return "%s" %(self.name)
    
def createEquipment(resources: List[Resource]):
    result = 0
    for res in resources:
        for prop in res.properties:
            print(prop.level)
