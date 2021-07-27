# n=[2,6,18,50,7]
# i=0
# max=0
# while i<len(n):
#     if n[i]>max:
#         max=n[i]
#     i=i+1
# print(max)


name=['m','o','m']
i=-1
j=[]
while i>=-len(name):
    j=j+[name[i]]
    i=i+1
if j==name:
    print('palindrome')
else:
    print('not palindrome')