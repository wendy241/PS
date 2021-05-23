# a=input().split()
# # text=[]
# # for i in range(len(first)):
# #     text.append(int(first[i]))
# # text.sort()
# first=[]
# for i in range(len(a)):
#     first.append(int(a[i]))

# #1. first에 음수만 들어있을 경우 찾기 어려움
# mx=-1
# inx=-1
# for i in range(len(first)):
#     if mx<first[i]:
#         mx=first[i]
#         inx=i
# #2
# mx=max(first)
# inx=-1
# for i in range(len(first)):
#     if mx==first[i]:
#         inx=i
#         break
# print(mx)
# print(inx)
#
# ########################################################
# #1
# mx=-1
# inx=-1
# for i in range(len(first)):
#     if mx<=first[i]:
#         mx=first[i]
#         inx=i
#
# first[inx] = -1
#
# mx=-1
# inx=-1
# for i in range(len(first)):
#     if mx<=first[i]:
#         mx=first[i]
#         inx=i
# print(mx)
# print(inx)
#
# #2
# second = first.copy()
# second.sort()
# mx=second[-2]
# for i in range(len(first)):
#     if mx==first[i]:
#         inx=i
#         break
# print(mx)
# print(inx)
# lst=[0]*1010#counting sort. 꼭 알아두자, 최빈값 구할 떄도 쓰임
# a=0
# inx=0
# for i in range(10):
#     k=int(input())
#     lst[k]+=1
#     a+=k#얘는 그냥 평균값 구하기 위해 전체 값을 다 더하는 것.
# mx=max(lst)
# for i in range(len(lst)):
#     if lst[i]==mx:
#         inx=i
# avg=a//10
# print(avg)
# print(inx)

# #day 1 11번
# n=int(input())
# answer=input().split()
# score=0
# grade=0
# for i in answer:
#     if int(i)==1:
#        score+=1
#        grade+=score
#     else:
#         score=0
# print(grade)
#
# ##12번
#
# lst1=[]
# lst_max=[]
# lst_idx=[]
# mx=-1;idx=-1
#
# for k in range(9):
#     a = input().split()
#     for i in range(len(a)):
#         lst1.append(int(a[i]))
#     for i in range(len(lst1)):
#         if lst1[i]>=mx:
#             mx=lst1[i]
#             idx=i
#     lst_max.append(mx)
#     lst_idx.append(idx)
#     mx=-1;idx=-1
#     lst1=[]
#
# for j in range(len(lst_max)):
#     if lst_max[j]>=mx:
#         mx=lst_max[j]
#         idx=j
# print(mx)
# print(idx+1, lst_idx[idx]+1)

# ##13번
# A=int(input())
# oper=input()
# B=int(input())
# if oper=='+':
#     print(A+B)
# elif oper=='*':
#     print(A*B)

# ##14번
# lst1=[]
# lst2=[]
# a, b=0, 0
# for i in range(3):
#     a=input().split()
#     lst1.append(a[0])
#     lst2.append(a[-1])
# lst1.sort()
# lst2.sort()
# if lst1[0]==lst1[1]:
#     a=lst1[2]
# else:
#     a=lst1[0]
# if lst2[0]==lst2[1]:
#     b=lst2[2]
# else:
#     b=lst2[0]
# print(a, b)

# ##16번
# a=input().split()
# b, c='', ''
# for i in range(len(a)):
#     if i<2:
#         b+=a[i]
#     else:
#         c+=a[i]
# print(int(b)+int(c))

# ##17번
#
# n=int(input())
# a=1
# for i in range(1,n+1):
#    a*=i
# print(a)

# ##18번
# lst=[]
# n=-1
# b=0
# c=1
# while n!=0:
#     n=input()
#     if n=='0':
#         break
#     else:
#         lst.append(n)
# print(lst)
# for k in range(len(lst)):
#     a=lst[k]
#
#     for i in range(1, len(a)+1):
#         c*=i
#     b+=c*int(a[i-1])
#     print(b)

##DAY2
##1
# n=int(input())
# k=[]
# for i in range(n):
#     k.append(int(input()))
# k.sort()
# for l in range(n):
#     print(k[l])

# ##2
# num=0
# lst=[0]*1010
# idx=0
# for i in range(10):
#     k=int(input())
#     num+=k
#     lst[k]+=1
# for i in range(1010):
#     if max(lst)==lst[i]:
#         idx=i
# print(num//10)
# print(idx)

# ##3
# n=int(input())
# a=0
# k=[]
# b=[0]*500000
# mx=-1
# idx=-1
# for i in range(n):
#    z=int(input())
#    k.append(z)
#    a+=z
#    b[z]=z
# for i in range(500000):
#     if b[i]>mx:
#         mx=b[i]
#         idx=i
# print(a//n)
# print(k[(n-1)//2])
# print(idx)

# ##4
# n=[]
# length=[]
# k=0
# a=input()
# while a!='0':
#     n.append(a)
#     for i in range(len(a)):
#         if a[i]=='1':
#             k+=2
#
#         elif a[i]=='0':
#             k+=4
#
#         else:
#             k+=3
#
#     k+=2
#     k+=len(a)-1
#     length.append(k)
#     k=0
#     a=input()
#
# for i in range(len(length)):
#     print(length[i])

