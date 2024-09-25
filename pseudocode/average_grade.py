first_name = (input('what is your first name: \n'))
quiz_score1 = float(input('a random quiz score %: \n'))
quiz_score2 = float(input('a random quiz score %: \n'))
quiz_score3 = float(input('a random quiz score %: \n'))

average = (quiz_score1 + quiz_score2 + quiz_score3) /3
print(f'Hello, {first_name}, your average quiz score for the quizes is: {average:.2f}%')