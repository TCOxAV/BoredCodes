# Coded functions - integerized
def dec_to_bin(num):
    if num == 0:
        return "0"
    elif num != int(num):
        return "Can't do float values!"
    elif num < 0:
        return "No negative integers!"
    bin_str = ""
    bin_num = num
    while bin_num > 0:
        rem = bin_num % 2
        bin_str = str(rem) + bin_str
        bin_num = bin_num // 2
    return bin_str

def dec_to_oct(num):
    if num == 0:
        return "0"
    elif num != int(num):
        return "Can't do float values!"
    elif num < 0:
        return "No negative integers!"
    oct_str = ""
    num2 = num
    while num2 > 0:
        rem = num2 % 8
        oct_str = str(rem) + oct_str
        num2 = num2 // 8
    return oct_str

def bin_to_dec(num):
    if isinstance(num, (float, int)) and num < 0:
        return "No negative integers!"
    num1 = str(num)
    if any(c not in '01' for c in num1):
        return "Invalid binary number! Please use only 0s and 1s."
    dec_val = 0
    num1 = num1[::-1]
    for i in range(len(num1)):
        if num1[i] == "1":
            dec_val += (2 ** i)
    return dec_val

def oct_to_dec(num):
    str_num = str(num)
    if any(c not in '01234567' for c in str_num):
        return "Invalid octal number! Please use digits 0-7."
    dec_val = 0
    str_num = str_num[::-1]
    for i in range(len(str_num)):
        oct_val = int(str_num[i]) * (8 ** i)
        dec_val += oct_val
    return dec_val

def hex_to_dec(num_str):
    num_str = str(num_str).upper()
    if any(c not in '0123456789ABCDEF' for c in num_str):
        return "Invalid hexadecimal number! Please use 0-9 and A-F."
    dec_val = 0
    num_str = num_str[::-1]
    for i in range(len(num_str)):
        covt = 0
        if num_str[i] == "A":
            covt = 10
        elif num_str[i] == "B":
            covt = 11
        elif num_str[i] == "C":
            covt = 12
        elif num_str[i] == "D":
            covt = 13
        elif num_str[i] == "E":
            covt = 14
        elif num_str[i] == "F":
            covt = 15
        else:
            covt = int(num_str[i])
        covt2 = covt * (16 ** i)
        dec_val += covt2
    return dec_val

# Coded functions - string_base
def dec_to_hex(num):
    if num == 0:
        return "0"
    elif num != int(num):
        return "Can't do float values!"
    elif num < 0:
        return "No negative integers!"
    hex_str = ""
    num2 = num
    while num2 > 0:
        rem = num2 % 16
        if rem == 10:
            hex_str += "A"
        elif rem == 11:
            hex_str += "B"
        elif rem == 12:
            hex_str += "C"
        elif rem == 13:
            hex_str += "D"
        elif rem == 14:
            hex_str += "E"
        elif rem == 15:
            hex_str += "F"
        else:
            hex_str += str(rem)
        num2 = num2 // 16
    return hex_str[::-1]

# Reused functions
def bin_to_hex(number):
    return dec_to_hex(bin_to_dec(number))

def bin_to_oct(number):
    return dec_to_oct(bin_to_dec(number))

def oct_to_hex(number):
    return dec_to_hex(oct_to_dec(number))

def oct_to_bin(number):
    return dec_to_bin(oct_to_dec(number))

def hex_to_oct(number):
    return dec_to_oct(hex_to_dec(number))

def hex_to_bin(number):
    return dec_to_bin(hex_to_dec(number))


# User-driven system
def get_base_choice(prompt, valid_options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        else:
            print("Oops! That's not a valid option. Please try again.")


def get_number_input(base_name):
    while True:
        user_input = input(f"Enter your {base_name} number: ").strip().upper()
        if base_name == "binary":
            if all(c in '01' for c in user_input):
                return int(user_input)
            else:
                print("That's not a valid binary number. Please use only 0s and 1s.")
        elif base_name == "octal":
            if all(c in '01234567' for c in user_input):
                return int(user_input)
            else:
                print("That's not a valid octal number. Please use digits from 0-7.")
        elif base_name == "decimal":
            if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
                return int(user_input)
            else:
                print("That's not a valid decimal number. Please use only digits.")
        elif base_name == "hexadecimal":
            if all(c in '0123456789ABCDEF' for c in user_input):
                return user_input
            else:
                print("That's not a valid hexadecimal number. Please use digits 0-9 and letters A-F.")


# Main program loop
print("✨ Welcome to the Number Base Converter! ✨")
print("I'm here to help you switch between different number systems.")

while True:
    print("\n--- Let's Get Started! ---")
    print("Which base do you want to start from?")
    print("1: Binary")
    print("2: Octal")
    print("3: Decimal")
    print("4: Hexadecimal")
    from_base_choice = get_base_choice("Enter your choice (1-4): ", ['1', '2', '3', '4'])

    print("\nAnd what base do you want to convert to?")
    print("1: Binary")
    print("2: Octal")
    print("3: Decimal")
    print("4: Hexadecimal")
    to_base_choice = get_base_choice("Enter your choice (1-4): ", ['1', '2', '3', '4'])

    bases = {'1': 'binary', '2': 'octal', '3': 'decimal', '4': 'hexadecimal'}
    from_base_name = bases[from_base_choice]
    to_base_name = bases[to_base_choice]

    if from_base_choice == to_base_choice:
        print("Heh, you can't convert a number to itself! Let's try again.")
        continue

    number = get_number_input(from_base_name)
    result = None

    if from_base_name == "binary":
        if to_base_name == "octal":
            result = bin_to_oct(number)
        elif to_base_name == "decimal":
            result = bin_to_dec(number)
        elif to_base_name == "hexadecimal":
            result = bin_to_hex(number)
    elif from_base_name == "octal":
        if to_base_name == "binary":
            result = oct_to_bin(number)
        elif to_base_name == "decimal":
            result = oct_to_dec(number)
        elif to_base_name == "hexadecimal":
            result = oct_to_hex(number)
    elif from_base_name == "decimal":
        if to_base_name == "binary":
            result = dec_to_bin(number)
        elif to_base_name == "octal":
            result = dec_to_oct(number)
        elif to_base_name == "hexadecimal":
            result = dec_to_hex(number)
    elif from_base_name == "hexadecimal":
        if to_base_name == "binary":
            result = hex_to_bin(number)
        elif to_base_name == "octal":
            result = hex_to_oct(number)
        elif to_base_name == "decimal":
            result = hex_to_dec(number)

    print(f"\n🚀 The result is: **{result}**!")

    play_again = input("\nWant to do another conversion? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for using the converter! See you next time! 👋")
        break
