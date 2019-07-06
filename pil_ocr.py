import argparse
import json
import datetime

try:  
    from PIL import Image
except ImportError:  
    import Image
import pytesseract

parser = argparse.ArgumentParser()
parser.add_argument("img", help="image file for OCR processing",type=str)
args = parser.parse_args()

def ocr(filename):  
    """
    This function will handle the core OCR processing of images.
    
    We'll use Pillow's Image class to open the image and pytesseract 
    to detect the string in the image
    """
    text = pytesseract.image_to_string(Image.open(filename))  

    return text

#print(ocr(args.img))
timestamp = datetime.datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

outpupt_json = {"file":args.img,"timestamp":timestamp,"text":ocr(args.img)}

filename = args.img+timestamp+".json"

with open(filename, 'w') as outfile:  
    json.dump(outpupt_json, outfile)

