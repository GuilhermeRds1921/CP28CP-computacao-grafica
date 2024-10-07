from PIL import Image, ImageDraw

def apply_halftone(image_path, output_image_path, dot_size=10):
    # Carrega a imagem
    image = Image.open(image_path).convert('L')  # Converte para escala de cinza

    # Obter as dimensões da imagem
    width, height = image.size

    # Criar uma nova imagem para o resultado final
    halftone_image = Image.new('L', (width, height), 255)
    draw = ImageDraw.Draw(halftone_image)

    # Aplicar o efeito de halftone
    for y in range(0, height, dot_size):
        for x in range(0, width, dot_size):
            # Extrair o valor médio de brilho da região do ponto
            region = image.crop((x, y, x + dot_size, y + dot_size))
            brightness = sum(region.getdata()) / (dot_size * dot_size)

            # Calcular o raio do círculo
            radius = int((brightness / 255) * (dot_size / 2))

            # Desenhar o círculo na nova imagem
            draw.ellipse((x, y, x + 2 * radius, y + 2 * radius), fill=0)

    # Salvar a imagem de saída
    halftone_image.save(output_image_path)
    print(f"Imagem de halftone salva em {output_image_path}")

image_path = './armario.PNG'
output_image_path = 'halftone_output.jpg'
apply_halftone(image_path, output_image_path)
