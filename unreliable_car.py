from prac8.car import Car
import random


class UnavaliableCar(Car):

    def _int_(self, name, fuel, reliability):
        super()._init_(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        self.distance = distance

        distance = random.randint(1, 100)
        return distance

        if distance < self.reliability:
            return self.distance
        else:
            return 'over ride'

