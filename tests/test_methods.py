import unittest
import blackbear as bb


class TestMethods(unittest.TestCase):

    def test_sumv(self):
        data = {'foo': 60,
                'bar': 15,
                'baz': 5}
        self.assertEqual(bb.sumv(data), 80)

    def test_sumk(self):
        data = {1: 60,
                2: 15,
                3: 5}
        self.assertEqual(bb.sumk(data), 6)

    def test_productv(self):
        data = {'foo': 60,
                'bar': 15,
                'baz': 5}
        self.assertEqual(bb.productv(data), 4500)

    def test_add(self):
        data = {'foo': 60,
                'bar': 15,
                'baz': 24}
        out = {'foo': 70,
               'bar': 25,
               'baz': 34}
        self.assertEqual(bb.add_scalar(data, value=10), out)

    def test_subtract(self):
        data = {'foo': 60,
                'bar': 15,
                'baz': 24}
        out = {'foo': 50,
               'bar': 5,
               'baz': 14}
        self.assertEqual(bb.subtract_scalar(data, value=10), out)

    def test_multiply(self):
        data = {'foo': 60,
                'bar': 15,
                'baz': 24}
        self.assertEqual(bb.multiply_scalar(data, value=1), data)

    def test_divide(self):
        data = {'foo': 60,
                'bar': 15,
                'baz': 24}
        self.assertEqual(bb.divide_scalar(data, value=1), data)

    def test_divide_dict(self):
        _in1 = {'foo': 60,
                'bar': 15,
                'baz': 24}
        _in2 = {'foo': 2,
                'bar': 3,
                'baz': 8}
        out = {'foo': 30,
               'bar': 5,
               'baz': 3}
        self.assertEqual(bb.divide(_in1, _in2), out)

    def test_add_dict(self):
        _in1 = {'foo': 60,
                'bar': 15,
                'baz': 24}
        _in2 = {'foo': 2,
                'bar': 3,
                'baz': 8}
        out = {'foo': 62,
               'bar': 18,
               'baz': 32}
        self.assertEqual(bb.add(_in1, _in2), out)

    def test_mul_dict(self):
        _in1 = {'foo': 60,
                'bar': 15,
                'baz': 24}
        _in2 = {'foo': 2,
                'bar': 3,
                'baz': 1}
        out = {'foo': 120,
               'bar': 45,
               'baz': 24}
        self.assertEqual(bb.multiply(_in1, _in2), out)

    def test_sub_dict(self):
        _in1 = {'foo': 60,
                'bar': 15,
                'baz': 24}
        _in2 = {'foo': 2,
                'bar': 3,
                'baz': 1}
        out = {'foo': 58,
               'bar': 12,
               'baz': 23}
        self.assertEqual(bb.subtract(_in1, _in2), out)

    def test_add_dict_fill(self):
        _in1 = {'foo': 60,
                'bar': 15,
                'baz': 24}
        _in2 = {'foo': 2,
                'baz': 8}
        out = {'foo': 62,
               'bar': 25,
               'baz': 32}
        self.assertEqual(bb.add(_in1, _in2, fill=10), out)

    def test_add_dict_fill_sparse(self):
        _in1 = {'foo': 60,
                'bar': 15,
                'baz': 24}
        _in2 = {'foo': 2,
                'exogenous': "not relevant",
                'baz': 8}
        out = {'foo': 62,
               'bar': 25,
               'baz': 32}
        self.assertEqual(bb.add(_in1, _in2, fill=10), out)

    def test_add_dict_fill_sparse(self):
        _in1 = {'foo': 60,
                'bar': 15,
                'baz': 24}
        _in2 = {'foo': 2,
                'exogenous': "not relevant",
                'baz': 8}
        out = {'foo': 62,
               'bar': 25,
               'baz': 32}
        self.assertEqual(bb.add(_in1, _in2, fill=10), out)

    def test_add_dict_fill_empty(self):
        _in1 = {}
        _in2 = {'foo': 2,
                'exogenous': "not relevant",
                'baz': 8}
        out = {'foo': 62,
               'bar': 25,
               'baz': 32}
        self.assertEqual(bb.add(_in1, _in2, fill=10), {})


if __name__ == '__main__':
    unittest.main()
