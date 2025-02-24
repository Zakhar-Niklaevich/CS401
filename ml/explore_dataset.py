import pandas as pd

# Define dataset paths
dataset_1_path = "/home/datasets/spotify/2023_spotify_ds1.csv"
dataset_2_path = "/home/datasets/spotify/2023_spotify_ds2.csv"
songs_path = "/home/datasets/spotify/2023_spotify_songs.csv"

# Load datasets
df1 = pd.read_csv(dataset_1_path)
df2 = pd.read_csv(dataset_2_path)
songs_df = pd.read_csv(songs_path)

# Print dataset information
print("Dataset 1 (Playlists) Info:")
print(df1.info(), "\n")

print("Dataset 2 (Playlists) Info:")
print(df2.info(), "\n")

print("Songs Dataset Info:")
print(songs_df.info(), "\n")

# Display the first few rows
print("First few rows of Dataset 1:")
print(df1.head(), "\n")

print("First few rows of Songs Dataset:")
print(songs_df.head(), "\n")

# Check for missing values
print("Missing values in Dataset 1:")
print(df1.isnull().sum(), "\n")

print("Missing values in Songs Dataset:")
print(songs_df.isnull().sum(), "\n")

# Check unique values in key columns
print("Unique Playlists in Dataset 1:", df1["pid"].nunique()) 
print("Unique Songs in Dataset 1:", df1["track_uri"].nunique())

print("Unique Playlists in Dataset 2:", df2["pid"].nunique()) 
print("Unique Songs in Dataset 2:", df2["track_uri"].nunique())

print("Unique Songs in Songs Dataset:", songs_df["track_name"].nunique())
