import datetime

print("""
🌟🔮 Welcome, stranger!! 🔮🌟

The stars have aligned just for you…  
Prepare to unveil the secrets written in the cosmos.  
Your birth date holds the key to your Zodiac destiny.  
Let us begin the journey of self-discovery…  
""")

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

while True:
    try:
        month = int(input("\nEnter your birth month (1-12): "))
        day = int(input("Enter your birth day (1-31): "))

        datetime.date(1990, month, day)
        break
    except ValueError:
        print("Oops! That's not a valid date. Please make sure the month and day are correct.")

user_zodiac = "Unknown"
for sign_info in zodiac_signs:
    if sign_info["start_month"] > sign_info["end_month"]:
        if (month == sign_info["start_month"] and day >= sign_info["start_day"]) or \
                (month == sign_info["end_month"] and day <= sign_info["end_day"]):
            user_zodiac = f"{sign_info['sign']} {sign_info['emoji']}"
            break
    else:
        if (month == sign_info["start_month"] and day >= sign_info["start_day"]) or \
                (month == sign_info["end_month"] and day <= sign_info["end_day"]):
            user_zodiac = f"{sign_info['sign']} {sign_info['emoji']}"
            break

if user_zodiac != "Unknown":
    print(f"\nYour Zodiac sign is: {user_zodiac}")
else:
    print("\nI couldn't determine your sign. Please check your date and try again.")