import matplotlib.pyplot as plt
import pandas as pd


#A vonaldiagram létrehozó függvény.
def line_maker(csv_file_name: str, save=False):
    """
    Csinál egy vonal diagramot egy .csv fileból.

    Paraméterek:
    - csv_file_name (str): A .csv file amiből az diagram adatai származnak.
    - save (bool) (optional): True -> jpeg-kén menti
    """

    #beolvassa a csv filet.
    df = pd.read_csv(csv_file_name)

    #az oszlopok nevei
    column_names = df.columns.tolist()

    #Leveszi a kiterjesztést a file nevéről.
    name = ""
    for letter in csv_file_name:
        if letter != ".":
            name += letter
        else:
            break
    
    #az ablak kezdő mérete
    plt.figure(figsize=(8, 5))

    #rács stílusa
    plt.grid(True, linestyle='--', alpha=0.5)

    #vonaldiagram létrehozása

    
    plt.plot(df[column_names[0]], df[column_names[1]], color="red", marker="o", linewidth=2)
    
    # "x", "y" - tengely neve, stílusa
    plt.xlabel(column_names[0], fontsize="12")
    plt.ylabel(column_names[1], fontsize="12")

    #diagram neve
    plt.title(name, fontweight="bold", fontsize="20")

    #az x tengelyen lévő adatok 45 fokos forgatása
    plt.xticks(rotation=45, fontsize=10)

    #ha túl nagy a keletkezett ablak, lekicsinyíti
    plt.tight_layout()

    #mentés paraméter ellenőrzése
    if save == True:
        plt.savefig(name + ".jpeg")
    else:
        plt.show()


    #Becsó Barnabás - SSH61K
    #2024.11.17 - 21:23

    #jelenleg csak olyan .csv fileokkal működik, amikben csak 2 oszlop szerepel. (pl: employes quitting.csv)








#példa           V - file neve        V - mentés  
#line_maker("employes quitting.csv", True)




