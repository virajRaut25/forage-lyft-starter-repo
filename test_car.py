import unittest
from datetime import datetime

from carFactory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        cf = CarFactory()
        cf.create_calliope(last_service_date,
                           current_mileage, last_service_mileage)
        self.assertTrue(cf.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        cf = CarFactory()
        cf.create_calliope(last_service_date,
                           current_mileage, last_service_mileage)
        self.assertFalse(cf.car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        cf = CarFactory()
        cf.create_calliope(last_service_date,
                           current_mileage, last_service_mileage)
        self.assertTrue(cf.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        cf = CarFactory()
        cf.create_calliope(last_service_date,
                           current_mileage, last_service_mileage)
        self.assertFalse(cf.car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_glissade(last_service_date,
                           current_mileage, last_service_mileage)
        self.assertTrue(cf.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_glissade(last_service_date,
                           current_mileage, last_service_mileage)
        self.assertFalse(cf.car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_glissade(last_service_date,
                           current_mileage, last_service_mileage)
        self.assertTrue(cf.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_glissade(last_service_date,
                           current_mileage, last_service_mileage)
        self.assertFalse(cf.car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        cf = CarFactory()
        cf.create_palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(cf.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        warning_light_is_on = False

        cf = CarFactory()
        cf.create_palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(cf.car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        cf = CarFactory()
        cf.create_palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(cf.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        cf = CarFactory()
        cf.create_palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(cf.car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_rorschach(last_service_date,
                            current_mileage, last_service_mileage)
        self.assertTrue(cf.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_rorschach(last_service_date,
                            current_mileage, last_service_mileage)
        self.assertFalse(cf.car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_rorschach(last_service_date,
                            current_mileage, last_service_mileage)
        self.assertTrue(cf.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_rorschach(last_service_date,
                            current_mileage, last_service_mileage)
        self.assertFalse(cf.car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_thovex(last_service_date, current_mileage,
                         last_service_mileage)
        self.assertTrue(cf.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_thovex(last_service_date, current_mileage,
                         last_service_mileage)
        self.assertFalse(cf.car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_thovex(last_service_date, current_mileage,
                         last_service_mileage)
        self.assertTrue(cf.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        cf = CarFactory()
        cf.create_thovex(last_service_date, current_mileage,
                         last_service_mileage)
        self.assertFalse(cf.car.needs_service())


if __name__ == '__main__':
    unittest.main()
