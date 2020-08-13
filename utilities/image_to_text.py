import cv2
import requests
import io
import json
import matplotlib.pyplot as plt

#path = "./texts/text1.jpeg"

def plot_image(img1, title = ''):
    fig = plt.figure(figsize = [15,15])
    ax1 = fig.add_subplot()
    ax1.imshow(img1, cmap = 'gray')
    ax1.set(xticks = [], yticks = [], title = title)
    plot_image(img1)

def get_text(path):
    img1 = cv2.imread(path)

    # manually reshaping the image
    height, width, channels = img1.shape
    img1.shape
    
    f = open("./ocr_api_key.txt", "r")
    api_key = f.read()
    f.close()
    
    url_api = "https://api.ocr.space/parse/image"
    
    # compressing the image to bytes to send to the url
    _, compressed_image = cv2.imencode(".jpg", img1, [1, 90])
    file_bytes = io.BytesIO(compressed_image)
    
    result = requests.post(url_api, files = {"text1.jpeg": file_bytes}, data = {"apikey": api_key, "language": "eng"})
    
    result = result.content.decode()
    
    # the result is a string, we want a dictionary
    result = json.loads(result)
    
    text_detected = result.get("ParsedResults")
    # print(text_detected)
    # we get an array of only one element which is a dictionary
    
    text_detected = result.get("ParsedResults")[0].get("ParsedText")
    return text_detected