a = int(input())
b = input()
b_hat = 0
location = int((b.__len__()-1) / 2)
for i in range(location):
    b_hat += int(b[(i+1)*2-1]) * 10**(location-i-1)
print(pow(a,b_hat,1337))

# def main(a,b):
#     b_hat = 0
#     location = len(b)
#     for i in range(location):
#         b_hat += int(b[i]) * 10**(location-i-1)
#     return pow(a,b_hat,1337)
# print(main(4,[3,5]))

# def main(a,b):
#     b_hat = 0
#     length = b.__len__()
#     for i in range(length):
#         b_hat += int(b[i]) * 10**(length-i-1)
#     return pow(int(a),b_hat,1337)
# print(main(4,[3,5]))