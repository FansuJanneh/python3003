# Kirjoita luokka Circle
# - Luokka ottaa rakentajan parametrina ympyrän säteen
# - Luokalla on kaksi metodia
#  - area, laskee ja palauttaa ympyrän pinta-alan
#  - circumference, laskee ja palauttaa ympyrän kehän pituuden

# sisältää piin (math.pi)
# import math

# Otetaan PI vakio käyttöön myMath-moduulista
from myMath import PI


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2  # self.radius^2

    def circumference(self):
        return 2 * PI * self.radius


circle = Circle(5)
print("Radius", circle.radius)
print("Area", circle.area())
print("Circumference", circle.circumference())
