from flask import Flask, render_template, request, jsonify
from engine.ytfastcut import cortar_rapido
import socket # serve para testar se a porta está sendo usada
import webbrowser # abre o navegador
import time # tempo de espera
import threading # para rodar coisas em paralelo

# =========== GARANTIR ESTRUTURA MÍNIMA =============

from core.app_path import get_clipper_root, get_data_root, get_essentials
get_clipper_root()
get_essentials()
get_data_root()


# ===== RESPONSABILIDADES =====
# 0. Abrir o servidor e navegador
# 1. Interface
# 2. Receber pedido para gerar corte

def porta_em_uso(host="127.0.0.1", port=int("5000")):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) == 0
    
def abrir_navegador():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:5000")

app = Flask(__name__) # cria a variável app e armazena Flask nela

@app.route('/') # A rota principal do site ('/') deve abrir index.html
def home(): # Função para abrir index
    return render_template('index.html') # Renderiza index

@app.route('/cut', methods=['POST']) # A rota de corte indicada por '/cut' deve chamar a função cut e definir como unico método aceitavel o método POST
def cut():
    data = request.get_json() # armazena os dados da requisição na variável data

    if not data: # Valida se os dados existem
        return jsonify({
        "status": "erro",
        "mensagem": "JSON não enviado"
    }), 400

    # Armazena os indexadores em variáveis
    url = data.get('url')
    video_id = data.get('video_id')
    start = data.get('start')
    end = data.get('end')


    if not url or start is None or end is None: # Valida se algum dado deu erro
        return jsonify({
            "status": "erro",
            "mensagem": "Dados incompletos"
        }), 400



    cortar_rapido(url=data["url"], video_id=data["video_id"], start=data["start"], end=data["end"])

    return jsonify({
        "status": "ok",
        "url": url,
        "id": video_id,
        "start": start,
        "end": end
    }) # Retorna com os dados da url

if __name__ == "__main__":
    PORT = 5000

    if porta_em_uso(port=PORT):
        webbrowser.open("http://127.0.0.1:5000")
    else:
        threading.Thread(
            target=abrir_navegador,
            daemon=True
            ).start()
        app.run(
            host="127.0.0.1",
            port=PORT,
            debug=False,
            use_reloader=False
            )
