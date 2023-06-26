class Animal:
    def __init__(self, name: str, weight: int, age:int):
        self.name = name
        self.weight = weight
        self.age = age


    def move(self):
        pass

    def say(self):
        pass

class Bird(Animal):
    def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
        super().__init__(name, weight, age)
        self.bird_type = bird_type
        self.sound = sound

    def move(self):
        return 'Fly'

    def say(self):
        return self.sound
    
class Dog(Animal):
    def __init__(self, name: str, weight: int, age: int, dog_type: str):
        super().__init__(name, weight, age)
        self.dog_type = dog_type

    def move(self):
        return 'Run'

    def say(self):
        return 'Gav'




