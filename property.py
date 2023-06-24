from typing import Dict

# this class handles the characteristics that a resource can have
class PropertyData():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "%s" %(self.name)

class Property():
    def __init__(self, property: PropertyData, level: int):
        self.name = property.name
        self.level = level

    def __str__(self):
        return "%s %d" %(self.name, self.level)

# Game Properties
def createNewPropertyData(property):
    global properties
    global propertyCount
    properties[propertyCount] = property
    propertyCount += 1

properties: Dict[int, PropertyData] = {}
propertyCount: int = 0

createNewPropertyData(PropertyData("Dureza"))
createNewPropertyData(PropertyData("Leveza"))
createNewPropertyData(PropertyData("Durabilidade"))
createNewPropertyData(PropertyData("Proteção"))

#for propCount in range(0, len(properties)):
#    print(properties[propCount])
