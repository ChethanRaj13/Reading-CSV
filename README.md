# 📊 Data Analysis Script

This project is a simple Python script that performs basic **data exploration** and **visualization** using a CSV file.  
It uses **Pandas** for data manipulation and **Matplotlib** for visual analysis.

---

## 🚀 Features
- Reads and displays data from a CSV file.  
- Prints dataset shape, column names, and the first few rows.  
- Provides summary statistics for numerical columns.  
- Checks for missing values.  
- Visualizes the distribution of a numeric column (`Calories`) with a histogram.

---

## 🧰 Requirements

Make sure you have the following installed:

```bash
pip install pandas matplotlib
```
---
## project-folder/
│
├── data.csv             # Your dataset file
├── analysis.py          # The Python script
└── README.md            # Project documentation
---
## How to Run
Place your dataset file (data.csv) in the same directory as the script.
Open a terminal in the project folder.
Run the script:
```bash
python analysis.py
```
---
## Output
The script will:
Print dataset information in the terminal.
Display a histogram showing the distribution of the Calories column.

Example output:
```
🔹 Shape of the dataset: (500, 5)
🔹 Column names: ['Food', 'Calories', 'Protein', 'Carbs', 'Fat']
```
A histogram will pop up displaying the calorie distribution.
---
