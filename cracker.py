sticky = input('Enter Sticky Number\n')
half1 = input('Enter Guess Number 1\n')
half2 = input('Enter Guess Number 2\n')

three_1 = (int(half1) + 10)
if three_1 > 40:
    three_1 = (int(three_1)-40)
three_2 = (int(half1) + 20)
if three_2 > 40:
    three_2 = (int(three_2)-40)
three_3 = (int(half1) + 30)
if three_3 > 40:
    three_3 = (int(three_3)-40)
    

three_4 = (int(half2) + 10)
if three_4 > 40:
    three_4 = (int(three_4)-40)
three_5 = (int(half2) + 10)
if three_4 > 40:
    three_4 = (int(three_5)-40)
three_6 = (int(half2) + 10)
if three_4 > 40:
    three_4 = (int(three_6)-40)

three_7 = int(half1)
three_8 = int(half2)


one_1 = (int(sticky)+5)
if one_1 > 40:
    one_1 = (int(one_1)-40)

modulo_one_1 = (int(one_1) % 4)
three_list=[]

modulo_three_1 = (int(three_1) % 4)
if modulo_three_1 == modulo_one_1:
    three_list.append(three_1)
    
modulo_three_2 = (int(three_2) % 4)
if modulo_three_2 == modulo_one_1:
    three_list.append(three_2)

modulo_three_3 = (int(three_3) % 4)
if modulo_three_3 == modulo_one_1:
    three_list.append(three_3)

modulo_three_4 = (int(three_4) % 4)
if modulo_three_4 == modulo_one_1:
    three_list.append(three_4)

modulo_three_5 = (int(three_5) % 4)
if modulo_three_5 == modulo_one_1:
    three_list.append(three_5)

modulo_three_6 = (int(three_2) % 4)
if modulo_three_6 == modulo_one_1:
    three_list.append(three_6)

modulo_three_7 = (int(three_7) % 4)
if modulo_three_7 == modulo_one_1:
    three_list.append(three_7)

modulo_three_8 = (int(three_8) % 4)
if modulo_three_8 == modulo_one_1:
    three_list.append(three_8)

print('The third number is one of the following numbers ')
print(three_list)

true_three = input('Test each number and select the number with the largest gate.\n')

two_1 = (int(modulo_one_1)+2)
if two_1 > 40:
    two_1 = (int(two_1)-40)

two_2 = (int(two_1)+8)
if two_2 > 40:
    two_2 = (int(two_2)-40)

two_3 = (int(two_1)+16)
if two_3 > 40:
    two_3 = (int(two_3)-40)

two_4 = (int(two_1)+24)
if two_4 > 40:
    two_4 = (int(two_4)-40)

two_5 = (int(two_1)+32)
if two_5 > 40:
    two_5 = (int(two_5)-40)




two_6 = (int(modulo_one_1)+6)
if two_6 > 40:
    two_6 = (int(two_6)-40)

two_7 = (int(two_6)+8)
if two_7 > 40:
    two_7 = (int(two_5)-40)

two_8 = (int(two_6)+16)
if two_8 > 40:
    two_8 = (int(two_8)-40)

two_9 = (int(two_6)+24)
if two_9 > 40:
    two_9 = (int(two_9)-40)

two_10 = (int(two_6)+32)
if two_10 > 40:
    two_10 = (int(two_10)-40)


combo1 = (str(one_1) + ',' + str(two_1) + ',' + str(true_three))
combo2 = (str(one_1) + ',' + str(two_2) + ',' + str(true_three))
combo3 = (str(one_1) + ',' + str(two_3) + ',' + str(true_three))
combo4 = (str(one_1) + ',' + str(two_4) + ',' + str(true_three))
combo5 = (str(one_1) + ',' + str(two_5) + ',' + str(true_three))
combo6 = (str(one_1) + ',' + str(two_6) + ',' + str(true_three))
combo7 = (str(one_1) + ',' + str(two_7) + ',' + str(true_three))
combo8 = (str(one_1) + ',' + str(two_8) + ',' + str(true_three))
combo9 = (str(one_1) + ',' + str(two_9) + ',' + str(true_three))
combo10 = (str(one_1) + ',' + str(two_10) + ',' + str(true_three))


print('\nThe combo is one of the following\n' + combo1 + '\n' + combo2 + '\n' + combo3 + '\n' + combo4 + '\n' + combo5 + '\n' + combo6 + '\n' + combo7 + '\n' + combo8 + '\n' + combo9 + '\n' + combo10) 

