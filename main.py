import random

number_choice = input("Input 7 lottery numbers between 1 and 100")  # chosen integers by user
lottery_ticket_string = number_choice.split(", ")  # turn string into list
if len(lottery_ticket_string) != 7:         # if statement to make sure user enters 7 integers
    print("You did not input 7 integers!")
    exit(0)
print(type(lottery_ticket_string))  # print out type to make sure string is converted to list
lottery_ticket = [int(i) for i in lottery_ticket_string]
# specify a range and give how many random numbers are needed to generate. generate a rand
random_nums = random.sample(range(1, 101), 7)  # sample() method in random module to generate a list of 7 random numbers
print(lottery_ticket)
print(random_nums)
matches = set(lottery_ticket_string).intersection(random_nums)  # set.intersection matches the elements that are similar
print("The matching numbers are", matches)  # prints the matching elements but returns set() when it's 0


def matchingNumber():
    countMatches = sum(i in random_nums for i in lottery_ticket)
    print(countMatches)
    if 1 < countMatches < 3:
        print("You have won £5")
    elif countMatches == 3:
        print("you have won £20")
    elif countMatches == 4:
        print("you have won £40")
    elif countMatches == 5:
        print("you have won £100")
    elif countMatches == 6:
        print("you have won £10,000")
    elif countMatches == 7:
        print("you have won £1000000")
    else:
        print("You have won nothing!")


matchingNumber()
