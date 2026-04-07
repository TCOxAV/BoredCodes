import datetime
import random
import sys

# Rage-bait responses
roasts = [
    "Seriously? 🤡", "Bruh... 💀", "You good? 🧠", "Try again, champ 🏆",
    "That's embarrassing 📉", "Read the screen? 👓", "Are you trolling me? 🎣",
    "My grandma dates better 👵", "Skill issue ngl 🔥","You did that on purpose? 🙄", "Oof size: LARGE 📦", "Brain.exe stopped 🖥️",
    "Tell me you failed kindergarten without telling me 🍼", "Even a rock knows months 📅"
]

zodiac_roasts = {
    "Capricorn": "Workaholic who forgot how to have fun. When's the last time you relaxed? 💼",
    "Aquarius": "You think you're unique. Everyone thinks you're weird. 🤖",
    "Pisces": "Cries during commercials. Gets offended by everything. 😭",
    "Aries": "Impulsive temper tantrum in human form. Count to 10 maybe? 🔥",
    "Taurus": "Stubborn as a rock. Good luck changing your mind (impossible). 🪨",
    "Gemini": "Two-faced? More like 10 personalities. Pick a struggle. 🎭",
    "Cancer": "Crabby, moody, and lives in the past. Get over it already. 🦀",
    "Leo": "Main character syndrome. The world doesn't revolve around you. 🦁",
    "Virgo": "Control freak who alphabetizes their spice rack. Relax. 📋",
    "Libra": "Can't decide what to eat for 3 hours. Indecisive much? ⚖️",
    "Scorpio": "Intense stare that screams 'I'm plotting something'. Creepy. 🦂",
    "Sagittarius": "Commitment issues wrapped in a 'free spirit' bow. Run away much? 🏹"
}

def rage_bait():
    return random.choice(roasts)

def get_zodiac(month, day):
    zodiac_signs = [
        {"sign": "Capricorn", "emoji": "♑", "start_month": 12, "start_day": 22, "end_month": 1, "end_day": 19},
        {"sign": "Aquarius", "emoji": "♒", "start_month": 1, "start_day": 20, "end_month": 2, "end_day": 18},
        {"sign": "Pisces", "emoji": "♓", "start_month": 2, "start_day": 19, "end_month": 3, "end_day": 20},
        {"sign": "Aries", "emoji": "♈", "start_month": 3, "start_day": 21, "end_month": 4, "end_day": 19},
        {"sign": "Taurus", "emoji": "♉", "start_month": 4, "start_day": 20, "end_month": 5, "end_day": 20},
        {"sign": "Gemini", "emoji": "♊", "start_month": 5, "start_day": 21, "end_month": 6, "end_day": 21},
        {"sign": "Cancer", "emoji": "♋", "start_month": 6, "start_day": 22, "end_month": 7, "end_day": 22},
        {"sign": "Leo", "emoji": "♌", "start_month": 7, "start_day": 23, "end_month": 8, "end_day": 22},
        {"sign": "Virgo", "emoji": "♍", "start_month": 8, "start_day": 23, "end_month": 9, "end_day": 22},
        {"sign": "Libra", "emoji": "♎", "start_month": 9, "start_day": 23, "end_month": 10, "end_day": 23},
        {"sign": "Scorpio", "emoji": "♏", "start_month": 10, "start_day": 24, "end_month": 11, "end_day": 21},
        {"sign": "Sagittarius", "emoji": "♐", "start_month": 11, "start_day": 22, "end_month": 12, "end_day": 21},
    ]
    
    for sign_info in zodiac_signs:
        if sign_info["start_month"] > sign_info["end_month"]:
            if (month == sign_info["start_month"] and day >= sign_info["start_day"]) or \
                    (month == sign_info["end_month"] and day <= sign_info["end_day"]):
                return sign_info
        else:
            if (month == sign_info["start_month"] and day >= sign_info["start_day"]) or \
                    (month == sign_info["end_month"] and day <= sign_info["end_day"]):
                return sign_info
    return None

