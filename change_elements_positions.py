# Напишите функцию modification(lst), которая принимает список и меняет местами его первый и последний элемент.

def modification(lst):
    lst.reverse()
    new_lst = lst[1:-1]
    new_lst.sort()
    new_lst.insert(0, lst[0])
    new_lst.insert(len(new_lst), lst[-1])
    return new_lst


data = [
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    ['н', 'л', 'о', 'с']
]

test_data = [
    [3, 2, 1], [5, 2, 3, 4, 1], ['с', 'л', 'о', 'н']
]


for i, d in enumerate(data):
    assert modification(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
