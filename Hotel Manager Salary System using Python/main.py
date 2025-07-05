import pandas as pd

# Input: total waiters
num_waiters = int(input("Enter number of waiters: "))

# List to store salary data
salary_data = []

for i in range(num_waiters):
    print(f"\nEnter details for waiter {i+1}:")
    name = input("Name: ")
    monthly_salary = float(input("Monthly Salary (₹): "))
    total_working_days = int(input("Total Working Days in Month: "))
    attended_days = int(input("Days Attended: "))
    overtime_hours = float(input("Overtime Hours: "))
    overtime_rate = float(input("Overtime Rate per Hour (₹): "))

    # Calculationsimport pandas as pd
import os

FILENAME = "Waiter_Salary_Report.xlsx"

def calculate_salary():
    name = input("\nWaiter Name: ")
    monthly_salary = float(input("Monthly Salary (₹): "))
    total_working_days = int(input("Total Working Days in Month: "))
    attended_days = int(input("Days Attended: "))
    overtime_hours = float(input("Overtime Hours: "))

    # Calculate per day and per hour rate
    per_day_salary = monthly_salary / total_working_days
    working_hours_per_month = total_working_days * 8  # 8 hours/day
    overtime_rate = monthly_salary / working_hours_per_month

    base_salary = per_day_salary * attended_days
    overtime_amount = overtime_hours * overtime_rate
    final_salary = base_salary + overtime_amount

    return {
        "Name": name,
        "Monthly Salary (₹)": monthly_salary,
        "Working Days": total_working_days,
        "Days Attended": attended_days,
        "Overtime Hours": overtime_hours,
        "Overtime Rate (₹/hr)": round(overtime_rate, 2),
        "Base Salary (₹)": round(base_salary, 2),
        "Overtime Amount (₹)": round(overtime_amount, 2),
        "Final Salary (₹)": round(final_salary, 2)
    }

def save_to_excel(data):
    df_new = pd.DataFrame([data])
    
    if os.path.exists(FILENAME):
        df_existing = pd.read_excel(FILENAME)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_excel(FILENAME, index=False)
    print(f"✅ Data saved for {data['Name']} in '{FILENAME}'")

# Main loop
print("💼 Waiter Salary Calculator - Advanced Version")

while True:
    record = calculate_salary()
    save_to_excel(record)
    
    more = input("\n➕ Do you want to add another waiter? (yes/no): ").strip().lower()
    if more != 'yes':
        print("\n👋 Thank you! Salary report saved.")
        break

    per_day_salary = monthly_salary / total_working_days
    base_salary = per_day_salary * attended_days
    overtime_amount = overtime_hours * overtime_rate
    final_salary = base_salary + overtime_amount

    # Add to list
    salary_data.append({
        "Name": name,
        "Monthly Salary (₹)": monthly_salary,
        "Working Days": total_working_days,
        "Days Attended": attended_days,
        "Overtime Hours": overtime_hours,
        "Overtime Rate (₹/hr)": overtime_rate,
        "Base Salary (₹)": round(base_salary, 2),
        "Overtime Amount (₹)": round(overtime_amount, 2),
        "Final Salary (₹)": round(final_salary, 2)
    })

# Create DataFrame
df = pd.DataFrame(salary_data)

# Save to Excel
df.to_excel(f'{salary_data["Name"]}_Salary_Report.xlsx', index=False)

print("\nSalary report saved as 'Waiter_Salary_Report.xlsx'")
