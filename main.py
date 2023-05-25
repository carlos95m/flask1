app.debug = True

from flask import Flask, request
import rembg

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola! La API está funcionando correctamente."

@app.route('/remove_background', methods=['POST'])
def remove_background():
    # Obtener la imagen enviada por la aplicación Android
    image_file = request.files.get('image')

    if image_file is None:
        return "No se proporcionó ningún archivo de imagen", 400

    # Leer los datos de la imagen
    image_data = image_file.read()

    # Eliminar el fondo de la imagen utilizando rembg
    output_data = rembg.remove(image_data)

    # Devolver la imagen resultante sin fondo como respuesta
    return output_data, 200, {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=35)

