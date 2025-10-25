"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.lineplot(data=df, x="Age", y="Total Purchase Amount",ax = ax)
    ax.set_title("Average Purchase Amount by Age")
    fig.tight_layout()
    ax.grid(True)
    plt.show()
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x="Payment Method", hue="Gender")
    ax.set_title("Count of Payment Methods by Gender", fontsize=14, fontweight="bold")
    ax.set_xlabel("Payment Method")
    ax.set_ylabel("Number of Customers")
    plt.xticks(rotation=45)
    for container in ax.containers:
     ax.bar_label(container, fmt='%d', label_type='edge', padding=3)
    fig.tight_layout()
    plt.savefig('categorical_plot.png')
    return


def plot_statistical_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    pivot_table = df.pivot_table(
        index='Product Category', 
        columns='Gender', 
        values='Total Purchase Amount', 
        aggfunc='mean'
    )
    sns.heatmap(
        pivot_table,
        annot=True,            
        fmt=".2f",               
        cmap="YlGnBu",           
        linewidths=.5,           
        cbar_kws={'label': 'Average Total Purchase Amount ($)'},
        ax=ax
    )
    

    ax.set_title(
        "Average Purchase Amount Heatmap by Category and Gender",
        fontsize=16,
        fontweight="bold",
        pad=15
    )
    ax.set_xlabel("Gender", fontsize=12)
    ax.set_ylabel("Product Category", fontsize=12)
    
    plt.yticks(rotation=0) 
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df, col: str):
    series = df[col]
    mean = series.mean()
    stddev = series.std()
    skew = series.skew()
    excess_kurtosis = series.kurt()
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
     print("\nInitial DataFrame Head:")
     print(df.head())
    
     print("\nStatistical Summary (Describe):")
     print(df.describe())
    
     print("\nDataFrame Info (Dtypes and Null Counts):")
     df.info()
    
     print("\nCorrelation Matrix (Numerical Features):")
     print(df.corr(numeric_only=True).round(2))
 
     return df


def writing(moments, col):
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    skew_val = moments[2]
    skew_desc = "not skewed"
    if skew_val > 2:
        skew_desc = "right-skewed (positive asymmetry)"
    elif skew_val < 0:
        skew_desc = "left-skewed (negative asymmetry)"
        

    kurt_val = moments[3]
    kurt_desc = "mesokurtic (normal tailedness)"
    if kurt_val > 0:
        kurt_desc = "leptokurtic (heavy/fat tails, sharper peak)"
    elif kurt_val < 2:
        kurt_desc = "platykurtic (light/thin tails, flatter peak)"
    print('\nConclusion:')
    print(f'The data distribution for "{col}" is {skew_desc} and {kurt_desc}.')   
    return


def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = 'Total Purchase Amount'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
