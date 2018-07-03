# -*- coding:utf-8 -*-
from collections import namedtuple


City = namedtuple('City', 'name country population coordinates')
shanghai = City('Shanghai', 'CN', 25, (1, 2))
print(shanghai)
print(shanghai.country)
print(shanghai[2])
