from PIL import Image

def convert_to_black_and_white(image_path, width, height):
    # Open the image file
    img = Image.open(image_path)
    
    # Convert the image to grayscale
    img = img.convert("L")
    
    # Resize the image to the specified width and height
    img = img.resize((width, height))
    
    # Convert the image to a list of pixel values
    pixel_values = list(img.getdata())
    
    return pixel_values

# Example usage:
image_path = "example.png"
width = 75
height = 75

data = convert_to_black_and_white(image_path, width, height)
print(data)
