# ZENVY Payroll Risk Analysis
**Objective:** Identify high-risk payroll records using Machine Learning.

## Project Structure
- `data/`: Contains the 3,500 records dataset.
- `src/`: Modular Python scripts for feature engineering and model definitions.
- `notebooks/`: Full EDA, Model Comparison, and Feature Importance analysis.

## How to Run
1. Activate virtual environment: `source .venv/bin/activate`
2. Install requirements: `pip install -r requirements.txt`
3. Run the notebook in VS Code.

## Conclusion
The XGBoost model achieved the highest F1-Score, identifying Salary Spikes and Unplanned Leaves as the most significant risk indicators.