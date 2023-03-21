class Parent():
    """"""
    
    def __init__(self, name):
        self.name = name


class Enfant1(Parent):
    """"""
    
    def bark(self):
        print(f"\033[3;2m *{self.name} aboie*\033[0m")


class Enfant2(Parent):
    """"""
    
    def meow(self):
        print(f"\033[3;2m *{self.name} miaule*\033[0m")


def main():
    enfant1 = Enfant1("Ryad", ) # create a dog and give it a name
    print(f"created dog \033[44m {dog.name} \033[0m") # print the dog's name
    dog.bark()

    enfant2 = Enfant2("Felix") # create a cat and give it a name
    print(f"created cat \033[44m {cat.name} \033[0m") # print the cat's name
    cat.meow()


if __name__ == "__main__":
    main() # call main function to avoid global variables