class Marin:
    def __init__(self):
        self.hp = 80
        self.mana = 200

    def attack(self):
        self.hp += 1
        self.mana -= 10

    def move(self):
        self.hp -= 10
        self.mana += 5

    def status(self):
        print(f'{self.hp} {self.mana}')

m1 = Marin() # instance
m1.attack()
m1.move()
m1.status()

m2 = Marin()
m2.attack()
m2.attack()
m2.move()
m2.status()
