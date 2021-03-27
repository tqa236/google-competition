from array import array
import unittest
import hypothesis.strategies as st
from hypothesis import given
from Reversort_Engineering import func, func_rev


class Test(unittest.TestCase):
    def test_1(self):
        array = func(0, 4, 6)
        array = array[array.index(":") + 1 :]
        array = [int(i) for i in array.split()]
        # print(array)
        self.assertEqual(func_rev(array), 6)

    @given(
        st.integers(min_value=2, max_value=100),
        st.integers(min_value=1, max_value=1000),
    )
    def test_random(self, n, c):
        array = func(0, n, c)
        if "IMPOSSIBLE" not in array:
            array = array[array.index(":") + 1 :]
            array = [int(i) for i in array.split()]
            print(n, c, array)
            self.assertEqual(func_rev(array), c)


if __name__ == "__main__":
    unittest.main()