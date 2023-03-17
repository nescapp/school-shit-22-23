class Animal():
    """animal class"""
    def __init__(self, name):
        self.name = name
    

class Dog(Animal):
    """dog class"""
    def bark(self):
        print(f"\033[3m *{self.name} aboie*\033[0m")

class Cat(Animal):
    """cat class"""
    def meow(self):
        # print(f"\033[3m *{} miaule*\033[0m")
        # précise qui miaule
        print(f"\033[3m *{self.name} miaule*\033[0m")


def main():
    dog = Dog("Rex")
    print(f"created dog \033[44m {dog.name} \033[0m")
    dog.bark()

    cat = Cat("Felix")
    print(f"created cat \033[44m {cat.name} \033[0m")
    cat.meow()

if __name__ == "__main__":
    main()