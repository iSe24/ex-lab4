# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2
def print_result(decor):            #decor - то что заворачиваем
    def obertka(*args):             #ВО ЧТО заворачиваем
        print(decor.__name__)       #вывод названия функции-decora - по условию
        if len(args) > 0:           
            d = decor(args[0])
        else:
            d = decor()
        if (type(d) == list):               
            print("\n".join([str(x) for x in d]))
        elif (type(d) == dict):
            print("\n".join([str(x) + " = " + str(d[x]) for x in d]))
        else:
            print(d)
        return(d)
    return obertka
