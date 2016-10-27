import types
from collections import Counter
# Итератор для удаления дубликатов
class Unique(object):
    ignore_case = False
    items = []
    gg = []
    ind = 0
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']
        if isinstance(items, types.GeneratorType):
            self.items = list(items)
        else:
            self.items = items

    def __next__(self):
        # Нужно реализовать __next__
        while True:
            if self.ind == len(self.items) - 1:
                raise StopIteration
            self.ind += 1
            val = self.items[self.ind]
            val2 = val
            if self.ignore_case:
                val2 = val2.lower()
            if val2 not in self.gg:
                self.gg.append(val2)
                return val

    def __iter__(self):
        del self.gg[:]
        self.ind = -1
        return self