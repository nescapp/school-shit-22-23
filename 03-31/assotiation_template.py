# make a basic association between two objects

class Association:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def __repr__(self):
        return "%s %s" % (self.obj1, self.obj2)


class AssociationManager:
    def __init__(self):
        self.associations = []

    def add(self, obj1, obj2):
        self.associations.append(Association(obj1, obj2))

    def __repr__(self):
        return str(self.associations)

if __name__ == "__main__":
    am = AssociationManager()
    am.add("a", "b")
    am.add("c", "d")
    print(am)