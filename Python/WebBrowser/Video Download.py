# --- Importando a Biblioteca
from flask import Flask, redirect, render_template, request

# --- Biblioteca flask é um pequeno framework web,
# --- que provê um modelo simples para desenvolvimento web. Uma vez 
# --- importando no Python, Flask pode ser usado para economizar 
# --- tempo construindo aplicações web.

# --- Objetivo deste codigo é facilitar o acesso ao site de download,
# --- como tambem testar as funcionalidades mais simples da biblioteca Flask

# -- Instanciando o objeto Flask
app = Flask(__name__)
 
# -- Criando rota principal para recebimento de URLs
@app.route('/')
def inicio():
    return render_template('index.html')

# -- Rota redirecionada pela 'index.html'
# -- Request obtem a URL, verificamos de quem pertence a URL
# -- dividimos a mesma para obter a "id" do video
# -- Redirecionamos o usuario ao site de download com a "id" obtida
@app.route('/redi')
def redirect_pag():
    url = request.args['url']
    if "youtube" in url:
        link = url.split('=')
        link = f"https://www.y2mate.com/pt/youtube/{link[1]}"
    return redirect(link)


app.run(debug=True)
