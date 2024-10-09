## Problem 1 ##
#Fix the following code so that its output matches
# Sample output:
# --------------------------------------------------
# my name is Tim Tester, I am 20 years old
# 
# my skills are
#  - python (beginner)
#  - java (veteran)
#  - programming (semiprofessional)
#  
# I am looking for a job with a salary of 2000-3000 dollars per month

name = input("Please enter your name: ")
age = input("Please enter your age: ")
skill1 = input("Please name one of your skills: ")
level1 = input("Please choose how talented you are at this skill (beginner, semiprofessional, expert, veteran): ")
skill2 = input("PLease name another one of your skills: ")
level2 = input("Please choose how talented you are at this skill (beginner, semiprofessional, expert, veteran): ")
skill3 = input("PLease name a third skill of yours: ")
level3 = input("Please choose how talented you are at this skill (beginner, semiprofessional, expert, veteran): ")
lower = input("Name your minimum salary for a job: ")
upper = input("Name your maximum salary for a job: ")

print("\nmy name is " + name + ", I am " + age + " years old\n")
print("my skills are")
print(" - " + skill1 + " (" + level1 + ")")
print(" - " + skill2 + " ("+ level2 + ")")
print(" - " + skill3 + " (" + level3 + ")\n")
print("I am looking for a job with a salary of " + lower + "-" + upper + " dollars per month")





## Problem 2 ##
#Please finish the script so that: 
# - the following output is printed:
# Sample output:
# --------------------------------------------------
# X val: 27
# Y val: 15
#
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8
#
# - The program should work correctly even if the values of the variables are changed.

x = input("X val: ")
y = input("Y val: ")

print(x, "+", y, str("="), int(x) + int(y))
print(x, "-", y, str("="), int(x) - int(y))
print(x, "*", y, str("="), int(x) * int(y))
print(x, "/", y, str("="), int(x) / int(y))
