import unittest
import xmlrunner
from logic import calculate_pyramidal_sum

class TestPyramidalCalculation(unittest.TestCase):
    def test_standard_values(self):
        # 1 = 1
        self.assertEqual(calculate_pyramidal_sum(1), 1)
        # 1 + 3 = 4
        self.assertEqual(calculate_pyramidal_sum(2), 4)
        # 1 + 3 + 6 = 10
        self.assertEqual(calculate_pyramidal_sum(3), 10)

    def test_zero(self):
        # Сума 0 елементів = 0
        self.assertEqual(calculate_pyramidal_sum(0), 0)

    @unittest.expectedFailure
    def test_negative_value(self):
        calculate_pyramidal_sum(-1)

    def test_invalid_types(self):
        """
        Перевіряємо, що функція не приймає сміття замість цілих чисел.
        Ми очікуємо TypeError.
        """
        # Спроба передати рядок
        with self.assertRaises(TypeError):
            calculate_pyramidal_sum("hello")
            
        # Спроба передати дробове число (float)
        with self.assertRaises(TypeError):
            calculate_pyramidal_sum(5.5)
            
        # Спроба передати None
        with self.assertRaises(TypeError):
            calculate_pyramidal_sum(None)

if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)