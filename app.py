from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
import forms

app = Flask(__name__)
app.secret_key='clave secreta'

csrf=CSRFProtect(app)

@app.route('/')
def index():
    titulo = "Flask"
    lista = ["Juan", "Pedro", "Maria", "Luis"]
    #Se renderiza
    return render_template('index.html', titulo=titulo, lista=lista)


@app.route('/operasBas', methods=["GET", "POST"])
def operas1():
    n1=0
    n2=0
    res=0
    if request.method == "POST":
       n1 = request.form.get('n1')
       n2 = request.form.get('n2')
       res=float(n1)+float(n2)
    return render_template("operasBas.html", n1=n1, n2=n2, res=res)

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    tem=float(n1)+float(n2)
    return f"La suma es: {tem}"


@app.route('/usuarios', methods=["GET", "POST"])
def usuarios():
    mat=0
    nom=''
    apa=''
    ama=''
    email=''
    usuarios_class=forms.UserForm(request.form)
    if request.method=='POST' and usuarios_class.validate():
        mat=usuarios_class.matricula.data
        nom=usuarios_class.nombre.data
        apa=usuarios_class.apaterno.data
        ama=usuarios_class.amaterno.data
        email=usuarios_class.correo.data
        mensaje='Bienvenido {}' .format(nom)
        flash(mensaje)
    #Se renderiza
    return render_template('usuarios.html' , form=usuarios_class,
                           mat=mat, nom=nom, apa=apa, ama=ama, email=email)

@app.route('/alumnos')
def alumnos():
    #Se renderiza
    return render_template('alumnos.html')

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
    csrf.init_app(app)
    app.run(debug=True)
