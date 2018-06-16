# filename: api.py
"""A basic (single function) API written using hug"""
import hug
import mysql.connector ,json





@hug.get('/' output=hug.output_format.json))
def getPokemon(id):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemones")
    cursor = conn.cursor()
    cursor.execute("""select nom, p_type, total from pokemones where id = %s""", [id])
    res = cursor.fetchall()
    
    return json.dumps(res)
    
    conn.close()
    return rows

@hug.delete('/' output=hug.output_format.json))
def Pokemon():
    cursor = cnx.cursor()
    print(body.get("id"))
    try:
        cursor.execute("""DELETE FROM pokemon WHERE id = %s""", [str(body.get("id"))])
        conn.commit()
    except:
        return "ERROR"

    return json.dumps("it work")


