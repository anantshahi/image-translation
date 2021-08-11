from paddleocr import PaddleOCR,draw_ocr
import cv2
import math


def recognitions(image_path):
    '''
    This function is responsible to take image path from the front end and provide with list of text it has recognised
    [image_path]: str() Path of the image'
    Return: list() recognised_texts
    '''
    # Also switch the language by modifying the lang parameter
    ocr = PaddleOCR(lang="en") # The model file will be downloaded automatically when executed for the first time
    img_path = str(image_path)
    image = cv2.imread(img_path)
    result = ocr.ocr(image)

    recognised_texts = list()

    for line in result:
        text = line[1][0]
        recognised_texts.append(text)
    
    return recognised_texts

def bbox_coordinates(paddle_det):
    '''
    This function converts four-point coordinate system to xy,w-h system to make it compatible with our current architecture
    [paddle_det] : list() of recognised values from paddlepop function
    Return : list() bbox with coordinates and text
    '''
    bbox = list()
    x = int(paddle_det[0][0][0])
    y = int(paddle_det[0][0][1])
    w = int(math.sqrt((math.pow(paddle_det[0][1][0]-paddle_det[0][2][0],2))+ (math.pow(paddle_det[0][1][1]-paddle_det[0][2][1],2))))
    h = int(math.sqrt((math.pow(paddle_det[0][2][0]-paddle_det[0][3][0],2))+ (math.pow(paddle_det[0][2][1]-paddle_det[0][3][1],2))))
    text = paddle_det[1][0]
    bbox.append(x)
    bbox.append(y)
    bbox.append(w)
    bbox.append(h)
    bbox.append(text)
    
    return bbox

def paddlepop(img_path):
    '''
    This function is responsible to take image path and carry out detection and recognition functions
    [img_path]: str() Path of the image in string
    Return: list() result
    '''
  ocr = PaddleOCR(lang="en")
  image_path = str(img_path)
  image = cv2.imread(image_path)
  result = ocr.ocr(image)
  
  return result







