import random

def get_incontine_nums(array):
    result_list = [0 for i in range(len(array))]
    print(result_list)
    for num in array:
        print('Num------------>', num)
        while True:
            index = random.randint(0, len(array) - 1)
            print('index --------------------------->', index)
            print('result_list - index  -------------------------------', result_list[index] )
            if result_list[index] == 0:
                if index == 0:
                    right_node =  result_list[index + 1]
                    right = abs(num - right_node) != 1
                    if num == 1 and right_node == 0:
                        right = True
                    if right:
                        result_list[index] = num
                        break
                elif index == len(array)-1:
                    left_node = result_list[index - 1]
                    left =  abs(num - left_node) != 1
                    if num == 1 and left_node == 0:
                        left = True
                    if left:
                        result_list[index] = num
                        break
                else:
                    left_node = result_list[index - 1]
                    left =  abs(num - left_node) != 1
                    if num == 1 and left_node == 0:
                        left = True
                    right_node =  result_list[index + 1]
                    right = abs(num - right_node) != 1
                    if num == 1 and left_node == 0:
                        right = True
                    if left and right:
                        result_list[index] = num
                        break
        print(num, '------------>' , result_list)
    return result_list
            

mylist = [1, 2, 3, 4, 5, 6, 7, 8]
print('=====================')
res = get_incontine_nums(mylist)
print(res)