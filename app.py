from flask import Flask, render_template, request, redirect, url_for, send_file
import cv2
import insightface
import os
from flask import jsonify
from tkinter import Tk, filedialog
import tempfile
from datetime import datetime
import random
from flask import session
from collections import defaultdict

model_dir = os.path.join('archivos')





app = Flask(__name__)
user_ip = request.remote_addr if request and request.remote_addr else "unknown_ip"

unique_name = None
result_image = None
a = 1
b = ""

print("insightface", insightface.__version__)

model_dir = os.path.join('archivos')

# Crear una instancia de FaceAnalysis y evitar la descarga automática del modelo




# Preparar la instancia de FaceAnalysis




#############################################################
    
# Diccionario para almacenar el número de veces que un código ha sido validado
codigos_validos = {
    'a1b2c3d': 0, 'e4f5g6h': 0, 'i7j8k9l': 0, 'm0n1o2p': 0, 'q3r4s5t': 0, 'u6v7w8x': 0, 'y9z0a1b': 0, 'c2d3e4f': 0, 'g5h6i7j': 0, 'k8l9m0n': 0,
    'o1p2q3r': 0, 's4t5u6v': 0, 'w7x8y9z': 0, '0a1b2c3': 0, 'd4e5f6g': 0, 'h7i8j9k': 0, 'lmn0opq': 0, 'rstu1vw': 0, 'xyz234a': 0, 'bcd567e': 0,
    'fgh89ij': 0, 'klmnopq': 0, 'rstuvwx': 0, 'yz01234': 0, '56789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0,
    'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0,
    'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0,
    'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0,
    '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0,
    'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0,
    'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0,
    'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0,
    '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0,
    '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0,
    'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0,
    'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0,
    'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0,
    '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0,
    'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0,
    'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0,
    'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0,
    '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0,
    '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0,
    'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0,
    'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0,
    'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0,
    '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0,
    'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0,
    'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0,
    'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0,
    '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0,
    '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0,
    'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0,
    'opqrstuv': 0, 'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0,
    'wxyz0123': 0, '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0, '01234567': 0, '89abcdef': 0, 'ghijklmn': 0, 'opqrstuv': 0, 'wxyz0123': 0,
    '456789ab': 0, 'cdefghij': 0, 'klmnopqr': 0, 'stuvwxyz': 0}
limite_validaciones = 11  # Establece el límite de validaciones permitidas

# Diccionario para almacenar la lista negra de códigos
lista_negra = defaultdict(int)

@app.route('/validar_codigo/<codigo>', methods=['GET'])
def validar_codigo(codigo):
    global codigos_validos, lista_negra

    if codigo in codigos_validos:
        if codigos_validos[codigo] < limite_validaciones:
            # Incrementa el contador
            codigos_validos[codigo] += 1
            # Imprime el estado actual de la cuenta
            print(f"Código {codigo} validado {codigos_validos[codigo]} veces.")
            # Devuelve éxito
            return jsonify({'status': 'success', 'message': 'Código válido'})
        else:
            # Excede el límite de validaciones
            if codigo not in lista_negra:
                lista_negra[codigo] = 1
                # Imprime el estado actual de la cuenta
                print(f"Código {codigo} agregado a la lista negra.")
            return jsonify({'status': 'error', 'message': 'Código ha alcanzado el límite de validaciones'})
    else:
        # Código no válido
        return jsonify({'status': 'error', 'message': 'Código no válido'})






##########################################################################



@app.route('/static_images')
def static_images():
    estilos_path = os.path.join(app.static_folder, 'estilos')
    files = [f for f in os.listdir(estilos_path) if os.path.isfile(os.path.join(estilos_path, f))]
    return jsonify({'files': files})

def construir_imfondo(imagefilename):
    global b
    static_dir = os.path.join('static')
    # Construir la ruta de la imagen de fondo en el directorio 'grandes'
    imfondo_path = os.path.join(static_dir, b, 'grandes', imagefilename)
    
    # Verificar si el archivo existe
    if not os.path.exists(imfondo_path):
        print(f"El archivo no existe en la ruta: {imfondo_path}")
        # Puedes manejar el error de alguna manera, por ejemplo, retornar None
        return None

    return imfondo_path



