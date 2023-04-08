def get_unique_list_numbers():
    from random import randint
    li = []
    while len(li) < 15:
        num = randint(-10, 10)
        if num not in li:
            li += [num]
    return li
    #  написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
