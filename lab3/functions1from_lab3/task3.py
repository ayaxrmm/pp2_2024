def solve(numheads, numlegs):
    num_chikens=0
    num_rabbits=0
    for num_chikens in range(numheads+1):
        num_rabbits=numheads-num_chikens
        totalleg = 2*num_chikens + 4*num_rabbits
        if totalleg == numlegs:
            return num_rabbits, num_chikens
    return None
res=solve(35,94)
if res:
    num_rabbits, num_chikens = res
    print("number of rabbits: ", num_rabbits)
    print("number of chikens: ", num_chikens)
else:
    print("No solution")
    