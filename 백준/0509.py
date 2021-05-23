# num1=input().split()
# num2=input().split()
# num3=input().split()
# num4=[]
# if num1[0]==num2[0]:
#     num4.append(num3[0])
#     if num1[1]==num3[1]:
#         num4.append(num2[1])
#     elif num1[1]!=num3[1]:
#         num4.append(num1[1])
# elif num1[0]==num3[0]:
#
# elif num1[0]!=num2[0] and num1[0]!=num3[0]:

# a=int(input(""))
#
# for i in range(1, a+1):
#     print(" "*(a-i)+"*"*(2*i-1))
#
# a, b, c, d=map(int, input().split())
# num1=str(a)+str(b)
# num2=str(c)+str(d)
# print(int(num1)+int(num2))


# people=int(input())
# num=[]
# for _ in range(people):
#     k=input().split()
#     k[0], k[1], k[2]=int(k[0]), int(k[1]), int(k[2])
#     k.sort()
#     if k[0]==k[2]:
#         num.append(10000+1000*k[1])
#     elif k[0]==k[1] or k[1]==k[2]:
#         num.append(1000+100*k[1])
#     else:
#         num.append(100*k[2])
# print(max(num))


# n=int(input())
#
# for i in range(1, n-1):
#     print(" "*(i-1)+"*"*(2*n-2*i-1))
# for i in range(1, n):
#     print(" "*(n-i-1)+"*"*(2*i-1))

# n=int(input())
# num=[]
# for i in range(n):
#     k=input().split()
#     k[0], k[1], k[2]=int(k[0]), int(k[1]), int(k[2])
#     k.sort()
#     if k[0]==k[2]:
#         num.append(10000+1000*k[0])
#     elif k[0]==k[1] or k[1]==k[2]:
#         num.append(1000+100*k[1])
#     else:
#         num.append(100*k[2])
# print(max(num))
# ##11번 질문
# n=int(input())
# a=input().split
# s=0
# for i in range(n):
#     if a[i]=="1":
#         if a[i-1]=="1":
#             s+=2
#         elif a[i-1]=="0":
#             s+=1
#     elif a[i]=="0":
#         s+=0

