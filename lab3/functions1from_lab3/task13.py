import random
def guess():
    secret_number=random.randint(1,20)
    print("Hello! What is your name?")
    name=input("enter your name: ")
    print("Well, "+name+", I am thinking of a number between 1 and 20.")
    sum=0
    while True:
        print("Take a guess.")
        guess=int(input())
        sum+=1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print("Good job, " + name+ "!You guessed my number in " +str(sum)+ " guesses!")
            break
guess()