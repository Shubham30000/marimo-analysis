import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    # Interactive Data Analysis Notebook
    # Author: 23f2005282@ds.study.iitm.ac.in
    # Purpose: Demonstrate relationship between sample size and statistical confidence
    
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    mo.md(
        """
        # 📊 Interactive Data Analysis: Sample Size vs Confidence
        
        **Author:** 23f2005282@ds.study.iitm.ac.in
        
        This notebook demonstrates how sample size affects statistical confidence 
        in population mean estimation using interactive visualizations.
        """
    )
    return mo, np, pd, plt


@app.cell
def __(mo):
    # CELL 1: Interactive Controls
    # This cell defines the interactive widgets that control the analysis
    # Dependencies: None (input cell)
    # Used by: Cell 2 (sample generation), Cell 3 (visualization)
    
    mo.md("## 🎛️ Control Panel")
    
    # Sample size slider - controls how many data points to generate
    sample_size = mo.ui.slider(
        start=10,
        stop=1000,
        step=10,
        value=100,
        label="Sample Size (n):",
        show_value=True
    )
    
    # Confidence level slider - controls confidence interval width
    confidence_level = mo.ui.slider(
        start=80,
        stop=99,
        step=1,
        value=95,
        label="Confidence Level (%):",
        show_value=True
    )
    
    # Population mean slider - true population parameter
    population_mean = mo.ui.slider(
        start=50,
        stop=150,
        step=5,
        value=100,
        label="True Population Mean (μ):",
        show_value=True
    )
    
    mo.vstack([
        sample_size,
        confidence_level,
        population_mean
    ])
    return confidence_level, population_mean, sample_size


@app.cell
def __(confidence_level, mo, np, population_mean, sample_size):
    # CELL 2: Data Generation and Statistical Calculations
    # This cell depends on the widgets from Cell 1
    # Dependencies: sample_size, population_mean, confidence_level
    # Used by: Cell 3 (creates visualizations from this data)
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate sample data from normal distribution
    # Uses population_mean from Cell 1 as the true mean
    population_std = 20  # Fixed standard deviation
    sample_data = np.random.normal(
        loc=population_mean.value,
        scale=population_std,
        size=sample_size.value
    )
    
    # Calculate sample statistics
    sample_mean = np.mean(sample_data)
    sample_std = np.std(sample_data, ddof=1)
    standard_error = sample_std / np.sqrt(sample_size.value)
    
    # Calculate confidence interval
    # Z-scores for common confidence levels
    z_scores = {80: 1.28, 90: 1.645, 95: 1.96, 99: 2.576}
    z_score = z_scores.get(confidence_level.value, 1.96)
    
    margin_of_error = z_score * standard_error
    ci_lower = sample_mean - margin_of_error
    ci_upper = sample_mean + margin_of_error
    
    # Check if confidence interval captures true mean
    captures_true_mean = ci_lower <= population_mean.value <= ci_upper
    
    mo.md(
        f"""
        ### 📈 Sample Statistics
        
        - **Sample Size:** {sample_size.value}
        - **Sample Mean:** {sample_mean:.2f}
        - **Sample Std Dev:** {sample_std:.2f}
        - **Standard Error:** {standard_error:.2f}
        - **Margin of Error:** {margin_of_error:.2f}
        - **{confidence_level.value}% CI:** [{ci_lower:.2f}, {ci_upper:.2f}]
        """
    )
    return (
        captures_true_mean,
        ci_lower,
        ci_upper,
        margin_of_error,
        population_std,
        sample_data,
        sample_mean,
        sample_std,
        standard_error,
        z_score,
        z_scores,
    )


@app.cell
def __(
    captures_true_mean,
    ci_lower,
    ci_upper,
    confidence_level,
    mo,
    population_mean,
    sample_mean,
    sample_size,
):
    # CELL 3: Dynamic Markdown Output with Interpretations
    # This cell creates dynamic content based on widget states and calculations
    # Dependencies: All variables from Cell 1 and Cell 2
    # Data flow: Widgets → Statistics → Interpretation
    
    # Dynamic emoji based on sample size
    size_emoji = "🔴" if sample_size.value < 30 else "🟡" if sample_size.value < 100 else "🟢"
    
    # Dynamic assessment of confidence interval
    ci_status = "✅ SUCCESS" if captures_true_mean else "❌ MISS"
    ci_emoji = "🎯" if captures_true_mean else "📍"
    
    # Calculate relative error
    relative_error = abs(sample_mean - population_mean.value) / population_mean.value * 100
    
    # Interpretation message
    if sample_size.value < 30:
        interpretation = "⚠️ **Small sample warning:** With fewer than 30 observations, statistical estimates may be unreliable."
    elif sample_size.value < 100:
        interpretation = "📊 **Moderate sample:** Results are reasonably reliable, but larger samples would improve precision."
    else:
        interpretation = "✨ **Large sample:** Statistical estimates are highly reliable with good precision."
    
    mo.md(
        f"""
        ## 🎯 Analysis Results
        
        ### Sample Size Assessment {size_emoji}
        {interpretation}
        
        ### Confidence Interval Evaluation {ci_emoji}
        - **Status:** {ci_status}
        - **True Mean (μ):** {population_mean.value}
        - **Sample Mean:** {sample_mean:.2f}
        - **Relative Error:** {relative_error:.2f}%
        - **{confidence_level.value}% CI:** [{ci_lower:.2f}, {ci_upper:.2f}]
        
        {'🟢' * min(int(sample_size.value / 50), 20)}
        
        ### 💡 Key Insights
        
        1. **Precision improves with sample size:** As n increases from 10 to 1000, 
           the margin of error decreases proportionally to 1/√n
        
        2. **Confidence level tradeoff:** Higher confidence levels (99% vs 80%) 
           produce wider intervals but greater certainty
        
        3. **Statistical accuracy:** The confidence interval should capture the 
           true population mean approximately {confidence_level.value}% of the time
        
        ### 📊 Try This:
        - Increase sample size to see margin of error shrink
        - Change confidence level to see interval width adjust
        - Adjust true mean to test interval coverage
        """
    )
    return (
        ci_emoji,
        ci_status,
        interpretation,
        relative_error,
        size_emoji,
    )


