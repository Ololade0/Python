# def minimum(list):
#     for i in list:
#         return min(list)
# list = [10,20,30,40,50]
# print(minimum(list))
def count(list):
   count = 0

# list = ["abc", "xyz", "aba", "1221", "aba"]
   for x in list:
    if len(list) > 1 and list[0] == [-1]:
        count+= 1
    return count
print(count([list]))
