# 에러 존재
# li = [3,30,34,9,100,200,1000]
# 정렬
# 십의 단위로 indexing
# def solution(li):
#     one = []
#     dec = []
#     hund = []
#     thou = []
#     li.sort()
#     for idx, i in enumerate(li):
#         if (i) < 10:
#             one.append(str(i))
#         elif (10<=i)and(i<100):
#             dec.append(str(i))
#         elif (100<=i) and (i<1000):
#             hund.append(str(i))
#         else:
#             thou.append(str(i))
#     return ('').join(one[::-1]) + ('').join(dec[::-1])+ ('').join(hund[::-1])+('').join(thou[::-1])

li = [3, 30, 34, 5, 9,1000]
# # 지린다
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))
# print(solution(li))
# li = [0,0,0,0,0]
def solution(li):
    list1 = list(map(str, li))
    list1.sort(key=lambda x:x*3 ,reverse = True)
    return int(''.join(list1))
print(solution(li))