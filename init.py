import requests
import mysql.connector
from bs4 import BeautifulSoup

conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
cursor = conn.cursor()
url = "https://pokemondb.net/pokedex/all"

response = requests.get(url)
html = str(response.content)
soup = BeautifulSoup(html, "html.parser")

#Création table pokemon :
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemones
    (
       id_pk INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
       id INT NOT NULL,
       nom VARCHAR(100),
       p_type VARCHAR(10),
       total INT(10),
       hp INT(10),
       attack INT(10),
       defense INT(10),
       speed_att INT(10),
       speed_def INT(10),
       speed INT(10)
    );
    """)
tab = soup.find(id="pokedex")
for link in tab.find_all("tr"):
    tt = []
    for l in link.find_all("td"):
        tt.append(l.text)
    print(tt)
    if not tt:
        print("no list")
    else:
        cursor.execute("""INSERT INTO pokemones(id, nom, p_type, total, hp, attack, defense, speed_att, speed_def, speed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", tt)

#recuperation de la liste des pokemon dans un fichier
fichier = open("data.html", "w")
print(fichier.write(html))
fichier.close()

conn.commit()
conn.close()






