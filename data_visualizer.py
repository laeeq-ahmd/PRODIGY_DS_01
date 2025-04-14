import pandas as pd
import data_processor as dp
import matplotlib.pyplot as plt

def plot_pop(grouped):
    
    total_population = grouped["Value"].sum()
    grouped["Percentage"] = (grouped["Value"] / total_population) * 100
    grouped.loc[grouped["Gender"] == "male", "Percentage"] *= -1

    # Split by gender
    males = grouped[grouped["Gender"] == "male"]
    females = grouped[grouped["Gender"] == "female"]

    # Plot
    plt.figure(figsize=(10, 7))
    plt.barh(males["Age_Group"], males["Percentage"], color="blue", label="Male")
    plt.barh(females["Age_Group"], females["Percentage"], color="pink", label="Female")

    plt.xlabel("Population Percentage (%)")
    plt.ylabel("Age Group")
    plt.title("Population Pyramid")
    plt.legend()
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