# ##5
# a=input().split()
# piece={}
# name=['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
# for i in range(len(a)):
#     a[i]=int(a[i])
# for i in range(len(a)):
#     piece[name[i]]=a[i]
# if piece['king']!=1:
#     piece['king']=1-a[0]
#
# if piece['queen']!=1:
#     piece['queen']=1-a[1]
#
# if piece['rook']!=2:
#     piece['rook']=2-a[2]
#
# if piece['bishop']!=2:
#     piece['bishop']=2-a[3]
#
# if piece['knight']!=2:
#     piece['knight']=2-a[4]
#
# if piece['pawn']!=8:
#     piece['pawn']=8-a[5]
# print(piece.values())

# ##5
# a=input().split()
# piece=[0]*6
# piece_2=[0]*6
# for i in range(len(a)):
#     piece[i]=int(a[i])
# if piece[0]!=1:
#     piece_2[0]=1-piece[0]
#
# if piece[1]!=1:
#     piece_2[1]=1-piece[1]
#
# if piece[2]!=2:
#     piece_2[2]=2-piece[2]
#
# if piece[3]!=2:
#     piece_2[3]=2-piece[3]
#
# if piece[4]!=2:
#     piece_2[4]=2-piece[4]
#
# if piece[5]!=8:
#     piece_2[5]=8-piece[5]
#
# print(piece_2[::1])

# ##6
#
# n=int(input())
#
# while n>9:
#     n-=8
# if n==1 or n==9:
#     print(1)
# elif n==2 or n==8:
#     print(2)
# elif n==3 or n==7:
#     print(3)
# elif n==4 or n==6:
#     print(4)
# else:
#     print(5)

# ##7
# result=[]
# for i in range(3):
#     a=input().split()
#     if a.count('1')==3:
#         result.append("A")
#     elif a.count('1')==2:
#         result.append("B")
#     elif a.count('1')==1:
#         result.append("C")
#     elif a.count('1')==0:
#         result.append("D")
#     elif a.count('1')==4:
#         result.append("E")
# for i in range(3):
#     print(result[i])

# ##8
# a=input()
# k=0
# alphabet=['a', 'e', 'i', 'o', 'u', "A", 'E', "I", "O", "U"]
# count_lst=[]
# while a!='#':
#     for i in range(len(alphabet)):
#         k+=a.count(alphabet[i])
#     count_lst.append(k)
#     k=0
#     a=input()
# for i in range(len(count_lst)):
#     print(count_lst[i])

##9

# ##10
# n=int(input())#n이 test case 개수
#
# for i in range(n):
#     c=input().split()
#     t=input().split()
# for i in range(n):
#     c[i]=int(c[i])
#     t[i]=int(t[i])
#
# c[0]

# ##11
# letter=input()
# word=['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
#
# for i in range(len(letter)):
#     for k in range(len(word)):
#         if letter[i]==word[k]:
#             letter=letter.replace(letter[i], "_")
# letter=letter.replace("_", '')
# print(letter)

# ##12
# T=int(input())
# Result=[]
# for i in range(T):
#     g, s = 0, 0
#     G_lst, S_lst = [], []
#     G=input().split()
#     S=input().split()
#     for i in range(len(G)):
#         G_lst.append(int(G[i]))
#     for i in range(len(S)):
#         S_lst.append(int(S[i]))
#     for k in range(len(S_lst)):
#         if k==0:
#             g+=1*G_lst[k];s+=1*S_lst[k]
#         elif k==1:
#             g+=2*G_lst[k];s+=2*S_lst[k]
#         elif k==2:
#             g+=3*G_lst[k];s+=2*S_lst[k]
#         elif k==3:
#             g+=3*G_lst[k];s+=2*S_lst[k]
#         elif k==4:
#             g+=4*G_lst[k];s+=3*S_lst[k]
#         elif k==5:
#             g+=10*G_lst[k];s+=5*S_lst[k]
#         elif k==6:
#             s+=10*S_lst[k]
#     if g>s:
#         Result.append('G_WIN')
#     elif g<s:
#         Result.append('S_WIN')
#     else:
#         Result.append(('DRAW'))
# for i in range(T):
#     if Result[i]=='G_WIN':
#         print("Battle %d: %s"%(i+1,"Good triumphs over Evil"))
#     elif Result[i]=='S_WIN':
#         print("Battle %d: %s"%(i+1,"Evil eradicates all trace of Good"))
#     else:
#         print("Battle %d: %s"%(i+1, "No victor on this battle field"))

# ##13
# n=input()
# n_1=[]
# result_lst=[]
# while n!='#':
#     a=0
#     for i in range(len(n)):
#         if n[i]=='-':
#             n_1.append(0)
#         if n[i]=='\\':
#             n_1.append(1)
#         if n[i]=='(':
#             n_1.append(2)
#         if n[i]=='@':
#             n_1.append(3)
#         if n[i]=='?':
#             n_1.append(4)
#         if n[i]=='>':
#             n_1.append(5)
#         if n[i]=='&':
#             n_1.append(6)
#         if n[i]=='%':
#             n_1.append(7)
#         if n[i]=='/':
#             n_1.append(-1)
#     for i in range(len(n_1)):
#         for k in range(n_1[i]):
#             a+=n_1[-i]*8**i
#         result_lst.append(a)













