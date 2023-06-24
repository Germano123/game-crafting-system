# this class handles the characteristics that a resource can have
class Property():
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def __str__(self):
        return "%s %d" %(self.name, self.level)
