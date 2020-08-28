import  abc
class Animal(metaclass=abc.ABCMeta) : #只能继承，不能实例化
    @abc.abstractclassmethod
    def run(self):
        pass
    @abc.abstractclassmethod
    def eat(self):
        pass
class People(Animal):
    def run(self):
        print('people is running')

    def eat(self):
        print('people is eating')

class Pig(Animal):
    def run(self):
        print('people is walking')

    def eat(self):
        print('people is eating')

class Dog(Animal):
    def run(self):
        print('people is walking')

    def eat(self):
        print('people is eating')
dog=Dog()
dog.run()