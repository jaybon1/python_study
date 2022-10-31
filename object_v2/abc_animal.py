from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def poop(self):
        pass


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self):
        print(f'dog {self.name} eat')

    def sleep(self):
        print(f'dog {self.name} sleep')

    def poop(self):
        print(f'dog {self.name} poop')


class Cat(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self):
        print(f'cat {self.name} eat')

    def sleep(self):
        print(f'cat {self.name} sleep')

    def poop(self):
        print(f'cat {self.name} poop')


if __name__ == '__main__':
    dog = Dog('dog', 2)
    dog.eat()
    dog.sleep()
    dog.poop()

    cat = Cat('cat', 1)
    cat.eat()
    cat.sleep()
    cat.poop()
