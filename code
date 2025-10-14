from flask import Flask, render_template_string, request, redirect, url_for
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

productos = []

@app.route('/')
def inicio():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AgroConecta - Del campo a tu mesa</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f7f9f7; }
            h1 { color: #2e7d32; }
            form { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
            input, button { margin: 5px; padding: 8px; }
            table { width: 100%; border-collapse: collapse; margin-top: 10px; }
            th, td { padding: 10px; border-bottom: 1px solid #ccc; text-align: left; }
        </style>
    </head>
    <body>
        <h1>🌱 AgroConecta</h1>
        <p>Conecta campesinos y compradores de forma justa y directa.</p>

        <form action="/agregar" method="POST">
            <input type="text" name="nombre" placeholder="Nombre del producto" required>
            <input type="number" name="cantidad" placeholder="Cantidad (kg)" required>
            <input type="number" name="precio" placeholder="Precio (por kg)" required>
            <input type="text" name="productor" placeholder="Nombre del productor" required>
            <button type="submit">Agregar producto</button>
        </form>

        <h2>Productos disponibles</h2>
        <table>
            <tr>
                <th>Producto</th>
                <th>Cantidad</th>
                <th>Precio (kg)</th>
                <th>Productor</th>
            </tr>
            {% for p in productos %}
            <tr>
                <td>{{ p['nombre'] }}</td>
                <td>{{ p['cantidad'] }}</td>
                <td>${{ p['precio'] }}</td>
                <td>{{ p['productor'] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    precio = request.form['precio']
    productor = request.form['productor']

    productos.append({
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio,
        'productor': productor
    })
    return redirect(url_for('inicio'))

# ✅ Esta línea lanza el servidor y genera el enlace público sin bloquear Colab
app.run()
