class Car():
    make = ""
    model = ""
    speed = 0

    def __init__(self, make = "", model = "", speed = 0):
        self.make = make
        self.model = model
        self.speed = speed

    def accelerate(self, value = 5):
        self.speed = self.speed + value
        return self.speed
    
    def brake(self, value = 5):

        if value > self.speed:
            self.speed = 0
        else:
            self.speed = self.speed - value
        return self.speed
    
    def get_status(self):
        return f"A vehicle {self.make} {self.model} is moving at a speed of {self.speed} km/h."
