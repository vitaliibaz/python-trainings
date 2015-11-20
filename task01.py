# Создать класс Person, описывающий человека. Конструктор принимает параметрами
# имя и возраст и сохраняет себе эту информацию в классе. Также создать функцию say,
# которая не принимает параметров, печатает на экран
# "Hello, my name is <??> and I am <??> years old.", ничего не возвращает.
# Для демонстрации, работы, инициализировать две персоны Alice и Bob,
# и вызвать функцию say для каждого из них. Результат запуска программы будет две строчки,
# напечатанные в консоль.

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("Hello, my name is {0} and I am {1} years old.".format(self.name, self.age))


alice = Person('Alice', '18')
bob = Person('Bob', '81')

alice.say()
bob.say()
