from typing import List, Dict
from item_resource import Resource
from property import properties, createNewPropertyData, Property

# Game tests

# test game properties
print("Types of properties:")
for propCount in range(0, len(properties)):
    print(properties[propCount])

# 0 Dureza -> Dano
# 1 Leveza -> Agilidade
# 2 Durabilidade -> Resistência
# 3 Proteção -> Defesa

resources: List[Resource] = [
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
        Property(properties[0], 2),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
    Resource("Couro de dragão", [
        Property(properties[0], 2),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
    Resource("Essência arcana", [
        Property(properties[0], 2),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
    Resource("Sangue de Fênix", [
        Property(properties[0], 2),
        Property(properties[1], 1),
        Property(properties[2], 3),
        Property(properties[3], 1),
    ]),
]

#for resource in resources:
 #   print(resource)
