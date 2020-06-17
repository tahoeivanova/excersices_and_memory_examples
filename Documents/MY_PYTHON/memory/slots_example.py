class SlotsClass:
    __slots__ = ('a', 'b', 'foo', 'bar')

    def __init__(self):
        self.foo = 10

    # def __del__(self):
    #     print(f'{self} is deleted')

    def __str__(self):
        return f'{self.foo}'


class NotSlotsClass(SlotsClass):
    def __init__(self):
        super().__init__()
        self.a = 1234



obj = SlotsClass()

obj.foo = 5

print(obj.foo)

obj.foo = 101
print(obj.foo)


obj2 = NotSlotsClass()
obj2.c = 3

print(obj2.c, obj2.foo, obj2.a)

# print(obj.__dict__)
print(obj.__slots__)


print(obj2.__dict__)
print(NotSlotsClass.__dict__)

