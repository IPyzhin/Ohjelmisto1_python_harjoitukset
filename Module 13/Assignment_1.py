from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        jakojat = []
        for n in range(1, int(luku) + 1):
            if int(luku) % n == 0:
                jakojat.append(n)
        if len(jakojat) == 2:
            vastaus = {
                "Number": luku,
                "isPrime": True
            }
        else:
            vastaus = {
                "Number": luku,
                "isPrime": False
            }
    except ValueError:
        vastaus = {
            "teksti": "The server cannot process a request"
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