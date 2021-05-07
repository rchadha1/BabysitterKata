import unittest
from babysitter import *

#testing compute salary with multiple cases
class TestBabysitterMethods(unittest.TestCase): 
    def test_compute_salary(self):    
        with self.subTest():
            self.assertEqual(compute_salary("A", "6:30", "9:30"), 60)
        with self.subTest():
            self.assertEqual(compute_salary("B", "9:15", "2:00"), 190)
        with self.subTest():
            self.assertEqual(compute_salary("c", "10:00", "4:00"), 85)
        with self.subTest():
            self.assertEqual(compute_salary("B", "7:30", "10:59"), 44)
        with self.subTest():
            self.assertEqual(compute_salary("C", "6:00", "11:20"), 95)
        with self.subTest():
            self.assertEqual(compute_salary("A", "7:15", "12:00"), 70)
        with self.subTest():
            self.assertEqual(compute_salary("B", "8:45", "11:45"), 30)
        with self.subTest():
            self.assertEqual(compute_salary("a", "2:00", "3:00"), 20)
        with self.subTest():
            self.assertEqual(compute_salary("C", "5:00", "2:45"), 80)
        with self.subTest():
            self.assertEqual(compute_salary("A", "11:30", "1:08"), 50)
        with self.subTest():
            self.assertEqual(compute_salary("B", "6:23", "8:56"), 48)
        with self.subTest():
            with self.assertRaises(KeyError):
                compute_salary("b", "4:05", "5:06")
    


if __name__ == "__main__":
    unittest.main()
