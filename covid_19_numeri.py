import telebot
import requests
import time

API_TOKEN = '???'
CHANNEL_ID = '@covid_19_numeri'
bot = telebot.TeleBot(API_TOKEN)
USERNAME_ADMIN = "???"

CONFERMATI = '⚠️ Confermati: '
RICOVERATI = '\n✅ Guariti: '
CRITICI = '\n💢Critici: '
MORTI = '\n🖤 Morti: '
LAST_UPDATE = '\n📡 Ultimo Cambiamento: '
LAST_UPGRADE = '\n⏰ Ultimo Caricamento: '
CREDITI = '\n💻 Crediti: Alessandro Greco'

MESSAGE_ID = 38

def get_json():
    url = "https://covid-19-data.p.rapidapi.com/totals"

    headers = {
        'x-rapidapi-key': "???",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return response.json()


@bot.message_handler(commands=["start"])
def update(message):
    if message.from_user.username == USERNAME_ADMIN:
        response_data = get_json()
        TEXT = CONFERMATI + str(format(response_data[0]['confirmed'], ","))
        TEXT = TEXT + RICOVERATI + str(format(response_data[0]['recovered'], ","))
        TEXT = TEXT + CRITICI + str(format(response_data[0]['critical'], ","))
        TEXT = TEXT + MORTI + str(format(response_data[0]['deaths'], ","))
        TEXT = TEXT + '\n'
        TEXT = TEXT + LAST_UPDATE + str(response_data[0]['lastChange'])
        TEXT = TEXT + LAST_UPGRADE + str(response_data[0]['lastUpdate'])
        TEXT = TEXT + '\n\n---------------------------------\n\n'
        TEXT = TEXT + "🙋🏻‍♂️ Sviluppatore: Alessandro Greco"
        
        try:
            bot.edit_message_text(TEXT, CHANNEL_ID, MESSAGE_ID)
        except Exception as e:
            print("[WARN] - Exception detected!")
            print(e)
        time.sleep(3600)
        update(message)

bot.polling()