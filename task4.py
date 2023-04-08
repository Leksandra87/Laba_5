from random import choice

EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    eagle = sum([1 for _ in range(count) if choice(coin) == EAGLE])
    tatl = count - eagle
    if tatl > eagle:
        tatl, eagle = eagle, tatl
    list_freq += [round(tatl / eagle, 4)]
    ...  # подсчитать количество выпаданий орлов и решек

    #  разделить минимальное число среди орлов и решек на максимальное число и сохранить результат

print(list_freq)
