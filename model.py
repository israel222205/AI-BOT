from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def get_class(model_path, labels_path, image_path):

    # configurar o numpy
    np.set_printoptions(suppress=True)

    # Carregar o modelo
    model = load_model(model_path, compile=False)

    # Carregar os rótulos
    class_names = open(labels_path, "r", encoding="utf-8").readlines()

    # criar um array de imagem com o tamanho correto
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # abrir a imagem
    image = Image.open(image_path).convert("RGB")
    # redimensionar a imagem
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # converter a imagem em um array
    image_array = np.asarray(image)

    # normalizar a imagem
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # carregar a imagem no array
    data[0] = normalized_image_array

    # fazer a previsão
    prediction = model.predict(data)
    index = np.argmax(prediction)

    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name[2:], confidence_score
