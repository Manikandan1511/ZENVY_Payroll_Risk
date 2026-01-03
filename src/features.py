import pandas as pd

def engineer_payroll_features(df):
    # Attendance patterns
    df['attendance_instability'] = df['Late_Arrivals'] / (df['Avg_Work_Hours'] + 1)
    # Leave frequency
    df['unplanned_leave_rate'] = df['Unplanned_Leaves'] / (df['Total_Leaves'] + 1)
    # Salary changes
    df['salary_risk_index'] = df['Salary_Change_Pct'] * (df['Manual_Override'] + 1)
    return df