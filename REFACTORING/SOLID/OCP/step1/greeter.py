class Greeter:
    def __init__(self) -> None:
        super().__init__()
        self.__formality = "normal"

    def get_formality(self):
        if self.__formality == "formal":
            formality = Formality()
        elif self.__formality == "casual":
            formality = Casual()
        elif self.__formality == "intimate":
            formality = Intimate()
        else:
            formality = Normal()
        return formality

    def greet(self) -> str:
        return self.get_formality().say_hi()

    def set_formality(self, formality: str):
        self.__formality = formality

class Formality:
    def say_hi(self):
        return "Good Morning"

class Casual:
    def say_hi(self):
        return "Sup bro?"

class Intimate:
    def say_hi(self):
        return "Hello Darling!"

class Normal:
    def say_hi(self):
        return "Hello!"