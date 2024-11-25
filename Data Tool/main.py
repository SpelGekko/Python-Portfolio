import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Display basic information about the dataset
def display_basic_info(data):
    print("\nBasic Information:")
    print(data.info())
    print("\nFirst 5 rows of the dataset:")
    print(data.head())

# Analyze and visualize the dataset
def analyze_data(data):
    print("\nData Analysis:")

    # Top 10 movies by average rating
    top_rated = data.sort_values(by='averageRating', ascending=False).head(10)
    print("\nTop 10 Movies by Rating:")
    print(top_rated[['title', 'averageRating']])

    # Plot top 10 movies by rating
    plt.figure(figsize=(10, 6))
    sns.barplot(x='averageRating', y='title', data=top_rated, palette='viridis')
    plt.title('Top 10 Movies by Rating')
    plt.xlabel('Average Rating')
    plt.ylabel('Title')
    plt.show()

    # Average rating by genre
    avg_rating_by_genre = data.groupby('genres')['averageRating'].mean().sort_values(ascending=False)
    print("\nAverage Rating by Genre:")
    print(avg_rating_by_genre)

    # Plot average rating by genre
    plt.figure(figsize=(12, 8))
    avg_rating_by_genre.plot(kind='bar', color='skyblue')
    plt.title('Average Rating by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Average Rating')
    plt.show()

    # Number of movies per year
    movies_per_year = data['releaseYear'].value_counts().sort_index()
    print("\nNumber of Movies per Year:")
    print(movies_per_year)

    # Plot number of movies per year
    plt.figure(figsize=(14, 7))
    movies_per_year.plot(kind='line', marker='o', color='coral')
    plt.title('Number of Movies per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.grid(True)
    plt.show()

# List files in the current directory
def list_files(directory):
    try:
        files = os.listdir(directory)
        print(f"Files in '{directory}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = 'Data Tool/data.csv'  # Path to the dataset
    data = load_data(file_path)
    if data is not None:
        display_basic_info(data)
        analyze_data(data)

if __name__ == "__main__":
    main()