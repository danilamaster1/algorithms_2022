"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

company_dict_ = {
    170000: 'Nvidia',
    240000: 'AMD',
    500000: 'Intel',
    150000: 'Nokia',
    130000: 'Samsung'
}


# Вариант 1 - O(n log n) - этот вариант предпочтительнее, так как имеет меньшую сложность, чем O(n^2)
def top_company_1(company_dict):
    lst = sorted(list(company_dict.keys()))[::-1][:3]   # O(n log n)
    for i in lst:                                       # O(1)
        print(f'{company_dict[i]} - {i}')               # O(1)


top_company_1(company_dict_)

print('*' * 30)


# Вариант 2 O(n^2)
def top_company_2(company_dict):
    lst = list(company_dict.keys())                    # O(1)
    for i in range(len(lst)-1):                        # O(n)
        for j in range(len(lst)-i-1):                  # O(n^2)
            if lst[j] < lst[j + 1]:                    # O(1)
                lst[j], lst[j+1] = lst[j+1], lst[j]    # O(1)
    return [company_dict[i] for i in lst[:3]]          # O(n)


print(top_company_2(company_dict_))
