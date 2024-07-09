class Rectangle:
    def __init__(self):
        self.height = 0
        self.width = 0

    def set_height(self, h):
        self.height = h

    def set_width(self, w):
        self.width = w

    def area(self):
        return self.height * self.width


class Square(Rectangle):
    def set_height(self, h):
        super().set_width(h)
        super().set_height(h)

    def set_width(self, w):
        super().set_width(w)
        super().set_height(w)


# lsp 가 깨지는 클라이언트 코드
def client(rect: Rectangle):
    rect.set_width(10)
    rect.set_height(20)
    assert  rect.area() == 200
    # 직사각형일 때는 괜찮은데 정사각형으로 클라이언트를 만들 경우 면적 구하는게 깨진다.


client(Rectangle())
client(Square()) # 깨지도록