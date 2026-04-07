# --- Configuration Data ---
NORMAL_YEAR = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
LEAP_YEAR   = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
DAY_MAP = {0:"Saturday", 1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday"}

def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def normalize_date(d, m, y):
    """Mode 2: Cascades overflow values into next month/year."""
    while m > 12:
        m -= 12
        y += 1
    while True:
        limit = (LEAP_YEAR if is_leap(y) else NORMAL_YEAR)[m]
        if d <= limit: break
        d -= limit
        m += 1
        if m > 12:
            m, y = 1, y + 1
    return d, m, y

def validate_date(d, m, y):
    """Mode 1: Strict validation. Returns True if valid, False otherwise."""
    if m < 1 or m > 12 or y < 1:
        return False
    limit = (LEAP_YEAR if is_leap(y) else NORMAL_YEAR)[m]
    return 1 <= d <= limit

def formula(d, m, y):
    """Zeller's Congruence."""
    if m < 3:
        m += 12
        y -= 1
    K, J = y % 100, y // 100
    h = (d + (13 * (m + 1) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7
    return h

def main():
    mode = None
    running = True  # Step 1: Create a flag
    
    while running:  # Step 2: Use the flag for the main loop
        if mode is None:
            print("\n--- 📅 ZELLER'S DAY FINDER ---")
            print("1. Normal Mode | 2. Rollover Mode | 3. Exit")
            choice = input("Select Mode: ")
            if choice == '3': 
                running = False
                continue
            if choice in ['1', '2']:
                mode = int(choice)
            else:
                print("Invalid choice!")
                continue

        # Step 2: Get Input
        try:
            print(f"\n[Mode {mode} Active]")
            d = int(input("Enter Day: "))
            m = int(input("Enter Month: "))
            y = int(input("Enter Year: "))
        except ValueError:
            print("Please enter numeric values only.")
            continue

        # Step 3: Process based on Mode
        if mode == 1:
            if validate_date(d, m, y):
                res = formula(d, m, y)
                print(f"✅ {d}/{m}/{y} is a {DAY_MAP[res]}")
            else:
                print(f"❌ Error: {d}/{m}/{y} is an invalid date for Normal Mode.")
        else:
            nd, nm, ny = normalize_date(d, m, y)
            res = formula(nd, nm, ny)
            print(f"🔄 Normalized to: {nd:02d}/{nm:02d}/{ny}")
            print(f"✅ The day is: {DAY_MAP[res]}")
        
        # --- Fixed Post-Action Menu ---
        while True:
            print("\n--- Options ---")
            print("C: Continue | S: Switch Mode | E: Exit")
            next_step = input("Choice: ").upper()
            
            if next_step == 'C':
                break 
            elif next_step == 'S':
                mode = None
                break
            elif next_step == 'E':
                running = False # Step 3: Set flag to False
                break           # Breaks the mini-menu loop
            else:
                print("❌ Invalid Choice! Please enter C, S, or E.")

    print("Program closed.") # This will now print before the script ends

if __name__ == "__main__":
    main()
