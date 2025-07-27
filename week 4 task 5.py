from datetime import datetime
birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
today = datetime.now()

# Calculate age in years
age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Total days lived
days_lived = (today - birth_date).days

print(f"You are {age_years} years old and have lived {days_lived} days.")
