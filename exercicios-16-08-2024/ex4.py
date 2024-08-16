import cv2
import json
import numpy as np

def decompress_rle(json_path, output_image_path, image_shape):
    # Carrega os dados comprimidos do arquivo JSON
    with open(json_path, 'r') as json_file:
        compressed_data = json.load(json_file)

    # Reconstrói a sequência de pixels a partir dos dados comprimidos
    decompressed_image = []
    for pixel_value, count in compressed_data:
        decompressed_image.extend([pixel_value] * count)

    # Converte a lista de pixels em um array NumPy e remodela para a forma original
    decompressed_image = np.array(decompressed_image, dtype=np.uint8)
    decompressed_image = decompressed_image.reshape(image_shape)

    # Salva a imagem reconstruída
    cv2.imwrite(output_image_path, decompressed_image)
    print(f"Imagem descomprimida salva em {output_image_path}")

json_path = 'compressed_image_rle.json' 
output_image_path = 'decompressed_image.jpg'
image_shape = (582, 585)  

decompress_rle(json_path, output_image_path, image_shape)
