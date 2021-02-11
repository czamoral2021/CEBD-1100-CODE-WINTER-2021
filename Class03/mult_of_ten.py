# Multiple of Ten: Ask the user for a number,
# and then report whether the number is a multiple of 10 or not.

# Modify this assignment in order to do it in a loop.
# The loop should end once the user presses “q” or “Q”


# answer = ""
#
# while True:
#     answer = input("Enter a number>")
#     if answer  == "q" or answer == "Q":
#         # if answer[0:1].upper() == "Q"
#         break
#     if int(answer) % 10 == 0:
#         print(answer + " is a multiple of ten.")
#     else:
#         print(answer + " is not a multiple of ten.")

answer = ""
while answer != "q":
    answer = input("Enter a number (enter \"Q\" to stop)>")
    if answer  == "q" or answer == "Q":
        # if answer[0:1].upper() == "Q"
        break
    if int(answer) % 10 == 0:
        print(answer + " is a multiple of ten.")
    else:
        print(answer + " is not a multiple of ten.")
