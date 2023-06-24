from typing import List, Dict
from item_resource import Resource
from property import Property

# Game tests
def createNewProperty(property):
    properties[propertyId] = property
    propertyId += 1

properties: Dict[int, Property] = {}
propertyId = 0

createNewProperty(Property("Dureza", 1))
createNewProperty(Property("Dureza", 2))
createNewProperty(Property("Dureza", 3))
createNewProperty(Property("Leveza", 1))
createNewProperty(Property("Leveza", 2))
createNewProperty(Property("Leveza", 3))
createNewProperty(Property("Durabilidade", 1))
createNewProperty(Property("Durabilidade", 2))
createNewProperty(Property("Durabilidade", 3))
createNewProperty(Property("Proteção", 1))
createNewProperty(Property("Proteção", 2))
createNewProperty(Property("Proteção", 3))

for prop in properties:
    print(prop)

resources: List[Resource] = [
    Resource("Aço Damasco", []),
    Resource("Mithril", []),
    Resource("Vidro dracônico", []),
    Resource("Madeira de Ébano", []),
    Resource("Pedra de raios", []),
    Resource("Cristal de gelo profundo", []),
    Resource("Prata lunar", []),
    Resource("Couro de dragão", []),
    Resource("Essência arcana", []),
    Resource("Sangue de Fênix", []),
]

#for resource in resources:
 #   print(resource)
