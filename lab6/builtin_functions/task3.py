def Is_palindrome(input_string):
    reversed_string = "".join(reversed(input_string))
    if reversed_string == input_string:
        print("This string is a palindrome")
    else:
        print("This string is not a palindrome")

my_input = input("enter a string: ")
Is_palindrome(my_input)