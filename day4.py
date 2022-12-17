text_file = 'day4.txt'
skra = open(text_file, 'r').readlines()
result = [item.split(',') for item in skra]
length = len(result)
i, n, sum, sum2 = 0, 0, 0, 0
while i<length:
    for number in result[i]:
        numsplit = [item.split('-') for item in result[i]]
        numsplit1, numsplit2, numsplit3, numsplit4 = int(numsplit[0][0]), int(numsplit[0][1]), int(numsplit[1][0]), int(numsplit[1][1])
    if numsplit1 >= numsplit3 and numsplit2 <= numsplit4 or numsplit3>= numsplit1 and numsplit4 <= numsplit2:
        sum += 1
        sum2 += 1
    elif numsplit3<=numsplit2 and numsplit3>=numsplit1 or numsplit1<=numsplit4 and numsplit1>=numsplit3:
        sum2 += 1
    i+=1
print(sum)
print(sum2)