from typing import override


class Rifle:
    def shot(self):
        print('RFILE')


class Shotgun(Rifle):
    def shot(self):
        print('SHOTGUN')


class SniperRifle(Rifle):
    def shot(self):
        print('SNIPER')


def client(r: Rifle):
    r.shot()

client(Shotgun())
client(SniperRifle())