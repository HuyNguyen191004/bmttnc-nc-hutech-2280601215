import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    pixel_index = 0
    brimary_message = ''.join(format(ord(char), '08b') for char in message)
    brimary_message += '1111111111111110' 
    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col,row)))
            for color_channel in range(3):
                if data_index < len(brimary_message):
                     pixel[color_channel]= int(format(pixel[color_channel],'08b')[:-1]+ brimary_message[data_index],2)
            img.putpixel((col,row), tuple(pixel))
            
            if data_index >= len(brimary_message):
                break
    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print("Steganography complete. Encodeed image saved as", encoded_image_path)
    
def main():
    if len(sys.argv)!=3:
        print("Usage: python encrypt.pt<image_path> <message>")
        return
    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)
    
if __name__ =="__main__":
    main()