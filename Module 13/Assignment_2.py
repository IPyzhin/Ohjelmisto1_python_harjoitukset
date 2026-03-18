import mysql.connector
from flask import Flask, jsonify

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='boris',
    password='Bubalar60',
    autocommit=True
)

app = Flask(__name__)

@app.route('/kenttä/<icao>')
def kenttä(icao):
    try:
        query = (f"SELECT name, municipality FROM airport WHERE ident = %s")
        cursor = yhteys.cursor()
        cursor.execute(query, (icao.upper(),))
        result = cursor.fetchone()
        if cursor.rowcount:
            vastaus = {
                "ICAO":icao,
                "Name":result[0],
                "Municipality":result[1]
            }
        cursor.close()
        return jsonify(vastaus)
    except ValueError:
        vastaus = {
            "teksti": f"Airport with this {icao} code does not found."
        }

    return jsonify(vastaus)

@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": virhe.code,
        "teksti": virhe.description
    }
    return jsonify(vastaus), virhe.code

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)