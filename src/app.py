from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')     #Decorador o rutas, llamar a un archivo
def index():       
    titulo='IEVN-1001'  
    list=['Pedro','Juan', 'Fulanito']
    return render_template('index.html', titulo=titulo, list=list) #Pasar parametros al archivo

@app.route('/uno') 
def uno():
    return render_template('uno.html')

@app.route('/dos') 
def dos():
    return render_template('dos.html')

#@app.route('/')     #Decorador o rutas
#def index():       #Declarar metodo
#    return '<h1>Hola Mundo !!!</h1>'

@app.route('/hola') 
def hola():
    return 'Saludo Hola'

@app.route('/user/<string:user>')#Pasar Parametros a traves del navegador
def user(user):
    return "El usuario es: {}".format(user)

@app.route('/numero/<int:n1>')
def numero(n1):
    return "El numero es: {}".format(n1)

@app.route('/user/<string:nom>/<int:id>')
def datos(nom, id):
    return "<h1>ID: {} Nombre: {} </h1>".format(id,nom)

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return "<h1>La suma es {}".format(n1+n2)

@app.route('/default')
@app.route('/default/<string:nom>')
def nom(nom="Dario"):
    return '<h1>El nombre es: {}</h1>'.format(nom)

if __name__ == "__main__":  #Correr la funcion
    app.run(debug=True)     #Hacer que corra sin ejecutar en cmd