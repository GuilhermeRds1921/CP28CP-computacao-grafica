import cv2
import json

def compress_image_rle(image_path, output_json_path):
    # Carrega a imagem em escala de cinza
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        raise ValueError(f"Não foi possível carregar a imagem: {image_path}")

    # Achata a imagem para transformar em uma sequência 1D
    flattened_image = image.flatten()

    # Aplicação do Run-Length Encoding (RLE)
    compressed_data = []
    prev_pixel = flattened_image[0]
    count = 1

    for pixel in flattened_image[1:]:
        if pixel == prev_pixel:
            count += 1
        else:
            compressed_data.append((int(prev_pixel), count))
            prev_pixel = pixel
            count = 1
    
    # Adiciona o último pixel e sua contagem
    compressed_data.append((int(prev_pixel), count))

    # Salva os dados comprimidos em um arquivo JSON
    with open(output_json_path, 'w') as json_file:
        json.dump(compressed_data, json_file, indent=4)

    print(f"Imagem comprimida salva em {output_json_path}")

image_path = './armario.PNG'
output_json_path = 'compressed_image_rle.json'
compress_image_rle(image_path, output_json_path)
