print("================================================")
print("=      WELCOME BABY CHILD HEALTH SYSTEM        =")
print("================================================")

# Dictionary Format: {"Age_Key": [Normal_Weight_KG, Normal_Height_CM]}
# Data covers 0.1 (1 month) to 0.12 (12 months) and 1.0 to 6.0 (Years)
male_db = {
    "0.0": [3.3, 49.9], "0.1": [4.5, 54.7], "0.2": [5.6, 58.4], "0.3": [6.4, 61.4],
    "0.4": [7.0, 63.9], "0.5": [7.5, 65.9], "0.6": [7.9, 67.6], "0.7": [8.3, 69.2],
    "0.8": [8.6, 70.6], "0.9": [8.9, 72.0], "0.10": [9.2, 73.3], "0.11": [9.4, 74.5],
    "0.12": [9.6, 75.7], "1.0": [9.6, 75.7], "2.0": [12.2, 87.8], "3.0": [14.3, 96.1],
    "4.0": [16.3, 103.3], "5.0": [18.3, 110.0], "6.0": [20.5, 116.0]
}

female_db = {
    "0.0": [3.2, 49.1], "0.1": [4.2, 53.7], "0.2": [5.1, 57.1], "0.3": [5.8, 59.8],
    "0.4": [6.4, 62.1], "0.5": [6.9, 64.0], "0.6": [7.3, 65.7], "0.7": [7.6, 67.3],
    "0.8": [7.9, 68.7], "0.9": [8.2, 70.1], "0.10": [8.5, 71.5], "0.11": [8.7, 72.8],
    "0.12": [8.9, 74.0], "1.0": [8.9, 74.0], "2.0": [11.5, 86.4], "3.0": [13.9, 95.1],
    "4.0": [16.1, 102.7], "5.0": [18.2, 109.4], "6.0": [20.2, 115.1]
}

while True:
    print("\n" + "="*40)
    print("      2026 CHILD HEALTH TRACKER      ")
    print("="*40)
    
    gender = input("Enter Gender (m/f) or\n 'e' to Exit: ").lower()
    
    if gender == 'e':
        print("System shutting down. Goodbye!")
        break
    
    if gender in ['m', 'f']:
        # We take age as a string to match dictionary keys exactly
        age_key = input("Enter Age (e.g., 0.1 for 1 mo, 0.10 for 10 mo, 1.0 for 1 yr): ")
        
        # Select appropriate dictionary
        db = male_db if gender == 'm' else female_db
        gender_label = "MALE" if gender == 'm' else "FEMALE"

        if age_key in db:
            weight, height = db[age_key]
            print(f"\n✅ DATA FOUND FOR {gender_label}")
            print(f"--------------------------------")
            print(f"Age           : {age_key}")
            print(f"Normal Weight : {weight} kg")
            print(f"Normal Height : {height} cm")
            print(f"--------------------------------")
        else:
            print(f"❌ Error: Data not found for Age '{age_key}'.")
            print("Please use formats like: 0.1, 0.10, 1.0, 2.0 up to 6.0")
    else:
        print("❌ Invalid Input! Please enter 'm' for Male or 'f' for Female.")

