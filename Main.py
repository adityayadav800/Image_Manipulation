#!/usr/bin/env python
# coding: utf-8

# In[9]:


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                text,
                                position_logo,
                                position_text):
    
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    watermark=watermark.resize((50,50))     # Resizing the icon to have a size of 50X50
    
    
    transparent = Image.new('RGB', (width, height))
    
    transparent.paste(base_image, (0,0))
    
    transparent.paste(watermark, position_logo, mask=watermark)
    drawing = ImageDraw.Draw(transparent)
    
    font = ImageFont.load_default()
    width, height = watermark.size
    drawing.text(position_text, text, fill='black',font=font)   # Currently using 'black' color for the text
    transparent.show()
    transparent.save(output_image_path)


if __name__ == '__main__':
   
    watermark_with_transparency('example.jpg',              # Base Image
                                'example_output.jpg',       # Output Image Name
                                'logo.png',                 # Watermark Image
                                'Price Tag',                # Text To Use as Waterark
                                position_logo=(0,0),        # Position for the watermark image
                                position_text=(50,20))      # Position for watermark text


# In[ ]:





# In[ ]:




