# age = 10
# if age > 18:
#     print('This person is an adult')
# else:
#     print('This person is a minor')

# score = float(input('Input your score: '))
#
# if score >= 40:
#     print('You passed')
# else:
#     print('You failed')

# num = int(input('Input your number: '))
# if num%2 == 0:
#     print('This number is even')
# else:
#     print('This number is odd')

#Ceate a program that will take a student's score and grade them
#Based on the above grading system

score = float(input('What is your score?: '))
if score < 40:
    print('Your grade is F. FAILED, You must rewrite the test!')
elif score <= 50:
    print('Your grade is E. You nearly failed, sit up!')
elif score <= 60:
    print('Your grade is D. Pass, but you can do better.')
elif score <= 70:
    print('Your grade is C. Good, but make sure to improve.')
elif score <= 80:
    print('Your grade is B. Very Good! Keep it up.')
elif score <= 90:
    print('Your grade is A. Excellent!')
else:
    print('Your grade is A+. Mastered!')
