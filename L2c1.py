# -*- coding: utf8 -*-
#Задание 1
listing = []
listing.append(['a', 'b', 'c'])
listing.append((1,2,3,4))
listing.append({'a': 1, 'b': 2, 'c':3})
listing.insert(2, {'m': [1, 2], 'n': 'stri_ng'})
listing[0] = ['k', 'm', 'd']
listing.insert(1, 'привет')
listing.insert(4, 36.36)
print(listing)

for i in listing:
    print(type(i))