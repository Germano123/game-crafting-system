# base class for itens
class Item():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
