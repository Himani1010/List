n=[2,6,7,191,9]
max=0
sec_max=0
i=0
while i<len(n):
    if n[i]>max:
        max=n[i]
    elif n[i]>sec_max and sec_max<max:
        sec_max=n[i]
    i=i+1
print(max)
print(sec_max)

