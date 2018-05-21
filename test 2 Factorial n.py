import unittest, importlib
module_factorial = importlib.import_module("2 Factorial n") 

class TestFactorial(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_input(self):
        self.assertEqual(module_factorial.check_input("-9"), False)
        self.assertEqual(module_factorial.check_input("13"), 13)
        self.assertEqual(module_factorial.check_input("10.20"), False)
 
    def test_recursion_factorial(self):
        self.assertEqual(module_factorial.recursion_factorial(0), 1)
        self.assertEqual(module_factorial.recursion_factorial(6), 720)
        self.assertEqual(module_factorial.recursion_factorial(13), 6227020800)
        self.assertEqual(module_factorial.recursion_factorial(1), 1)
        self.assertEqual(module_factorial.recursion_factorial(8), 40320)

    def test_non_recursion_factorial(self):
        self.assertEqual(module_factorial.non_recursion_factorial(0), 1)
        self.assertEqual(module_factorial.non_recursion_factorial(6), 720)
        self.assertEqual(module_factorial.non_recursion_factorial(13), 6227020800)
        self.assertEqual(module_factorial.non_recursion_factorial(1), 1)
        self.assertEqual(module_factorial.non_recursion_factorial(8), 40320)
        
 
if __name__ == '__main__':
    unittest.main()
