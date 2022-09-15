
class Button:
    def __init__(self, color, bg, text):
        self.bg = bg
        self.color = color
        self.text = text
    def speak(self, age):
        print(self.name)
        print(self.age)
    def f(self, x):
        print('F')
    @classmethod
    def createPrimary(cls, text):
        return cls("Red", "Blue", text)

class Button2(Button):
    pass

print(Button2.createPrimary("XXX").bg)