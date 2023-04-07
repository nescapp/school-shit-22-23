class Animal():
    
    
    def __init__(self, nom):
        self.nom = nom


class Dog(Animal):
    
    
    def bark(self):
        print(f" *{self.nom} aboie*")


class Cat(Animal):
    
    
    def meow(self):
        print(f" *{self.nom} miaule*")


def main():
    chien = Dog("Rex") 
    print(f"created chien  {chien.nom} ") 
    chien.bark()

    chat = Cat("Felix") 
    print(f"created chat  {chat.nom} ") 
    chat.meow()


if __name__ == "__main__":
    main() 