def get_valid_date():
    wrong_count = 0
    while True:
        try:
            month_input = input("\n📅 Birth month (1-12): ").strip()
            if not month_input.isdigit():
                wrong_count += 1
                if wrong_count >= 2:
                    print(f"{rage_bait()} Months are NUMBERS 1-12. Not '{month_input}'. Are you OK?")
                else:
                    print(f"{rage_bait()} That's not a number. Try again.")
                continue
                
            month = int(month_input)
            
            if month < 1 or month > 12:
                wrong_count += 1
                if wrong_count >= 2:
                    print(f"{rage_bait()} Months go from 1 to 12. {month}? Really? 🤦")
                else:
                    print(f"{rage_bait()} {month} is not a month. 1-12 please.")
                continue
                
            day_input = input("📅 Birth day (1-31): ").strip()
            if not day_input.isdigit():
                wrong_count += 1
                if wrong_count >= 2:
                    print(f"{rage_bait()} Days are NUMBERS. '{day_input}'? My disappointment is immeasurable.")
                else:
                    print(f"{rage_bait()} That's not a number. Focus.")
                continue
                
            day = int(day_input)
            
            if day < 1 or day > 31:
                wrong_count += 1
                if wrong_count >= 2:
                    print(f"{rage_bait()} Days are 1-31. {day}? You're killing me smalls.")
                else:
                    print(f"{rage_bait()} {day} is invalid. Try 1-31.")
                continue

            # Check if date exists
            datetime.date(1990, month, day)
            return month, day, wrong_count
            
        except ValueError:
            wrong_count += 1
            if wrong_count >= 3:
                print(f"{rage_bait()} That date doesn't exist. February 30th? April 31st? Use your brain.")
            elif wrong_count >= 2:
                print(f"{rage_bait()} Invalid date. Check your calendar, genius.")
            else:
                print(f"{rage_bait()} That's not a real date. Try again.")

# Main program loop
running = True
while running:
    print("""
🌟🔮 WELCOME, MORTAL! 🔮🌟

The stars have aligned just for you...  
Or have they? Don't mess this up.  
Enter your birth date.  
TRY not to embarrass yourself.
""")
    
    month, day, wrong_count = get_valid_date()
    user_zodiac = get_zodiac(month, day)
    
    if user_zodiac:
        sign_name = user_zodiac['sign']
        emoji = user_zodiac['emoji']
        roast = zodiac_roasts.get(sign_name, "You exist. Congrats?")
        
        print(f"\n✨✨✨ YOUR ZODIAC IS: {sign_name} {emoji} ✨✨✨")
        print("\n" + "="*50)
        print(f"🔮 THE STARS SAY: {roast}")
        print("="*50)
        
        # Extra rage based on wrong attempts
        if wrong_count >= 3:
            print(f"\n⚠️ Also, it took you {wrong_count} tries to enter a date. Impressive... in a bad way.")
        elif wrong_count >= 1:
            print(f"\n⚠️ {wrong_count} mistake(s) just to enter a birthday. Yikes.")
        else:
            print("\n✅ Wow. No mistakes. I'm genuinely shocked.")
    else:
        print(f"\n❌ {rage_bait()} Couldn't find your sign. You're from another planet?")
    
    # Play again loop
    while True:
        again = input("\n🎰 Find another sign? (y/n): ").strip().lower()
        if again in ['y', 'yes']:
            break  # Break inner loop, continue outer loop
        elif again in ['n', 'no']:
            print(f"\n💀 Leaving already? {rage_bait()} The stars will forget you in 5 minutes. Bye.")
            running = False  # Set flag to exit outer loop
            break  # Break inner loop
        else:
            print(f"{rage_bait()} That's not y or n. How do you function?")
    
    print()  # Add blank line for spacing between runs

# Natural program exit - no termination warning
print("\n👋 Program ended. Thanks for playing (and surviving the roasts)!")
