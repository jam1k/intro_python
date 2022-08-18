# Write your solution here
def read_input(string, minimum: int, maximum: int):
    while True:
        try:
            input_str = input(string)
            number  = int(input_str)
            if number > minimum and number < maximum:
                return number
        except ValueError:
            pass
        print (f"You must type in an integer between {minimum} and {maximum}")
