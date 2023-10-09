from flask import Flask, render_template, request, redirect, url_for, send_file
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import io
import base64

app = Flask(__name__, static_url_path='/static')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    # Renderizar a página inicial com a imagem padrão
    return render_template('index.html')

@app.route('/add_text', methods=['POST'])
def add_text():
    # Receber os dados do formulário
    option = request.form['option']
    name = request.form['name']
    position = request.form['position']
    email = request.form['email']
    phone = request.form['phone']
    phone02 = request.form['phone02']
    
    # Definir constantes e opções
    IMG_ML = 'static/img/01-masterline.png'
    IMG_PL = 'static/img/02-platina.png'
    opcoes = {
        'Platina_csc': IMG_PL,
        'Platina_log': IMG_PL,
        'Masterline': IMG_ML
    }
    
    # Carregar a imagem selecionada
    caminho_imagem = opcoes[option]
    print(caminho_imagem)
    imagem = Image.open(caminho_imagem)
    
    desenho = ImageDraw.Draw(imagem)
    
    # Definir texto e fontes
    texto_nome = name
    texto_cargo = position
    texto_email = email
    texto_telefone_fixo = phone
    texto_telefone_movel = phone02
    
    tamanho_fonte = 15
    fonte_atributos = ImageFont.truetype('fonts/josefins/JosefinSans-Regular.ttf', tamanho_fonte)
    
    if caminho_imagem == IMG_ML:
        posicao_nome = (210, 18)
        posicao_cargo = (210, 38)
        posicao_email = (210, 58)
        posicao_telefone_fixo = (210, 78)
        posicao_telefone_movel = (350, 78)
    else:
        posicao_nome = (192, 18)
        posicao_cargo = (192, 38)
        posicao_email = (192, 58)
        posicao_telefone_fixo = (192, 78)
        posicao_telefone_movel = (330, 78)
    
    # Adicionar texto à imagem
    desenho.text(posicao_nome, texto_nome, font=fonte_atributos, fill=(162, 205, 90))
    desenho.text(posicao_cargo, texto_cargo, font=fonte_atributos, fill=(162, 205, 90))
    desenho.text(posicao_email, texto_email, font=fonte_atributos, fill=(3, 3, 3))
    desenho.text(posicao_telefone_fixo, texto_telefone_fixo, font=fonte_atributos, fill=(3, 3, 3))
    desenho.text(posicao_telefone_movel, texto_telefone_movel, font=fonte_atributos, fill=(3, 3, 3))
    
    # Codificar a imagem em base64
    buffered = io.BytesIO()
    imagem.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    # Retorne a imagem modificada codificada em base64
    return render_template('index.html', img_base64=img_base64)

@app.route('/clear_fields', methods=['POST'])
def clear_fields():
    # Lógica para limpar os campos aqui, se necessário
    return render_template('index.html')


@app.route('/save_image', methods=['POST'])
def save_image():
    temp_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_image.png')
    
    if os.path.exists(temp_image_path):
        # Excluir a imagem temporária após salvá-la
        os.remove(temp_image_path)
    
    return redirect(url_for('index'))

@app.route('/image')
def get_image():
    temp_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_image.png')
    if os.path.exists(temp_image_path):
        return send_file(temp_image_path)
    else:
        return "Imagem não encontrada"

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
