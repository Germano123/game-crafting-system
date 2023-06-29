from typing import List, Dict
from item_resource import Resource
from property import properties, createNewPropertyData, Property
from item_equipment import createEquipment
from item_resource import resources

# Game tests

# test game properties
#print("Types of properties:")
#for propCount in range(0, len(properties)):
#    print(properties[propCount])

# test game resources
print("Resources:")
for index in range(0, len(resources)):
   print(resources[index])

# 0 Dureza -> Dano
# 1 Leveza -> Agilidade
# 2 Durabilidade -> Resistência
# 3 Proteção -> Defesa

# createEquipment(resources=[resources[0]])

#for resource in resources:
 #   print(resource)
