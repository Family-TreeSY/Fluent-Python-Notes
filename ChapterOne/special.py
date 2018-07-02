# -*- coding:utf-8 -*-
d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])

print(d.__getitem__('a'))

print(d['a'] == d.__getitem__('a'))