@app.cell
def __(
    ci_lower,
    ci_upper,
    mo,
    np,
    plt,
    population_mean,
    sample_data,
    sample_mean,
    sample_size,
):
    # CELL 4: Visualization
    # This cell creates plots based on the generated data from Cell 2
    # Dependencies: sample_data, sample_mean, ci_lower, ci_upper, population_mean
    # Creates: Histogram and distribution visualization
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot 1: Histogram of sample data
    ax1.hist(sample_data, bins=30, alpha=0.7, color='steelblue', edgecolor='black')
    ax1.axvline(sample_mean, color='red', linestyle='--', linewidth=2, label=f'Sample Mean: {sample_mean:.2f}')
    ax1.axvline(population_mean.value, color='green', linestyle='-', linewidth=2, label=f'True Mean: {population_mean.value}')
    ax1.axvline(ci_lower, color='orange', linestyle=':', linewidth=2, label='CI Bounds')
    ax1.axvline(ci_upper, color='orange', linestyle=':', linewidth=2)
    ax1.set_xlabel('Value')
    ax1.set_ylabel('Frequency')
    ax1.set_title(f'Distribution of Sample Data (n={sample_size.value})')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Margin of error vs sample size
    sizes = np.arange(10, 1001, 10)
    margins = 1.96 * 20 / np.sqrt(sizes)  # Using fixed std=20 and 95% confidence
    
    ax2.plot(sizes, margins, linewidth=2, color='purple')
    ax2.axvline(sample_size.value, color='red', linestyle='--', alpha=0.7, label=f'Current n={sample_size.value}')
    ax2.axhline(1.96 * 20 / np.sqrt(sample_size.value), color='red', linestyle='--', alpha=0.7)
    ax2.set_xlabel('Sample Size (n)')
    ax2.set_ylabel('Margin of Error')
    ax2.set_title('Margin of Error vs Sample Size')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    mo.md("## 📊 Visualizations")
    return ax1, ax2, fig, margins, sizes


@app.cell
def __(fig, mo):
    # Display the figure
    mo.ui.pyplot(fig)
    return


@app.cell
def __(mo, pd, sample_data, sample_size):
    # CELL 5: Data Table Display
    # This cell shows the raw data in a table format
    # Dependencies: sample_data from Cell 2
    
    # Create a DataFrame with sample statistics
    sample_df = pd.DataFrame({
        'Index': range(1, min(sample_size.value, 50) + 1),
        'Value': sample_data[:min(sample_size.value, 50)],
        'Deviation from Mean': sample_data[:min(sample_size.value, 50)] - sample_data.mean()
    })
    
    mo.md(
        f"""
        ## 📋 Sample Data Preview
        
        Showing first {min(sample_size.value, 50)} observations out of {sample_size.value} total:
        """
    )
    
    mo.ui.table(sample_df, selection=None)
    return (sample_df,)


@app.cell
def __(mo):
    # CELL 6: Methodology and Formulas
    # Static documentation cell explaining the mathematical foundation
    
    mo.md(
        r"""
        ## 📚 Methodology
        
        ### Statistical Formulas Used:
        
        1. **Sample Mean:**
           $$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$
        
        2. **Standard Error:**
           $$SE = \frac{s}{\sqrt{n}}$$
        
        3. **Confidence Interval:**
           $$CI = \bar{x} \pm z_{\alpha/2} \times SE$$
        
        4. **Margin of Error:**
           $$ME = z_{\alpha/2} \times \frac{s}{\sqrt{n}}$$
        
        ### Key Relationship:
        
        The margin of error is **inversely proportional to the square root of sample size**:
        
        $$ME \propto \frac{1}{\sqrt{n}}$$
        
        This means to **halve the margin of error**, you need to **quadruple the sample size**.
        
        ---
        
        **Contact:** 23f2005282@ds.study.iitm.ac.in
        """
    )
    return


if __name__ == "__main__":
    app.run()
