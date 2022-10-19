list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max = list_numbers[0]
max_number = 0
for i in range(20):
    if list_numbers [i] > max:
      max = list_numbers [i]
      max_number = i
a = list_numbers [-1]
list_numbers[-1] = max
list_numbers [max_number] = a




print(list_numbers)
