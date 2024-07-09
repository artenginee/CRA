class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"{self.x}, {self.y} 에 버튼 찍힘")


class DrawButtonMachine:
    def __init__(self):
        self._buttons = []

    def add(self, button: Button):
        self._buttons.append(button)


a = DrawButtonMachine()
a.add(Button(1, 2))
a.add(Button(2, 3))
a.add(Button(5, 5))
a.add(Button(7, 1))
a.draw()
