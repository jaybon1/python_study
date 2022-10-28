from animal import Animal
from cat import Cat

Animal.hello()

print()

a = Animal(12)
b = Cat("나옹", 5)

a.eat()
b.eat()

print()

a.get_age()
b.get_age()


print()

Animal.get_count()
Cat.get_count()
