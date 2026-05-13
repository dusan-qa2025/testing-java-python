from Car import Car


class TestCar():

    def test_accelerate_from_stop(self):
        car = Car()
        result = car.accelerate(25)

        expected = 25

        if result == expected:
            print("Test CUT01 - accelerate from stop - passed. All good.")
        else:
            print("Test CUT01 - accelerate from stop - failed. Reason: Expected and actual result not equal.")


    def test_accelerate_for_moving_vehicle(self):
        car = Car()
        car.speed = 50

        expected = 55

        result = car.accelerate()

        if result == expected:
            print("Test CUT02 - accelerate for moving vehicle - passed. All good.")
        else:
            print("Test CUT02 - accelerate for moving vehicle - failed. Reason: Expected and actual result not equal.")

    def test_breaking_at_zero(self):

        expected = 0

        car = Car()
        result = car.brake()

        
        if result == expected:
            print("Test CUT03 - braking at zero - passed. All good.")
        else:
            print("Test CUT03 - braking at zero - failed. Reason: Expected and actual result not equal.")

    def test_get_status(self):
        car = Car("Honda", "Accord", 95)

        expected = "A vehicle Honda Accord is moving at a speed of 95 km/h."
        result = car.get_status()

        
        if result == expected:
            print("Test CUT04 - get status - passed. All good.")
        else:
            print("Test CUT04 - get status - failed. Reason: Expected and actual result not equal.")


      

