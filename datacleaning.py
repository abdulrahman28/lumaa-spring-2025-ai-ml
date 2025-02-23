import pandas as pd

# For processing and formatting the dataset for further use: Used by the CLI & GUI
def clean(fln):
    """Load movie dataset from a CSV file."""
    df = pd.read_csv(fln, low_memory=False)
    # Select relevant columns and drop rows with missing descriptions
    df = df[['title', 'overview']].dropna()
    # Rename 'overview' to 'description' for consistency
    df.rename(columns={'overview': 'Description', 'title':'Title'}, inplace=True)
    return df