from flask import Flask, render_template
import datetime
import requests
import os
import socket


app = Flask(__name__)
today = datetime.date.today()
currentYear = today.strftime("%Y")
currentMonth = today.strftime("%m")
currentDay = today.strftime("%m")
r = requests.get('http://nolaborables.com.ar/api/v2/feriados/{}'.format(currentYear))
json = r.json()
proximo = ""
for item in json:
    hDay = datetime.date(int(currentYear), int(item['mes']), int(item['dia']))
    cDay = datetime.date(int(currentYear), int(currentMonth), int(currentDay))
    if hDay > cDay :
        proximo = item
        break
motivo = proximo['motivo']
tipo = proximo['tipo']
link = proximo['info']
dia = proximo['dia']
mes = proximo['mes']
fecha = '{}/{}'.format(dia, mes)

@app.route("/")
def hello():
    return render_template('feriado.html', motivo = motivo, tipo=tipo, link=link, fecha=fecha)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)