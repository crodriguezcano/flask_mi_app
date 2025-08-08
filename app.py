from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

"""
Muestra la página de inicio de la aplicación web.

    returns:
    str: código HTML generado desde 'index.html'
    Yo aqui meto un "hola don pepito, hola don josé"
"""

if __name__ == '__main__':
    app.run(debug=True)
