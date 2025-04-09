from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Nova Cloud en ligne ✅"

@app.route("/nova", methods=["POST"])
def nova():
    data = request.json
    print("Commande reçue :", data)
    # Tu peux déclencher autre chose ici
    return {"status": "Nova a reçu : " + str(data)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
