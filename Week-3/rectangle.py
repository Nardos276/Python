class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
rect = Rectangle(5, 10)
area = rect.width * rect.height
print("Area:", area)
