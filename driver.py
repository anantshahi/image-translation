from PIL import Image, ImageDraw, ImageFont
import json
import math
from paddleocr import PaddleOCR, draw_ocr
import preprocessor as pr

def morph(image_file_path,json_file_path):

  json_file = open(json_file_path,'r') # Enter the rendered json file
  data = json.load(json_file)
  target_texts = data.get("config")[0].get('text').keys()
  label_color = data.get("config")[0].get("label_color")
  target_language = data.get("config")[0].get("target_language")
  
  target_language_font = data.get("config")[0].get("target_language_font")
  font_size  = data.get("config")[0].get("font_size")
  font_color=data.get("config")[0].get("font_color")
  fontHindi = ImageFont.truetype(target_language_font, font_size)
  image_filepath = image_file_path #Enter image filepath





  result = pr.paddlepop(image_filepath)
  
  
  bboxes = list()
  for line in result:
    if line[1][0] in target_texts:
      bbox = pr.bbox_coordinates(line)
      
      bboxes.append(bbox)
    else:
      continue

  image = Image.open(image_filepath).convert('RGB')
  for i in range(0,len(bboxes)):
    x = bboxes[i][0]
    y = bboxes[i][1]
    h= bboxes[i][2]
    w = bboxes[i][3]
    text = bboxes[i][4]
    print(text)
  
    img1 = ImageDraw.Draw(image)  
    img1.rectangle([(x,y+h+10),(x+w+12,y)],fill=label_color)
    img1.text(((x,y)),data.get("config")[0].get("text").get(text),fill=font_color,font=fontHindi)
    
  image.save('result/output.jpg')


def main():
  image_path = str('Enter image file path')
  recognised_texts_fe = pr.recognitions(image_path) #Ideally this is the function that you want to send to front end for user to select from text
  json_path = "enter json path here"
  morph(image_file_path=image_path,json_file_path=json_path)

if __name__ == '__main__':
  main()
  

  
  
