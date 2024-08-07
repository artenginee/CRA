class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, value):
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True


s = Singleton('test')
print(s.value)
print(s.initialized)