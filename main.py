from datetime import datetime


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def calculate_year_of_turning_100(self) -> int:
        current_year = datetime.now().year
        years_until_100 = 100 - self.age
        years_of_turning_100 = current_year + years_until_100
        return years_of_turning_100


class SeniorPerson(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def is_senior(self) -> bool:
        return self.age >= 65


person1 = SeniorPerson("Bob", 65)
print(f"Name: {person1.get_name()}")
print(f"Age: {person1.get_age()}")

person1.set_name("John")
person1.set_age(70)

print(f"Updated name: {person1.get_name()}")
print(f"Updated age: {person1.get_age()}")

years_of_turning_100 = person1.calculate_year_of_turning_100()
print(f"{person1.get_name()}, will turn 100 in the year {years_of_turning_100}")
print(f"{person1.get_name()} is a senior: {person1.is_senior()}")
