class Parent():
    """"""
    
    def __init__(self, name):
        self.name = name


class Enfant1(Parent):
    """"""
    
    def bark(self):
        print("")


class Enfant2(Parent):
    """"""
    
    def meow(self):
        print("a")


def main():
    enfant1 = Enfant1("Ryad", ) # create a dog and give it a name
    dog.bark()

    enfant2 = Enfant2("Felix") # create a cat and give it a name
    cat.meow()


if __name__ == "__main__":
    main() # call main function to avoid global variables