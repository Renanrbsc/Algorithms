from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/redi')
def redirect_pag():
    url = request.args['url']
    link = f"https://www.youtube.com/{url}"
    # https://www.y2mate.com/pt4
    # https://www.y2mate.com/pt/youtube/DPpziAhPwsk
    return redirect(link)


app.run(debug=True)
# url = input('Informe uma URL de video: ')

# url = url[:12]+'ss'+url[:12]
# webbrowser.open(url)
