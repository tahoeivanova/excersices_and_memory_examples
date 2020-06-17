from pympler import asizeof
import sys
def generator_function(num):
    for i in range(num):
        yield (i**3)

gen_list = [x**3 for x in  range(1000)]

gen = generator_function(1000000000000)
print(sys.getsizeof(gen))
print(sys.getsizeof(gen_list))

print(asizeof.asizeof(gen))
print(asizeof.asizeof(gen_list))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

