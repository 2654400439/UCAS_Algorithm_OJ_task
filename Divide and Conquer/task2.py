# a = [1,2,3,4,5,5,5,5,5,9,10]
# print(a.index(5))
# a.reverse()
# print(a)
# print(len(a) - a.index(5))

# line_1 = input()
# line_2 = input()
# num = int(line_1.split(' ')[1])
# num_list = int(line_1.split(' ')[0])
# main_list = list(map(int,line_2.split(' ')))
# main_list_reverse = main_list.copy()
# main_list_reverse.reverse()
# line = []
# for i in range(num):
#     line.append(int(input()))
# try:
#     for i in range(num):
#         print(main_list.index(line[i]),end=' ')
#         print(num_list - main_list_reverse.index(line[i])-1)
# except:
#     print('-1 -1')


# a = [1,2,3,4,5]
# b = a.copy()
# b.reverse()
# print(a)
# print(b)


# line_1 = input()
# line_2 = input()
# num = int(line_1.split(' ')[1])
# num_list = int(line_1.split(' ')[0])
# main_list = list(map(int,line_2.split(' ')))
# main_list_reverse = main_list.copy()
# main_list_reverse.reverse()
# line = []
# for i in range(num):
#     line.append(int(input()))
# for i in range(num):
#     try:
#         print(main_list.index(line[i]),end=' ')
#         print(num_list - main_list_reverse.index(line[i])-1)
#     except:
#         a = -1
#         b = -1
#         print(a,b)




# line_1 = input()
# line_2 = input()
# num = int(line_1.split(' ')[1])
# num_list = int(line_1.split(' ')[0])
# main_list = list(map(int,line_2.split(' ')))
# line = []
# for i in range(num):
#     line.append(int(input()))
# for i in range(num):
#     try:
#         starting = main_list.index(line[i])
#         tmp = 1
#         while (starting + tmp) < num_list and main_list[starting + tmp] == line[i]:
#             tmp += 1
#         ending = starting + tmp - 1
#         print(starting,end=' ')
#         print(ending)
#     except:
#         a = -1
#         b = -1
#         print(a,b)


# for i,element in enumerate([1,2,3,4,4,4,5,6,7]):
#     if element == 4:
#         print(i)
#         break

# line_1 = input()
# line_2 = input()
# num = int(line_1.split(' ')[1])
# num_list = int(line_1.split(' ')[0])
# main_list = list(map(int,line_2.split(' ')))
# line = []
# for i in range(num):
#     line.append(int(input()))
# for i in range(num):
#     try:
#         for j, element in enumerate(main_list):
#             if element == line[i]:
#                 starting = j
#                 break
#         tmp = 1
#         while (starting + tmp) < num_list and main_list[starting + tmp] == line[i]:
#             tmp += 1
#         ending = starting + tmp - 1
#         print(starting,end=' ')
#         print(ending)
#     except:
#         a = -1
#         b = -1
#         print(a,b)



#分而治之
# line_1 = input()
# line_2 = input()
# num = int(line_1.split(' ')[1])
# num_list = int(line_1.split(' ')[0])
# main_list = list(map(int,line_2.split(' ')))
# line = []
# for i in range(num):
#     line.append(int(input()))


# global left
# global right
# left = 0
# right = 10
#
# def giao(main_list,target):
#     global left
#     global right
#     if main_list.__len__() == 1:
#         return main_list[0]
#     location = int(main_list.__len__()/2)
#     middle = main_list[location]
#     if middle > target:
#         return giao(main_list[:location],target)#可以
#     elif middle < target:
#         return giao(main_list[location+1:],target)#可以
#     else:
#         return middle
#
# print(giao([1,20,31,42,53,64,75,86,97,108],31))






def giao(main_list,target):
    global left
    global right
    global stationary_list
    if main_list.__len__() == 1:
        if main_list[0] == target:
            return int((left + right)/2)
        else:
            raise Exception()
    location = int((left + right)/2)
    middle = stationary_list[location]
    if middle > target:
        right = location - 1
        return giao(main_list[:location],target)#可以
    elif middle < target:
        left = location + 1
        return giao(main_list[location+1:],target)#可以
    elif middle == target:
        return int((left + right)/2)
    else:
        raise Exception()

def find_left_right(main_list,location,target):
    flag_left = 0
    flag_right = 0
    while (location - flag_left) >= 0 and main_list[location - flag_left] == target:
        flag_left += 1
    while (location + flag_right) <= (main_list.__len__()-1) and main_list[location + flag_right] == target:
        flag_right += 1
    return location - flag_left + 1,location + flag_right - 1

line_1 = input()
line_2 = input()
num = int(line_1.split(' ')[1])
num_list = int(line_1.split(' ')[0])
main_list = list(map(int,line_2.split(' ')))
stationary_list = main_list.copy()
line = []
for i in range(num):
    line.append(int(input()))
for i in range(num):
    try:
        left = 0
        right = num_list - 1
        tmp_location = giao(main_list,line[i])
        result = find_left_right(stationary_list,tmp_location,line[i])
        print(result[0],result[1])
    except:
        a = -1
        b = -1
        print(a,b)