import pandas as pd

def engineer_payroll_features(df):
    # Requirement 6: Attendance patterns
    # Measures how 'unreliable' attendance is relative to work hours
    df['attendance_instability'] = df['Late_Arrivals'] / (df['Avg_Work_Hours'] + 1)
    
    # Requirement 7: Leave frequency
    # High unplanned leave ratio is a classic risk indicator
    df['unplanned_leave_rate'] = df['Unplanned_Leaves'] / (df['Total_Leaves'] + 1)
    
    # Requirement 8: Salary changes
    # High change combined with manual overrides
    df['salary_risk_index'] = df['Salary_Change_Pct'] * (df['Manual_Override'] + 1)
    
    return df