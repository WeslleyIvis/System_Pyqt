class Dex():
    def __init__(self):
        self.pi = 3.14
        self.value = 0

    def somar(self, x: int, y: int):
        self.value = x + y
        return self.value
    
    def status(self):
        return {
            'value': self.value,
            'pi': self.pi
        }



classe = Dex()
print(classe.somar(5, 10))
print(classe.status())