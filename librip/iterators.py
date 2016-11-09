import types
from collections import Counter
# Итератор для удаления дубликатов
class Unique(object):

    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False
        self.items = iter(items)        #цикл
        self.gg = set()     #множество без повторов
    def __next__(self):
        # Нужно реализовать __next__
        while True:
            sth = next(self.items)
            sthnow = sth
            if self.ignore_case:
                sthnow = sthnow.lower()
            if not sthnow in self.gg:
                self.gg.add(sthnow)
                return sth #мы же должны вернуть значение таким какое оно есть , а не уменьшенным в предыдущем шаге

    def __iter__(self):
        return self