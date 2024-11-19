
#könyvtárak betöltése
import file_handler as fh
import diagrams as dg
import pandas as pd
import selecter as sl


#lista
list = {
    "honapok": ["január", "február", "március", "április", "május", "június", "július", "augusztus", "szeptember", "október", "november", "december"],
    "db": [12, 32, 45, 32, 12, 65, 23, 12, 0, 3, 45, 34]
}

#létrehozza a .csv filet a listából
df = pd.DataFrame(list)
df.to_csv("employes quitting.csv", sep=",", index_label=False)

#beolvassa, és megtisztítja a .csv filet
fh.load_and_clean_data(file_path="employes quitting.csv", missing_value_marker="?")

#létrehoz egy vonaldiagramot a .csv fileból
dg.line_maker("employes quitting.csv", sl.select(True, False, "mentés: igen", "mentés: nem"))





