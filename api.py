# filename: api.py
"""A basic (single function) API written using hug"""
import hug
import mysql.connector
import json




@hug.get('/allPokemon')
def allPokemon(id):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
    cursor = conn.cursor()
    cursor.execute("""select nom, p_type, total from pokemones where id = %s""", [id])
    rows = cursor.fetchall()

    for row in rows:
        print('{0} | {1} | {2}'.format(row[0], row[1], row[2]))
    conn.close()
    return rows

@hug.post('/Pokemon')
def Pokemon():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO pokemones (id, nom, p_type, total, hp, attack, defense, speed_att, speed_def, speed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", user)
    
    conn.commit()
    conn.close()



