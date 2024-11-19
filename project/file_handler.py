import pandas as pd

def load_and_clean_data(file_path, missing_value_marker="?", date_columns=None):
    """
    Betölti és megtisztítja a megadott CSV fájl adatait.

    Paraméterek:
    - file_path (str): A CSV fájl elérési útvonala.
    - missing_value_marker (str, optional): Az a karakter vagy string, ami a hiányzó értékeket jelöli (pl. "?").
    - date_columns (list, optional): A dátum oszlopok nevei, amelyeket dátum formátumba kell konvertálni.

    Visszatérési érték:
    - df (pd.DataFrame): A megtisztított adatok DataFrame-je.
    """
    
    # Beolvassa a CSV fájlt, a megadott hiányzó értékek jelölőivel
    df = pd.read_csv(file_path, na_values=missing_value_marker)
    
    # Ellenőrzi, és kezelni a hiányzó értékeket
    # Ha sok hiányzó érték van egy oszlopban, azt el is távolíthatjuk (itt 50% alatt)
    missing_threshold = 0.5
    df = df.dropna(thresh=int(missing_threshold * len(df)), axis=1)
    
    # A maradék hiányzó értékek feltöltése az oszlop típusától függően
    for column in df.columns:
        if df[column].dtype == 'float64' or df[column].dtype == 'int64':
            # Numerikus oszlopok: hiányzó értékeket feltöltjük az oszlop átlagával
            df[column].fillna(df[column].mean(), inplace=True)
        else:
            # Szöveges oszlopok: hiányzó értékeket feltöltjük "N/A" értékkel
            df[column].fillna("N/A", inplace=True)
    
    # Konvertálja a dátum oszlopokat datetime formátumba
    if date_columns:
        for date_col in date_columns:
            if date_col in df.columns:
                df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    
    # Ellenőrzi és eltávolítja a joker karaktereket
    # Itt például a nem alfanumerikus karaktereket távolítjuk el szöveges mezőkben
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = df[column].str.replace(r'[^A-Za-z0-9\s]', '', regex=True)

    return df

# Adatok betöltése és tisztítása
#df_cleaned = load_and_clean_data(file_path="adatok.csv", missing_value_marker="?", date_columns=["join_date"])

# Tisztított adatok megjelenítése
#print(df_cleaned.head())
