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
    with open('input.txt') as inputFile:
        score = 0
        for line in inputFile:
            play1, play2 = line.split()

            if play1 == 'A': # player 1 played rock
                if play2 == 'Y': # player 2 played paper and won
                    score += 8
                elif play2 == 'X': # player 2 played rock and tied. 
                    score += 4
                else: # player 2 played scissors and lost
                    score += 3

            if play1 == 'B': # player 1 player paper
                if play2 == 'Z': # player 2 plays scissor and won.
                    score += 9
                if play2 == 'Y': # player 2 plays paper and tied.
                    score += 5
                else:
                    score += 1

            if play1 == 'C': # player 1 player scissor 
                if play2 == 'X':
                    score += 7
                if play2 == 'Z':
                    score += 6
                else:
                    score += 2

        print(score)





if __name__=="__main__":
    main()