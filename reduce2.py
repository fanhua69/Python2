import functools

d={'key1':1, 'key2':2,'key3':3}
s=functools.reduce(lambda a, k : a+d[k], d, 10)
print(s)