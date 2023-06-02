from PIL import Image, ImageDraw
import math
width = 400  # Ancho de la imagen
height = 400  # Alto de la imagen
image = Image.new('RGB', (width, height), (255, 255, 255))  # Crea una imagen blanca
draw = ImageDraw.Draw(image)
center_x = width // 2  # Coordenada x del centro
center_y = height // 2  # Coordenada y del centro
radius = min(center_x, center_y)  # Radio de la circunferencia
texture = Image.open('texture.jpg')
angle_step = 0.01  # Incremento angular para dibujar la circunferencia
cord=r,t=50,50
for angle in range(0, int(2*math.pi/angle_step), int(1/angle_step)):
    x = int(center_x + radius * math.cos(angle * angle_step))
    y = int(center_y + radius * math.sin(angle * angle_step))
    draw.bitmap((x, y),3,2,1)

image.save('circumference_with_texture.jpg')
