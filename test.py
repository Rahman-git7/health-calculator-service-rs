import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(1.60, 60), 23.44, places=2)

    def test_calculate_bmr_male(self):
        result = calculate_bmr(175, 70, 25, 'male')
        self.assertAlmostEqual(result, 1724.05, places=2)

    def test_calculate_bmr_female(self):
        result = calculate_bmr(160, 55, 30, 'female')
        self.assertAlmostEqual(result, 1321.96, places=2)


    def test_calculate_bmr_invalid_gender(self):
        with self.assertRaises(ValueError):
            calculate_bmr(170, 65, 25, 'other')

if __name__ == '__main__':
    unittest.main()
