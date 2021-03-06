from PylexaTools.responser import Responser
from PylexaTools.requester import Requester
from api_bibli import call_api
import json


def get_help(req):
    resp = Responser(should_end_session=False)
    resp.set_card(title="Bienvenue")
    resp.set_output_speech("Vous pouvez dire : A quelle heure ouvre la bibliothèque du premier arrondissement")
    return resp.get_response()


def manage_new_session(req):
    resp = Responser(should_end_session=False)
    resp.set_card(title="Bienvenue")
    resp.set_output_speech("""
    Bonjour, je suis Bib Lyon. Je vous aide à avoir des informations sur les bibliothèques municipales de Lyon.
    Vous pouvez me demander : à quelle heure ferme la bibliothèque du premier arrondissement ?
    Ou encore : quelle est l'adresse de la bibliothèque du quatrième ?
    """)
    return resp.get_response()


def manage_launch(req):
    resp = Responser(should_end_session=False)
    resp.set_card(title="Bienvenue")
    resp.set_output_speech("Bonjour, je suis Bib Lyon")
    return resp.get_response()


def manage_intent(req):
    name = req.intent.name
    # Dispatch to your skill's intent handlers
    if name == "horaire":
        return get_hours(req.intent)
    if name == "horaires":
        return get_full_hours(req.intent)
    if name == "adresse":
        return get_address(req.intent)
    elif name == "AMAZON.HelpIntent":
        return get_help(req)
    elif name == "AMAZON.CancelIntent" or name == "AMAZON.StopIntent":
        return manage_end_session(req)
    else:
        error_message = """Vous devez nommer clairement l'arrondissement et l'état.
        Vous pouvez demander de l'aide en disant : "Aide-moi".
        """
        return handle_error(error_message)

    resp = Responser()
    resp.set_card(title="Bienvenue")
    welcome_message = "Bonjour, je suis Bib Lyon"
    resp.set_output_speech(welcome_message)
    return resp.get_response()


def manage_end_session(req):
    resp = Responser()
    resp.set_card(title="Bienvenue")
    resp.set_output_speech("Merci d'avoir utilisé Bib Lyon. A bientôt !")
    return resp.get_response()


def handle_error(message):
    resp = Responser()
    resp.set_card(title="Error")
    resp.set_output_speech(message)
    return resp.get_response()


def data():
    days = [
        'lundi',
        'mardi',
        'mercredi',
        'jeudi',
        'vendredi',
        'samedi',
        'dimanche'
    ]
    return days


def format_arr(arr):
    if arr[0] == '2':
        arr = 'deuxième'
    elif arr[0] == '3':
        arr = 'troisième'
    elif arr[0] == '4':
        arr = 'quatrième'
    elif arr[0] == '5':
        arr = 'cinquième'
    elif arr[0] == '6':
        arr = 'sixième'
    elif arr[0] == '7':
        arr = 'septième'
    elif arr[0] == '8':
        arr = 'huitième'
    elif arr[0] == '9':
        arr = 'neuvième'
    return arr


def index_state(state):
    if state == 'ouvre' or state == 'ouvrira' or state == 'sera ouverte':
        index = 0
    elif state == 'ferme' or state == 'fermera' or state == 'sera fermée':
        index = 1
    return index


def treat_horaire_today(intent):
    res = json.loads(call_api())
    today = res['current_day']
    if today != 0 and today != 6:
        days = data()
        arr = format_arr(intent.slots.arrondissement)
        state = intent.slots.etat
        day = intent.slots.jour
        today = days[today]
        index = index_state(state)

        text = f"La bibliothèque du {arr} arrondissement {state} à {res[arr]['horaires'][today][index]} heures aujourd'hui"
    else:
        days = data()
        day = intent.slots.jour
        text = "Toutes les bibliothèques municipales de Lyon sont fermées aujourd'hui. "
    return text


def treat_horaire_day(intent):
    day = intent.slots.jour
    if day != 'lundi' and day != 'dimanche':
        res = json.loads(call_api())
        days = data()
        arr = format_arr(intent.slots.arrondissement)
        state = intent.slots.etat
        index = index_state(state)

        text = f"La bibliothèque du {arr} arrondissement {state} à {res[arr]['horaires'][days[days.index(day)]][index]} heures le {day}"
    else:
        text = f"Toutes les bibliothèques municipales de Lyon sont fermées le {day}."

    return text


def treat_intent_full(intent):
    res = json.loads(call_api())
    if res['current_day'] != 0 and res['current_day'] != 5:
        days = data()
        arr = format_arr(intent.slots.arrondissement)
        today = days[res['current_day']]
        text = f"La bibliothèque du {arr} arrondissement ouvre à {res[arr]['horaires']['mardi'][0]} heures et ferme à {res[arr]['horaires']['mardi'][1]} heures."
    else:
        text = "Toutes les bibliothèques municipales de Lyon sont fermées aujourd'hui."
    return text


def treat_address(intent):
    res = json.loads(call_api())
    days = data()
    arr = format_arr(intent.slots.arrondissement)
    address = res[arr]['address']
    text = f"La bibliothèque du {arr} arrondissement se trouve au {address}"
    return text


def get_hours(intent):
    resp = Responser()
    resp.set_card(title=intent.name)
    text = "Il me manque l'état et l'arrondissement."
    if intent.slots.etat and intent.slots.arrondissement and (
            not intent.slots.jour or intent.slots.jour == "aujourd'hui"):
        text = treat_horaire_today(intent)
    if intent.slots.etat and intent.slots.arrondissement and intent.slots.jour:
        text = treat_horaire_day(intent)
    resp.set_output_speech(text)
    return resp.get_response()


def get_full_hours(intent):
    resp = Responser()
    resp.set_card(title=intent.name)
    text = "Il me manque l'arrondissement."
    if intent.slots.arrondissement:
        text = treat_intent_full(intent)
    resp.set_output_speech(text)
    return resp.get_response()


def get_address(intent):
    resp = Responser()
    resp.set_card(title=intent.name)
    text = "Il me manque l'arrondissement."
    if intent.slots.arrondissement:
        text = treat_address(intent)
    resp.set_output_speech(text)
    return resp.get_response()


def lambda_handler(event, context):
    try:
        req = Requester(event, context)
        if req.request:
            if req.is_new_session():
                print("Nouvelle session.")
            if req.is_launch():
                return manage_launch(req)
            if req.is_intent():
                return manage_intent(req)
            if req.is_end_session():
                return manage_end_session(req)
    except Exception as e:
        return handle_error(str(e))

    resp = Responser()
    resp.set_card(title="Bienvenue")
    resp.set_output_speech("Bonjour, je suis Bib Lyon")
    return resp.get_response()
