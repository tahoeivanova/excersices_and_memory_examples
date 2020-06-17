import sys
from pympler import asizeof
from pympler import muppy, summary

all_objects_1 = muppy.get_objects()

# Shallow size (например, размер листа, но не объектов, которые в нем есть)
print(sys.getsizeof(1)) # 28
print(sys.getsizeof(54234.000342314000)) # 24
print(sys.getsizeof(None)) # 16
print(sys.getsizeof([])) # 72
print(sys.getsizeof([1,2,3,4, ['s','l', ['a',1]]])) # 112
print(sys.getsizeof({})) # 248
print(sys.getsizeof(tuple())) # 56


print()
# Deep size (идет по иерархии объектов вглубь, суммирует)
print(asizeof.asizeof(1)) # 32
print(asizeof.asizeof(54234.000342314000)) # 24
print(asizeof.asizeof(None)) # 16
print(asizeof.asizeof([])) # 72
print(asizeof.asizeof([1,2,3,4, ['s','l', ['a',1]]])) # 592
print(asizeof.asizeof([1,2,3,4, ['s','l', ['a',1, [None, 1, {'a': 1, 'b': 'a'}]]]])) # 1016
print(asizeof.asizeof({})) # 248
print(asizeof.asizeof(tuple())) # 56
print(asizeof.asizeof(set())) # 232

all_objects_2 = muppy.get_objects()
sum_1 = summary.summarize(all_objects_1)
sum_2 = summary.summarize(all_objects_2)
summary.print_(summary.get_diff(sum_1, sum_2))

