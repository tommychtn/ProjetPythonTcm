import unittest
from question import Question

class TestQuestion(unittest.TestCase):
    def test_is_correct(self):
        question = Question("Test question?", ["A", "B", "C"], 1)
        self.assertTrue(question.is_correct("b"))
        self.assertFalse(question.is_correct("a"))
        self.assertFalse(question.is_correct("c"))

if __name__ == "__main__":
    unittest.main()
