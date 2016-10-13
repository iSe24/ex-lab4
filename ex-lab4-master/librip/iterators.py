# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items=items
        self.current = 0
        self.dublicates=[]
        if len(kwargs)>0 and kwargs['ignore_case']!=None and type(kwargs['ignore_case'])==bool:
             self.ignore_case=kwargs['ignore_case']
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        pass

    def __next__(self):
        # Нужно реализовать __next__
       while True:
           try:
               cur = self.items[self.current]
               self.current+=1
               if (type(cur).__name__=='str') and (self.ignore_case == True):
                   cur_check=cur.uper()
               else:
                   cur_check=cur
               if not cur_check in self.dublicates:
                   self.dublicates.append(cur_check)
                   return cur
           except Exception:
               raise StopIteration

    def __iter__(self):
        return self
