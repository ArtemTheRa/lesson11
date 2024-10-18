my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
element = 0
while len(my_list) > element:
    if my_list[element] > 0:
        print(my_list[element])
        element += 1
        continue
    if my_list[element] == 0:
        element += 1
        continue
    else:
        break