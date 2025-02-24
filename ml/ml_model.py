import os
import pickle
import pandas as pd
from tqdm import tqdm
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    return df

def preprocess_data(df):
    transactions = df.groupby("pid")["track_name"].apply(list).values.tolist()
    print(f"Number of transactions (playlists): {len(transactions)}")

    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    encoded_baskets = pd.DataFrame(te_ary, columns=te.columns_)
    
    return encoded_baskets

def generate_model(encoded_baskets, min_support=0.01, min_confidence=0.5):
    frequent_itemsets = apriori(encoded_baskets, min_support=min_support, use_colnames=True)
    if frequent_itemsets.empty:
        raise ValueError("No frequent itemsets found. Lower min_support.")

    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    
    for _ in tqdm(range(len(rules)), desc="Processing rules"):
        pass

    return rules

def save_model(model, model_path):
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    csv_file = os.environ.get("DATASET_PATH", "./2023_spotify_ds1.csv")
    model_path = os.environ.get("MODEL_PATH", os.path.join(os.getcwd(), "model.pkl"))

    print(f"Loading data from {csv_file}")
    df = load_data(csv_file)

    print("Preprocessing data...")
    encoded = preprocess_data(df)

    print("Generating association rules...")
    model = generate_model(encoded, min_support=0.05, min_confidence=0.5)

    print("Saving model...")
    save_model(model, model_path)
