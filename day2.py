text_file = 'rps.txt'
skra = open(text_file, 'r').readlines()
playerPoints = 0
# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
for line in skra:
    x = line.split()
    if x[1] == 'X' and x[0] == 'A':
        playerPoints += 3
    if x[1] == 'X' and x[0] == 'B':
        playerPoints += 1
    if x[1] == 'X' and x[0] == 'C':
        playerPoints += 2
    if x[1] == 'Y' and x[0] == 'A':
        playerPoints += 4
    if x[1] == 'Y' and x[0] == 'B':
        playerPoints += 5
    if x[1] == 'Y' and x[0] == 'C':
        playerPoints += 6
    if x[1] == 'Z' and x[0] == 'A':
        playerPoints += 8
    if x[1] == 'Z' and x[0] == 'B':
        playerPoints += 9
    if x[1] == 'Z' and x[0] == 'C':
        playerPoints += 7
        
    
print(playerPoints)
