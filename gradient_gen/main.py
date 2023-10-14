from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def generate_gradient_from_image(image_path):
    # Load image and convert to numpy array
    image = Image.open(image_path).convert('RGB')
    image_data = np.asarray(image)

    # Extract the color palette from the image
    colors = np.unique(image_data.reshape(-1, image_data.shape[2]), axis=0)

    # Generate the linear gradient from the color palette
    gradient = ''
    for i, color in enumerate(colors):
        color_code = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
        gradient += color_code + ' {}%, '.format(int(i * 100 / (len(colors) - 1)))
    gradient = gradient[:-2]

    # Create the gradient card with the name at the center
    card = f"""<div style="background: linear-gradient({gradient}); width: 300px; height: 200px; display: flex; justify-content: center; align-items: center; font-size: 2rem; font-weight: bold;">{image_path.split('/')[-1].split('.')[0]}</div>"""

    return card

if __name__ == '__main__':
    image_path = 'E:/codes/PyScripts/gradient_gen/neon.jpg'
    gradient_card = generate_gradient_from_image(image_path)
    print(gradient_card)
