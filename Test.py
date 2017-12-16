# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# finally:
#     print('finally...')
# print('END')


# err_raise.py
# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
# foo('0')


# def fool(s):
#     n = int(s)
#     if n == 0:
#         raise ValueError("invalid value %s" % s)
#     return 10 / n
#
#
# def bar():
#     try:
#         fool('0')
#     except ValueError as e:
#         print("ValueError!")
#         raise
#
#
# bar()


import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty




