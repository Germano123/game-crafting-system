from typing import List, Dict
from item import Item
from property import Property, properties

# this class handles essential materials
class Resource(Item):
    def __init__(self, name: str, properties: List[Property]):
        Item.__init__(self, name)
        self.properties: List[Property] = properties

def get_resource_by_name(name: str):
    return resources[name]

resources_list: List[Resource] = [
    Resource("Metal", [
        Property(properties[0], 3),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
    Resource("Madeira", [
        Property(properties[0], 3),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),    
    Resource("Aço Damasco", [
        Property(properties[0], 2),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
    Resource("Mithril", [
        Property(properties[0], 3),
        Property(properties[1], 2),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
    Resource("Vidro dracônico", [
        Property(properties[0], 3),
        Property(properties[1], 3),
        Property(properties[2], 1),
        Property(properties[3], 1),
    ]),
    Resource("Madeira de Ébano", [
        Property(properties[0], 1),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 2),
    ]),
    Resource("Pedra de raios", [
        Property(properties[0], 3),
        Property(properties[1], 1),
        Property(properties[2], 2),
        Property(properties[3], 3),
    ]),
    Resource("Cristal de gelo profundo", [
        Property(properties[0], 3),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
    Resource("Prata lunar", [
        Property(properties[0], 3),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
    Resource("Couro de dragão", [
        Property(properties[0], 3),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
    Resource("Essência arcana", [
        Property(properties[0], 3),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
    Resource("Sangue de fênix", [
        Property(properties[0], 3),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
]

resources: Dict[str, Resource] = {}
