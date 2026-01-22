from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/hola')
def hola():
    return "Hola Mundo"

@app.route('/user/<string:user>')
def user(user):
    return f"Hello {user}"

@app.route('/numero/<int:n>')
def numero(n):
    return f"<h1>El numero es: {n}</h1>"

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return f"<h1>Hola, {username}!, tu id es: {id}</h1>"

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route('/default/')
@app.route('/default/<string:param>')
def default(param="Juanito"):
    return f"<h1>Hola , {param}</h1>"

@app.route('/operas')
def operas():
    return """
    <form>
        <input type="text" name="n1">
        <input type="text" name="n2">
        <input type="submit" value="Enviar">
    </form>
    """

if __name__ == '__main__':
    app.run(debug=True)

