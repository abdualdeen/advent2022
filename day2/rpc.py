"""
-----------------
A - rock - X = 1
B - paper - Y = 2
C - scissor - Z = 3
-----------------
0 for lost round
3 for tied round
6 for won round
"""

def main():
    score = 0
    with open('/home/abdu/git/advent2022/day2/input2.txt') as inputFile:
        for line in inputFile:

            play1, play2 = line.split()
            
            if play1 == 'A': # player 1 played rock
                if play2 == 'Y': # player 2 played paper and won
                    score += (2 + 6)
                elif play2 == 'X': # player 2 played rock and tied. 
                    score += (1 + 3)
                else: # player 2 played scissors and lost
                    score += (3 + 0)

            if play1 == 'B': # player 1 player paper
                if play2 == 'Z': # player 2 plays scissor and won.
                    score += (3 + 6)
                elif play2 == 'Y': # player 2 plays paper and tied.
                    score += (2 + 3)
                else:
                    score += (1 + 0)

            if play1 == 'C': # player 1 player scissor 
                if play2 == 'X':
                    score += (1 + 6)
                elif play2 == 'Z':
                    score += (3 + 3)
                else:
                    score += (2 + 0)

    print(score)





if __name__=="__main__":
    main()