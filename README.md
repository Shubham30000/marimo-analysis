# 📊 Interactive Data Analysis with Marimo  
**Author:** 23f2005282@ds.study.iitm.ac.in  

This project demonstrates an **interactive, reactive data analysis notebook** built using **Marimo**, an emerging notebook framework that works like a spreadsheet—automatically updating dependent cells whenever input values change.

It forms part of the Week 8 assignment: *"Create an Interactive Data Analysis with Marimo"* for TDS.

---

## 🧠 Project Overview

The goal of this notebook is to explore the relationship between:

- **Sample size**
- **Confidence intervals**
- **Statistical accuracy**

Users can interactively adjust parameters such as:

- `sample_size`
- `confidence_level`
- `population_mean`

The notebook reacts automatically, updating:

- Statistical calculations  
- Confidence intervals  
- Visualizations  
- Interpretations  
- Markdown summaries  

---

## 🧩 Features Implemented

### ✔ Interactive Widgets (Sliders)
The notebook includes **three Marimo sliders**:

- Sample size (10 to 1000)
- Confidence level (80% to 99%)
- True population mean (50 to 150)

### ✔ Reactive Data Flow
Cells update automatically when widgets change:

- Data generation  
- Summary statistics  
- Confidence interval  
- Plots  
- Interpretation markdown  
- Data table  

### ✔ Dynamic Markdown Output
Using Marimo’s `mo.md()`, the notebook generates:

- Emoji-based feedback  
- Color-coded interpretations  
- Step-by-step statistical explanations  

### ✔ Visualizations
Two side-by-side charts:

1. Histogram with:
   - Sample mean  
   - True mean  
   - Confidence interval bounds  

2. Margin of error vs sample size curve  

### ✔ Data Table
A preview of the first 50 observations is shown interactively.

### ✔ Formula Documentation
Statistical formulas are included using LaTeX:

- Sample mean  
- Standard error  
- Margin of error  
- Confidence interval  

---

## 📂 File Structure

```
analysis.py        # Main interactive Marimo notebook
README.md          # Project documentation
```

---

## ▶️ How to Run the Notebook

### Option A — Using uvx (as in WSL Ubuntu)

```bash
uvx marimo edit analysis.py
```

You will see:

```
URL: http://localhost:2718?access_token=...
```

➡ Open this link in your browser to use the interactive notebook.

---

### Option B — Using pip (Windows or Linux)

```bash
pip install marimo
marimo edit analysis.py
```

Or:

```bash
python -m marimo edit analysis.py
```

---

## 🌐 Raw GitHub URL (for submission)

Replace with your actual link:

```
https://raw.githubusercontent.com/Shubham30000/marp-documentation/main/analysis.py
```

This URL directly gives the notebook’s source code as plain text.

---

## 📝 Assignment Requirements Checklist

| Requirement | Status |
|------------|--------|
| Includes student email | ✅ Done |
| At least two cells with dependencies | ✅ Many cells show dependency chains |
| Interactive widget | ✅ 3 sliders implemented |
| Dynamic markdown based on widget | ✅ Yes (analysis results change automatically) |
| Documented data flow | ✅ Descriptive comments in each cell |
| Provided raw GitHub URL | ✅ Added above |

**This project fulfills all rubric items.**

---

## 📧 Contact

For questions or feedback:

**23f2005282@ds.study.iitm.ac.in**

---

## ⭐ Acknowledgements

- Marimo (Reactive Notebook Framework)  
- TDS Week 8 Assignment Instructions  
- Visualization libraries: NumPy, Pandas, Matplotlib  

