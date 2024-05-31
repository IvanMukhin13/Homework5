immutable_bar = (13, 19, 'Varya','Irina')
print(immutable_bar)
# immutable_bar[0] = 20
# print(immutable_bar) #'tuple' object does not support item assignment
#Кортеж относится к неизменяемому типу списка
mutable_list = [13, 19, 'Ivan', 'Aleksandr']
print(mutable_list)
mutable_list[0] = 15
print(mutable_list)
mutable_list = [13, 19, 'Ivan', 'Aleksandr'] + ['Family', 10]
print(mutable_list)