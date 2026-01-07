from flask import Flask, render_template, request

app = Flask(__name__)

# -------------------------
# Página de registro
# -------------------------
@app.route('/')
def registro():
    return render_template('registro.html')


# -------------------------
# Página de bienvenida
# -------------------------
@app.route('/bienvenida')
def bienvenida():
    nombre = request.args.get('nombre')
    grupo = request.args.get('grupo')
    carrera = request.args.get('carrera')
    return render_template(
        'bienvenida.html',
        nombre=nombre,
        grupo=grupo,
        carrera=carrera
    )


# -------------------------
# Introducción: ¿Qué es el medioambiente?
# -------------------------
@app.route('/introduccion')
def introduccion():
    return render_template('introduccion.html')


# -------------------------
# ¿Cómo empezar?
# -------------------------
@app.route('/como_empezar')
def como_empezar():
    return render_template('como_empezar.html')


# -------------------------
# Beneficios del reciclaje
# -------------------------
@app.route('/beneficios')
def beneficios():
    return render_template('beneficios.html')


# -------------------------
# Programas comunitarios
# -------------------------
@app.route('/programas')
def programas():
    return render_template('programas.html')


# -------------------------
# Menú principal
# -------------------------
@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/quees')
def menu():
    return render_template('quees.html')

@app.route('/bienvenida')
def menu():
    return render_template('bienvenida.html')


@app.route('/index')
def menu():
    return render_template('index.html')


@app.route('/contactos')
def menu():
    return render_template('contactos.html')

@app.route('/reciclaje_inteligente')
def menu():
    return render_template('reciclaje_inteligente.html')




# -------------------------
# Ejecutar aplicación
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
