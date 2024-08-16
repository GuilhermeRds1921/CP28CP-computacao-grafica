import cv2
import json
import os

def generate_histogram(image_path, output_json_path):
    # Verifica se o arquivo de imagem existe
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Arquivo de imagem não encontrado: {image_path}")
    
    # Carrega a imagem
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Não foi possível carregar a imagem: {image_path}")

    # Converte a imagem para RGB (caso esteja em BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calcula o histograma para cada canal de cor (R, G, B)
    histogram_dict = {}
    for i, color in enumerate(['R', 'G', 'B']):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        histogram_dict[color] = hist.flatten().tolist()

    # Salva os dados do histograma em um arquivo JSON
    with open(output_json_path, 'w') as json_file:
        json.dump(histogram_dict, json_file, indent=4)

    print(f"Histograma salvo em {output_json_path}")

image_path = './armario.PNG'
output_json_path = 'histograma.json'
generate_histogram(image_path, output_json_path)
