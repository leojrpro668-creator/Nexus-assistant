from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>NEXUS</h1>
    <p>Asistente iniciado correctamente.</p>
    """

@app.route("/estado")
def estado():
    return jsonify({"asistente": "NEXUS", "estado": "activo"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
