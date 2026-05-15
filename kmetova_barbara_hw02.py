import json

# Vytvoríme si prázdne zoznamy. Lines potrebujeme na čítanie súboru a movie_list na konečný výstup, do ktorého potom vložíme slovníky s filmami.
lines = []
movie_list = []

# Otvoríme súbor, zadáme kódovanie na podporu diakritiky a čítame po riadkoch.
with open('netflix_titles.tsv', encoding='utf-8') as file:
    lines = file.readlines()

# Vytvoríme for cyklus, ktorým si rozdelíme hodnoty do stĺpcov. Keďže súbor je tsv, tak hodnoty oddelujeme tabulátorom ("\t"). Vytiahneme si stĺlpce, ktoré budeme potrebovať do finálneho súboru podľa indexu.
for line in lines[1:]: 
    columns = line.split("\t") 
    title = columns[2] 
    directors = columns[15]
    cast = columns[16]
    genres = columns[8]
# Dekádu vypočítame tak, že rok prevedieme na číslo, vydelíme 10 aby sme mohli zaokrúhliť číslo a dostať rok len s desaťročím a potom vynásobíme naspät 10.     
    decade = int(columns[5]) // 10 * 10
# Tu si podchytíme prázdne hodnoty v jednotlivých stĺpcoch, aby v prípade, že hodnota na jednotlivých filmoch chýba, tak sa vytvorí v slovníku prázdny zoznam a for cyklus ju nepreskočí. 
    if directors == "":
        directors = []
    else:
        directors = directors.split(",")    
    
    if cast == "":
        cast = []
    else:
        cast = cast.split(",")    

    if genres == "":
        genres = []
    else:
        genres = genres.split(",")    

# Vytvoríme si slovník, do ktorého vložíme jednotlivé hodnoty zadefinované predtým.        
    movie = {
        "title": title,
        "directors": directors,
        "cast": cast,
        "genres": genres,
        "decade": decade
    }
    movie_list.append(movie)
   
# Uložíme si súbor vo formáte json. 
with open('kmetova_barbara_hw_02.json', mode='w', encoding='utf-8') as output_file:
    json.dump(movie_list, output_file, indent=4, ensure_ascii=False)