@app.route('/select_image', methods=['POST'])
def select_image():
    global a
    
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    # Aquí puedes procesar el archivo como lo hacías anteriormente
    # file.save('ruta/del/almacenamiento/' + secure_filename(file.filename))
    
    return 'Archivo cargado con éxito!'


@app.route('/check_a')
def check_a():
    global a
    if a == 1:
        return jsonify({'a': 1})
        
    else:
        return jsonify({'a': 0})
    

@app.route('/')
def seleccion():
    
    return redirect(url_for('seleccion_estilo'))

def obtener_direccion_ip():
    # Obtén la dirección IP del usuario desde la solicitud
    return request.remote_addr

@app.route('/imagen_final', methods=['GET'])
def imagen_final():
    global a
    a = 1
    global unique_name, result_image
    
    # Obtén la dirección IP del usuario
    user_ip = obtener_direccion_ip()

    # Comprueba si unique_name contiene user_ip como parte de su nombre
    if user_ip in unique_name:
        return render_template('imagen_final.html', result_image=unique_name)
    else:
        return "Error: Acceso no autorizado"


@app.route('/index', methods=['GET', 'POST'])
def index():
    global a
    result_image_path = None
    
     # Debes obtener el valor real de 'a' según tus necesidades

    result_image_path = None  # Inicializa la variable result_image_path fuera del bloque condicional

    if request.method == 'POST':
        # Lógica para manejar solicitudes POST
        imagefilename = request.form.get('imagefilename', '')
        print("Nombre de la imagen de fondo recibido en Flask:", imagefilename)
        imfondo_path = construir_imfondo(imagefilename)
        static_dir = os.path.join('static')
        image_files = [f for f in os.listdir(static_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]

        if image_files:
            last_image = max(image_files, key=lambda x: os.path.getctime(os.path.join(static_dir, x)))
            result_image_path = os.path.join('static', last_image)
        
            print("Result Image Path:", result_image_path)

        
        else:
            result_image_path = None
        imagen_final
        
        return render_template('index.html', result_image=result_image_path,a=a)

    # Lógica para manejar solicitudes GET
    imagefilename = str(request.args.get('imagefilename', ''))
    imfondo_path = construir_imfondo(imagefilename)
    return render_template('index.html', imfondo=imfondo_path)



@app.route('/seleccion_estilo')
def seleccion_estilo():
    return render_template('seleccion_estilo.html')






@app.route('/disenos_una_persona')
def disenos_una_persona():
    global b
    b = "individuales"
    # Ruta a la carpeta de imágenes para 1 persona
    folder_path = os.path.join('static', "individuales", 'reducido')
    # Obtener la lista de nombres de archivos en la carpeta
    image_files = os.listdir(folder_path)
    # Construir la ruta completa para cada imagen
    image_paths = [filename for filename in image_files]
    imagefilename = request.args.get('imagefilename', '')
    imfondo_path = construir_imfondo(imagefilename)
    return render_template('galeria.html', image_paths=image_paths, imfondo=imfondo_path)

@app.route('/disenos2personas')
def disenos_una_persona2():
    global b
    b = "dobles"
    # Ruta a la carpeta de imágenes para 1 persona
    folder_path = os.path.join('static', "dobles", 'reducido')
    # Obtener la lista de nombres de archivos en la carpeta
    image_files = os.listdir(folder_path)
    # Construir la ruta completa para cada imagen
    image_paths = [filename for filename in image_files]
    imagefilename = request.args.get('imagefilename', '')
    imfondo_path = construir_imfondo(imagefilename)
    return render_template('galeria2.html', image_paths=image_paths, imfondo=imfondo_path)

@app.route('/disenos3personas')
def disenos_una_persona3():
    global b
    b = "triples"
    # Ruta a la carpeta de imágenes para 1 persona
    folder_path = os.path.join('static', "triples", 'reducido')
    # Obtener la lista de nombres de archivos en la carpeta
    image_files = os.listdir(folder_path)
    # Construir la ruta completa para cada imagen
    image_paths = [filename for filename in image_files]
    imagefilename = request.args.get('imagefilename', '')
    imfondo_path = construir_imfondo(imagefilename)
    return render_template('galeria3.html', image_paths=image_paths, imfondo=imfondo_path)



@app.route('/disenos4personas')
def disenos_una_persona4():
    global b
    b = "cuadruples"
    # Ruta a la carpeta de imágenes para 1 persona
    folder_path = os.path.join('static', "cuadruples", 'reducido')
    # Obtener la lista de nombres de archivos en la carpeta
    image_files = os.listdir(folder_path)
    # Construir la ruta completa para cada imagen
    image_paths = [filename for filename in image_files]
    imagefilename = request.args.get('imagefilename', '')
    imfondo_path = construir_imfondo(imagefilename)
    return render_template('galeria4.html', image_paths=image_paths, imfondo=imfondo_path)

@app.route('/disenos5personas')
def disenos_una_persona5():
    global b
    b = "quintuples"
    # Ruta a la carpeta de imágenes para 1 persona
    folder_path = os.path.join('static', "quintuples", 'reducido')
    # Obtener la lista de nombres de archivos en la carpeta
    image_files = os.listdir(folder_path)
    # Construir la ruta completa para cada imagen
    image_paths = [filename for filename in image_files]
    imagefilename = request.args.get('imagefilename', '')
    imfondo_path = construir_imfondo(imagefilename)
    return render_template('galeria5.html', image_paths=image_paths, imfondo=imfondo_path)



from datetime import datetime
@app.route('/procesar', methods=['POST'])
def procesar():
    global unique_name, result_image
    swapper = insightface.model_zoo.get_model("inswapper_128.onnx")
    app_insightface =  swapper

    data = request.get_json()
    imagefilename_from_form = data.get('imagefilename', '')
    
    imfondo_path = construir_imfondo(imagefilename_from_form)

    print("Ruta de la imagen de fondo:", imfondo_path)

    img = cv2.imread(imfondo_path)

    if img is None:
        print("Error al cargar la imagen.")
        return jsonify({'status': 'error', 'message': 'Error al cargar la imagen'})

    faces = app_insightface.get(img)
    
    # Ordenar las caras por la posición del cuadro delimitador
    faces = sorted(faces, key=lambda x: x['bbox'][0])

    # Almacena los datos de los rostros en una lista
    faces_data = []

    for i, source_face in enumerate(faces):
        bbox = source_face["bbox"]
        bbox = [int(b) for b in bbox]
        
        img_persona_path = select_image()
        
        # Almacena los datos del rostro actual en la lista faces_data
        current_face_data = {
            'source_face': source_face,
            'img_persona_path': img_persona_path
        }
        faces_data.append(current_face_data)

    # Procesa los datos almacenados para generar las imágenes finales
    for i, face_data in enumerate(faces_data):
        source_face = face_data['source_face']
        img_persona_path = face_data['img_persona_path']
        
        img_persona = cv2.imread(img_persona_path)
        remp_faces = app_insightface.get(img_persona)
        remp_faces = remp_faces[0]
        img = swapper.get(img, source_face, remp_faces, paste_back=True)
        
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        random_number = str(random.randint(100000000, 999999999))
        user_ip = obtener_direccion_ip()
        print("Valor de user_ip:", user_ip)
        unique_name = f"output_image_{timestamp}_{random_number}_{user_ip}_{i}.jpg"
        print("Nombre de archivo único:", unique_name)
        output_path = os.path.join('static', unique_name)
        cv2.imwrite(output_path, img)

    # Devuelve la última imagen generada como resultado
    result_image = output_path
    

    # Pasar la variable unique_number al template
    return render_template('imagen_final.html', result_image=result_image, unique_number=unique_name)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
