from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ("LeetcodeHelpsMeLearn", [8,13,15], "Leetcode Helps Me Learn"),
                            2: ("icodeinpython", [1,5,7,9], "i code in py thon"), 
                            3: ("spacing", [0,1,2,3,4,5,6], " s p a c i n g")}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case_1(self):
        s, spaces, output = self.__testCases[1]
        result = self.__obj.addSpaces(s = s, spaces = spaces)
        self.assertIsInstance(result, str)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case_2(self):
        s, spaces, output = self.__testCases[2]
        result = self.__obj.addSpaces(s = s, spaces = spaces)
        self.assertIsInstance(result, str)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case_3(self):
        s, spaces, output = self.__testCases[3]
        result = self.__obj.addSpaces(s = s, spaces = spaces)
        self.assertIsInstance(result, str)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()