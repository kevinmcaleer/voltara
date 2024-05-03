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
image_path = "Voltara Speaks.png"
width = 75
height = 75

data = convert_to_black_and_white(image_path, width, height)
print(data)

def write_pixel_data_to_file(data, filename):
    with open(filename, "w") as file:
        file.write("data = [\n")
        for i in range(0, len(data), 10):
            file.write("  " + ",".join([hex(x) for x in data[i:i+10]]) + ",\n")
        file.write("]\n")

write_pixel_data_to_file(data, "pixel_data.py")

