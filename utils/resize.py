# importing Image class from PIL package 
from PIL import Image
from pathlib import Path
   
# creating a object 
image = Image.open("./static/media/home_page/home_image_4.jpg")
MAX_SIZE = (1000, 1000)
  
image.thumbnail(MAX_SIZE)
  
# creating thumbnail
image.save('./static/media/home_page/home_image_4.webp', format="webp", quality=85)