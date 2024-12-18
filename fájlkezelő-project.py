import pandas as pd

# Példa adatok létrehozása
data = {
    "name": ["John", "Anna", "Peter", "Linda", "James", "Michael"],
    "age": [28, 24, 35, 32, None, 40],
    "join_date": ["2020-01-01", "2019-05-15", "2021-09-10", "2020-07-23", "2021-01-10", "?"],
    "email": ["john@example.com", "anna@domain.com", "peter123@website.net", "linda@site.org", "james@website.com", None],
    "score": [89.5, 78.3, None, 91.0, 85.4, 32.2]
}

# DataFrame létrehozása a fenti adatokkal
df = pd.DataFrame(data)

# CSV fájlba írás
df.to_csv("adatok.csv", index=False)

print("CSV fájl sikeresen létrehozva.")

def load_and_clean_data(file_path="adatok.csv", missing_value_marker="?", date_columns=None):
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
    
    df = pd.read_csv("adatok.csv", na_values=missing_value_marker)

    
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
df_cleaned = load_and_clean_data(file_path="adatok.csv", missing_value_marker="?", date_columns=["join_date"])

# Tisztított adatok megjelenítése
print(df_cleaned.head())

