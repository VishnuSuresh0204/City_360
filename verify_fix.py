
from datetime import date, datetime

def calculate_wages(start_str, end_str, wage_per_day):
    sdate = datetime.strptime(start_str, "%Y-%m-%d")
    edate = datetime.strptime(end_str, "%Y-%m-%d")
    date_diff = edate - sdate
    # New logic
    totalWage = (int(date_diff.days) + 1) * (int(wage_per_day))
    return totalWage

print("Testing Wage Calculation:")
w1 = calculate_wages("2023-10-27", "2023-10-27", 100)
print(f"Same day (2023-10-27 to 2023-10-27) @ 100/day: {w1} (Expected 100)")

w2 = calculate_wages("2023-10-27", "2023-10-28", 100)
print(f"Two days (2023-10-27 to 2023-10-28) @ 100/day: {w2} (Expected 200)")

# Verify HTML content
print("\nVerifying HTML file content:")
with open(r'c:\Users\admin\Documents\gone\city360UPDATED\city360UPDATED\city360UPDATED\city360\Templates\user\payment.html', 'r') as f:
    content = f.read()
    if 'name="cardno"' in content:
         # It should still be there for the ACTUAL card number field
         print("Found name='cardno'. Checking specifics...")
         # Check if it's in the Amount field
         # The Amount field line has value="{{i.wages}}"
         lines = content.split('\n')
         for i, line in enumerate(lines):
             if 'value="{{i.wages}}"' in line:
                 if 'name="cardno"' in line:
                     print(f"FAIL: Amount field line {i+1} still has name='cardno': {line.strip()}")
                 else:
                     print(f"PASS: Amount field line {i+1} does NOT have name='cardno': {line.strip()}")
