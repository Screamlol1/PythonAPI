class TestExample:
    def test_check_math(self):
        a=5
        b=9
        expexted_sum = 14
        assert a+b == expexted_sum, f"Sum of variables a and b is not equal to {expexted_sum}"

    def test_check_math2(self):
        a=5
        b=11
        expexted_sum = 14
        assert a+b == expexted_sum, f"Sum of variables a and b is not equal to {expexted_sum}"