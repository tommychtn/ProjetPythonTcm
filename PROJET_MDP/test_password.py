import unittest
from password_generator import PasswordGenerator
from password_tester import PasswordTester

class TestPassword(unittest.TestCase):
    def test_password_generation(self):
        password = PasswordGenerator.generate_password(2, 2, 2, 2)
        self.assertEqual(len(password), 8)
    
    def test_entropy_calculation(self):
        entropy = PasswordTester.calculate_entropy("Aa1!")
        self.assertAlmostEqual(entropy, 18.77, places=2)
    
    def test_strength_evaluation(self):
        self.assertEqual(PasswordTester.evaluate_strength(20), "Faible")
        self.assertEqual(PasswordTester.evaluate_strength(40), "Forte")

if __name__ == "__main__":
    unittest.main()
