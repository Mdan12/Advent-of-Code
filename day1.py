
elf, maxElf1, maxElf2, maxElf3 = 0, 0, 0, 0
text_file = 'day1.txt'
skra = open(text_file, 'r').readlines()
for line in skra:
  if line == "\n":
    if maxElf1 <= elf:
      maxElf3 = maxElf2
      maxElf2 = maxElf1
      maxElf1 = elf
      elf = 0
    elif maxElf2 <= elf:
      maxElf3 = maxElf2
      maxElf2 = elf
      elf = 0
    elif maxElf3 <= elf:
      maxElf3 = elf
      elf = 0
    else:
      elf = 0
  else: 
    elf += int(line)
sumElf = maxElf1 + maxElf2 + maxElf3
print(maxElf1)
print(sumElf)