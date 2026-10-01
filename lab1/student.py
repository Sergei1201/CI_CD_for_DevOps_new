class Student:
    def __init__(self, first_name: str, last_name: str, age: int, isMale: bool, subject: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.isMale = isMale
        self.subject = subject


    def greetings(self) -> str:
        return f"Greetings to you {self.first_name} {self.last_name}. You are {self.age}, male: {self.isMale} and study {self.subject}"


s1 = Student("John", "Doe", 25, True, "Math")
s2 = Student("Jane", "Doe", 22, False, "Programming")
print(s1.greetings())
print(s2.greetings())


