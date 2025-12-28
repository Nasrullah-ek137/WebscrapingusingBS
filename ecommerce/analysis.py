import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("books_data.csv")

# Convert rating words to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Basic analysis
print("Average Price:", df["Price"].mean())
print("Highest Price:", df["Price"].max())
print("Lowest Price:", df["Price"].min())

# Rating distribution
sns.countplot(x="Rating", data=df)
plt.title("Rating Distribution")
plt.show()

# Price vs Rating
sns.boxplot(x="Rating", y="Price", data=df)
plt.title("Price vs Rating")
plt.show()
