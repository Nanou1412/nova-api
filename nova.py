import speech_recognition as sr
import pyttsx3
import json
import os

# ---------------------- VOIX DE NOVA ----------------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # voix féminine

def parler(texte):
    print(f"🗣️ Nova : {texte}")
    engine.say(texte)
    engine.runAndWait()

# ---------------------- ÉCOUTE DE NOVA ----------------------
def ecouter():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Nova écoute...")
        audio = recognizer.listen(source)

        try:
            texte = recognizer.recognize_google(audio, language="fr-FR")
            print(f"🧠 Tu as dit : {texte}")
            return texte.lower()
        except sr.UnknownValueError:
            print("❌ Je n'ai pas compris.")
            return ""
        except sr.RequestError:
            print("⚠️ Problème avec l’API Google.")
            return ""

# ---------------------- MÉMOIRE INTELLIGENTE ----------------------
def enregistrer_donnee(cle, valeur):
    fichier = "memoire.json"
    if os.path.exists(fichier):
        with open(fichier, "r", encoding="utf-8") as f:
            donnees = json.load(f)
    else:
        donnees = {}

    donnees[cle] = valeur

    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)

def lire_donnee(cle):
    fichier = "memoire.json"
    if not os.path.exists(fichier):
        return None
    with open(fichier, "r", encoding="utf-8") as f:
        donnees = json.load(f)
    return donnees.get(cle, None)

# ---------------------- INTERACTION AVEC MARWAN ----------------------
parler("Bonjour Marwan, je suis prête. Que veux-tu faire ?")
commande = ecouter()

if "objectif" in commande:
    objectif = lire_donnee("objectif")
    if objectif:
        parler(f"Ton objectif est : {objectif}")
    else:
        parler("Je ne connais pas encore ton objectif. Quel est-il ?")
        nouvel_obj = ecouter()
        enregistrer_donnee("objectif", nouvel_obj)
        parler("C'est noté. Je m'en souviendrai.")

elif "projets" in commande:
    projets = lire_donnee("projets")
    if projets:
        parler(f"Tes projets sont : {projets}")
    else:
        parler("Quels sont tes projets en cours ?")
        nouveaux_projets = ecouter()
        enregistrer_donnee("projets", nouveaux_projets)
        parler("C'est noté.")

else:
    parler("Je n'ai pas compris, peux-tu répéter ?")
