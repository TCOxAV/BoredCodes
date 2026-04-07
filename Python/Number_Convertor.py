# Coded functions - integerized
def dec_to_bin(num):
    if num == 0:
        return "0"
    elif num != int(num):
        return "No floats!"
    elif num < 0:
        return "No negatives!"
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
        return "No floats!"
    elif num < 0:
        return "No negatives!"
    oct_str = ""
    num2 = num
    while num2 > 0:
        rem = num2 % 8
        oct_str = str(rem) + oct_str
        num2 = num2 // 8
    return oct_str

def bin_to_dec(num):
    if isinstance(num, (float, int)) and num < 0:
        return "No negatives!"
    num1 = str(num)
    if any(c not in '01' for c in num1):
        return "Invalid binary! Use 0/1 only."
    dec_val = 0
    num1 = num1[::-1]
    for i in range(len(num1)):
        if num1[i] == "1":
            dec_val += (2 ** i)
    return dec_val

def oct_to_dec(num):
    str_num = str(num)
    if any(c not in '01234567' for c in str_num):
        return "Invalid octal! Use 0-7."
    dec_val = 0
    str_num = str_num[::-1]
    for i in range(len(str_num)):
        oct_val = int(str_num[i]) * (8 ** i)
        dec_val += oct_val
    return dec_val

def hex_to_dec(num_str):
    num_str = str(num_str).upper()
    if any(c not in '0123456789ABCDEF' for c in num_str):
        return "Invalid hex! Use 0-9,A-F."
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
        return "No floats!"
    elif num < 0:
        return "No negatives!"
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

import random

# Rage-bait responses
roasts = [
    "Seriously? 🤡", "Bruh... 💀", "You good? 🧠", "Try again, champ 🏆",
    "That's embarrassing 📉", "Read the screen? 👓", "Are you trolling me? 🎣",
    "My grandma codes better 👵", "Skill issue ngl 🔥", "Rage bait successful 😈",
    "You did that on purpose? 🙄", "Oof size: LARGE 📦", "Brain.exe stopped 🖥️"
]

smart_roasts = [
    "Wow. Just wow. 🤦", "Did you skip kindergarten? 🍼", "Tell me you're new without telling me 📢",
    "Even a rock would get this right 🪨", "Let me dumb it down for you... 📉",
    "I'm losing braincells rn 🧠💨", "You're why error handling exists 💀",
    "This is why we can't have nice things 🔥"
]

def rage_bait():
    return random.choice(roasts + smart_roasts)

# User-driven system
def get_base_choice(prompt, valid_options):
    wrong_count = 0
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        else:
            wrong_count += 1
            if wrong_count >= 2:
                print(f"{rage_bait()} That's not {valid_options}. C'mon man.")
            else:
                print(f"Nope. {rage_bait()} Pick {valid_options}.")


def get_number_input(base_name):
    wrong_count = 0
    while True:
        user_input = input(f"Enter {base_name} number: ").strip().upper()
        if base_name == "binary":
            if all(c in '01' for c in user_input):
                return int(user_input)
            else:
                wrong_count += 1
                if wrong_count >= 2:
                    print(f"{rage_bait()} Binary is 0s and 1s. Not {user_input}. How hard is that?")
                else:
                    print(f"Uh oh. {rage_bait()} Use only 0s & 1s.")
        elif base_name == "octal":
            if all(c in '01234567' for c in user_input):
                return int(user_input)
            else:
                wrong_count += 1
                if wrong_count >= 2:
                    print(f"{rage_bait()} OCTAL = digits 0-7. '{user_input}'?? You OK?")
                else:
                    print(f"Yikes. {rage_bait()} Use 0-7 only.")
        elif base_name == "decimal":
            if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
                return int(user_input)
            else:
                wrong_count += 1
                if wrong_count >= 2:
                    print(f"{rage_bait()} Decimal is just numbers. '{user_input}' ain't it.")
                else:
                    print(f"Lmao. {rage_bait()} Numbers only.")
        elif base_name == "hexadecimal":
            if all(c in '0123456789ABCDEF' for c in user_input):
                return user_input
            else:
                wrong_count += 1
                if wrong_count >= 2:
                    print(f"{rage_bait()} Hex is 0-9 and A-F. '{user_input}'? Nice try.")
                else:
                    print(f"Bro... {rage_bait()} Use 0-9 & A-F.")


# Main program loop
print("✨ Base Converter (Don't mess up) ✨")
print("⚠️ Warning: Wrong answers = public embarrassment ⚠️")

while True:
    print("\n--- Pick a base (carefully) ---")
    print("1: Bin  2: Oct  3: Dec  4: Hex")
    from_base_choice = get_base_choice("Choice (1-4): ", ['1', '2', '3', '4'])

    print("\n--- Convert to ---")
    print("1: Bin  2: Oct  3: Dec  4: Hex")
    to_base_choice = get_base_choice("Choice (1-4): ", ['1', '2', '3', '4'])

    bases = {'1': 'binary', '2': 'octal', '3': 'decimal', '4': 'hexadecimal'}
    from_base_name = bases[from_base_choice]
    to_base_name = bases[to_base_choice]

    if from_base_choice == to_base_choice:
        print(f"{rage_bait()} Same base? Really? Go touch grass. 🌿")
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

    # Check if result is an error message
    if isinstance(result, str) and result.startswith(("Invalid", "No", "Use")):
        print(f"\n❌ {result} {rage_bait()}")
    else:
        print(f"\n✅ Result: {result} (Don't act surprised you got it right)")

    play_again = input("\nAgain? (y/n): ").strip().lower()
    if play_again not in ['y', 'yes']:
        print(f"Finally leaving? {rage_bait()} Bye.")
        break
