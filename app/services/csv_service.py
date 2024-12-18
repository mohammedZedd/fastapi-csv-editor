import pandas as pd
from io import StringIO

def read_csv_file(file_contents: str):
    """
    Cette fonction prend en entrée les contenus d'un fichier CSV et retourne son contenu sous forme de DataFrame.
    """
    # Lire le contenu du fichier CSV
    df = pd.read_csv(StringIO(file_contents))
    return df
