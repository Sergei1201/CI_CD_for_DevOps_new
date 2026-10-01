class Person:
    def __init__(self, firstName: str, lastName: str, age: int, isMale: bool) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.isMale = isMale


    def __str__(self) -> str:
        return f"Information on the object: {self.firstName} {self.lastName} {self.age} {self.isMale}"


p1 = Person("John", "Doe", 35, True)
p2 = Person("Jane", "Doe", 30, False)
print(p1)
print(p2)

