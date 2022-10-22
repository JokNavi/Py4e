# Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
# < 0.6     F
def computegrade(score):
    if score <= 1 and score >= 0:
        if score <= 1 and score >= 0.9:
            return 'C'
        elif score < 0.9 and score >= 0.8:
            return 'B'
        elif score < 0.8 and score >= 0.7:
            return 'C'
        elif score < 0.7 and score >= 0.6:
            return 'D'
        elif score < 0.6:
            return 'F'
    else:
        return 'Bad score'  
try:
    score = float(input('Enter score: '))
    grade = computegrade(score)
    print(grade)
except:
    print('Bad score')