#  Итератор

'''
mas = [1, 2, 3, 4, 5]
itr = iter(mas)
for i in range(5):
    print(next(itr))
'''

'''
class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

s_iter1 = SimpleIterator(3)
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
'''

#Генератор
'''
def generator_function():
    for i in range(10):
        yield i
fun = generator_function()
print(next(fun))
print(next(fun))
print(next(fun))
'''
