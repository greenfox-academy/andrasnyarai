# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8
n = 23

m = input("Guess a number: ")
m = int(m)

if m < n:
    print("The stored number is higher")
elif m > n:
    print("The stored number is lower")
elif m == n:
    print("You found the number: " + str(n))