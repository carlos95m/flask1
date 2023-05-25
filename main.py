from flask import Flask, request
import rembg

app = Flask(__name__)


@app.route('/remove_background', methods=['POST'])
def remove_background():
    # Obtener la imagen enviada por la aplicación Android
    image_file = request.files['image']

    # Leer los datos de la imagen
    image_data = image_file.read()

    # Eliminar el fondo de la imagen utilizando rembg
    output_data = rembg.remove(image_data)

    # Devolver la imagen resultante sin fondo como respuesta
    return output_data, 200, {'Content-Type': 'image/png'}


if __name__ == '__main__':
    app.run(host='flask-production-082c.up.railway.app', port=80)
