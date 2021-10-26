height = int(input())
elements = input()

# elements = list(map(int,elements.split(' ')))
elements = [int(i) for i in elements.split(' ')]


elements_triangle = []
flag = 0
for i in range(height):
    tmp = []
    for j in range(i+1):
        tmp.append(elements[flag])
        flag += 1
    elements_triangle.append(tmp)


index = 0
sum_list = []
def find(height,elements_triangle):
    global index
    global sum_list
    sum_list.append([elements_triangle[0][0]])
    if height == 1:
        return elements_triangle[0][0]
    for i in range(height):
        if i == 0:
            continue
        tmp = []
        for j in range(i+1):
            index = j
            if index == 0:
                tmp.append(sum_list[i-1][index] + elements_triangle[i][j])
            elif index == i:
                tmp.append(sum_list[i-1][index-1] + elements_triangle[i][j])
            else:
                tmp.append(min(sum_list[i-1][index-1], sum_list[i-1][index]) + elements_triangle[i][j])
        sum_list.append(tmp)
    last_row = sum_list[-1]
    flag = last_row[0]
    for i in range(last_row.__len__()):
        if last_row[i] < flag:
            flag = last_row[i]
    return flag

if __name__ == '__main__':
    print(find(height,elements_triangle))
