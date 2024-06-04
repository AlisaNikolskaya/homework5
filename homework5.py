immutable_var = (1, 2, 'one', [3, 4])
print(immutable_var)
#immutable_var[0] = 5
#print(immutable_var) #в консоли будет выдавать ошибку, т.к. кортеж относится к неизменяемым типам данных, т.е в данном случае элемент (1) нельзя заменить на (5)
mutable_list = [1, 2, 'one', 'a', 'b']
mutable_list[0] = 'one'
mutable_list[2] = 3
print(mutable_list)