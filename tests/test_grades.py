import sys, os, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from grades import average, letter_grade


class TestGrades(unittest.TestCase):
    def test_average(self):                      # Issue #1
        self.assertEqual(average([80, 90, 100]), 90)

    def test_average_empty(self):                # Issue #2
        self.assertEqual(average([]), 0)

    def test_letter_boundaries(self):            # Issue #3
        self.assertEqual(letter_grade(90), "A")
        self.assertEqual(letter_grade(80), "B")
        self.assertEqual(letter_grade(70), "C")
        self.assertEqual(letter_grade(60), "D")

    def test_lowest(self):                       # Issue #4
        from grades import lowest
        self.assertEqual(lowest([70, 40, 95]), 40)


if __name__ == "__main__":
    unittest.main()
