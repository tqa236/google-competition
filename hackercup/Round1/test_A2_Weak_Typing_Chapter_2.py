import unittest
import hypothesis.strategies as st
from hypothesis import given
from A2_Weak_Typing_Chapter_2 import func


class Test(unittest.TestCase):
    # def test_1(self):
    #     solution = Solution()
    #     self.assertEqual(solution.{method}(), True)

    @given(st.from_regex("X|O|F", fullmatch=True))
    def test_random(self, val):
        self.assertEqual(func(0, val), func(0, val[::-1]))


if __name__ == "__main__":
    unittest.main()
