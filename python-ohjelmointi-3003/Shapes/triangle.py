class InvalidAnglesError(Exception):
    pass


class Triangle():
    def __init__(self, angle1, angle2, angle3):
        if (angle1 + angle2 + angle3 != 180):
            # Kulmien summa ei täsmää
            raise InvalidAnglesError()

        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def printAngles(self):
        print("Angles:", self.angle1, self.angle2, self.angle3)


triangle = Triangle(60, 60, 30)
triangle.printAngles()
