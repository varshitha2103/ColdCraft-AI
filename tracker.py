import pandas as pd
import os

CSV_FILE = "results.csv"

def log_result(version, outcome):
    df = pd.DataFrame([{"version": version, "outcome": outcome}])
    if os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(CSV_FILE, index=False)

def load_results():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    return pd.DataFrame(columns=["version", "outcome"])
