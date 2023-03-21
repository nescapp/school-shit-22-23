class Animal():
    """animal class with name attribute"""
    
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    """dog class with bark method"""
    
    def bark(self):
        print(f"\033[3;2m *{self.name} aboie*\033[0m")


class Cat(Animal):
    """cat class with meow method"""
    
    def meow(self):
        print(f"\033[3;2m *{self.name} miaule*\033[0m")


def main():
    dog = Dog("Rex") # create a dog and give it a name
    print(f"created dog \033[44m {dog.name} \033[0m") # print the dog's name
    dog.bark()

    cat = Cat("Felix") # create a cat and give it a name
    print(f"created cat \033[44m {cat.name} \033[0m") # print the cat's name
    cat.meow()


if __name__ == "__main__":
    main() # call main function to avoid global variables