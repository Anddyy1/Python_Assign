# =======================================
# Task 1: Load and Explore the Dataset
# =======================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# I’m using seaborn style to make the plots cleaner and easier to interpret
sns.set_style("whitegrid")

try:
    # Here I load the Iris dataset directly from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # This converts it to a pandas DataFrame automatically
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Dataset file not found.")
    df = pd.DataFrame()
except Exception as e:
    print(f"An unexpected error occurred while loading dataset: {e}")
    df = pd.DataFrame()

# Proceeding only if the dataframe is not empty
if not df.empty:
    try:
        # First, I look at the first few rows to understand the structure
        print("First 5 rows of the dataset:")
        print(df.head())

        # Now I check the datatypes and whether there are missing values
        print("\nDataset info:")
        print(df.info())

        print("\nMissing values in each column:")
        print(df.isnull().sum())

        # If there were missing values, I would fill them with the mean
        df = df.fillna(df.mean(numeric_only=True))
    except Exception as e:
        print(f"Error during dataset exploration or cleaning: {e}")


# =======================================
# Task 2: Basic Data Analysis
# =======================================

if not df.empty:
    try:
        # Here I generate summary statistics for the numerical columns
        print("\nDescriptive statistics:")
        print(df.describe())

        # I also map the numeric target column to actual species names
        df["species"] = df["target"].map(
            dict(zip(range(3), iris.target_names)))

        # Now I can easily compare the mean values across species
        print("\nMean values per species:")
        print(df.groupby("species").mean(numeric_only=True))
    except Exception as e:
        print(f"Error during analysis: {e}")


# =======================================
# Task 3: Data Visualization
# =======================================

if not df.empty:
    try:
        # 1. Line chart: This shows how Sepal Length changes across the dataset samples
        plt.figure(figsize=(8, 5))
        plt.plot(df.index, df["sepal length (cm)"],
                 label="Sepal Length", color="blue")
        plt.title("Sepal Length Trend Across Samples",
                  fontsize=14, fontweight="bold")
        plt.xlabel("Sample Index", fontsize=12)
        plt.ylabel("Sepal Length (cm)", fontsize=12)
        plt.legend()
        plt.tight_layout()
        plt.show()
        # My observation: Sepal length fluctuates between about 4 and 8 cm across samples.

        # 2. Bar chart: This compares the average petal length across the three species
        plt.figure(figsize=(8, 5))
        sns.barplot(x="species", y="petal length (cm)",
                    data=df, palette="viridis", ci=None)
        plt.title("Average Petal Length by Species",
                  fontsize=14, fontweight="bold")
        plt.xlabel("Species", fontsize=12)
        plt.ylabel("Average Petal Length (cm)", fontsize=12)
        plt.tight_layout()
        plt.show()
        # My observation: Iris-virginica has the longest petals, while Iris-setosa has the shortest.

        # 3. Histogram: This helps me see the distribution of sepal length
        plt.figure(figsize=(8, 5))
        sns.histplot(df["sepal length (cm)"], bins=15,
                     kde=True, color="skyblue")
        plt.title("Distribution of Sepal Length",
                  fontsize=14, fontweight="bold")
        plt.xlabel("Sepal Length (cm)", fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
        plt.tight_layout()
        plt.show()
        # My observation: Most sepal lengths fall between 5 and 6 cm, with fewer very short or very long sepals.

        # 4. Scatter plot: This shows the relationship between sepal length and petal length
        plt.figure(figsize=(8, 5))
        sns.scatterplot(
            x="sepal length (cm)",
            y="petal length (cm)",
            hue="species",
            data=df,
            palette="deep",
            s=70
        )
        plt.title("Relationship Between Sepal Length and Petal Length",
                  fontsize=14, fontweight="bold")
        plt.xlabel("Sepal Length (cm)", fontsize=12)
        plt.ylabel("Petal Length (cm)", fontsize=12)
        plt.legend(title="Species")
        plt.tight_layout()
        plt.show()
        # My observation: There is a strong positive relationship, and the species form clear clusters.

    except KeyError as ke:
        print(f"Key error: Column not found - {ke}")
    except TypeError as te:
        print(f"Type error during plotting: {te}")
    except Exception as e:
        print(f"An unexpected error occurred during visualization: {e}")
