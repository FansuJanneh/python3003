# Kirjoita luokka Point
# Point sisältää jäsenmuuttujat X ja Y, jotka kuvaavat pisteen koordinaatteja

# Kirjoita luokka Rectangle
# Rectangle ottaa rakentajan parametreina kaksi Point-oliota:
# - bottomLeft: nelikulmion vasemman alanurkan koordinaatti
# - topRight: nelikulmion oikean yläkulman koordinaatti
#
# Luokan jäsenfunktiot:
# - height: laskee ja palauttaa nelikulmion korkeuden
# - width: laskee ja palauttaa nelikulmion leveyden
# - area: laskee ja palauttaa nelikulmion pinta-alan

class Point():
   def __init__(self, x, y):
      self.x = x
      self.y = y

class Rectangle():
   def __init__(self, bottomLeft, topRight):
      self.bottomLeft = bottomLeft
      self.topRight = topRight
      if isinstance(self.bottomLeft, Point) == False or isinstance(self.topRight, Point) == False:
         raise AttributeError
   
   def height(self):
      return self.topRight.y - self.bottomLeft.y
   
   def width(self):
      return self.topRight.x - self.bottomLeft.x

   def area(self):
      return self.height() * self.width()   

point1 = Point(0, 0)
point2 = Point(5, 8)

try:
   rectangle = Rectangle(point1, 2)
   print("Height", rectangle.height())
   print("Width", rectangle.width())
   print("Area", rectangle.area())
except AttributeError:
   print("Virheelliset parametrit")