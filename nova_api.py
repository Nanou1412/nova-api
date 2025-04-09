from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Nova Cloud en ligne ✅"

@app.route("/nova", methods=["POST"])
def nova():
    data = request.json
    commande = data.get("commande", "").lower()
    print("Commande reçue :", commande)

    if commande == "lance nova":
        return {"réponse": "Nova est réveillée. Je suis prête à t’assister."}
    elif "projets" in commande:
        return {"réponse": "Tu travailles actuellement sur CopyPro, MoonBot et Sweet Store."}
    elif "objectif" in commande:
        return {"réponse": "Ton objectif est de générer 20 000 € par mois avec le CPA."}
    else:
        return {"réponse": "Je n'ai pas compris la commande, peux-tu reformuler ?" }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

