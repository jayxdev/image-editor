from PIL import Image, ImageFilter, ImageEnhance

# Backend for image editing application

def open_image(file_path):
    try:
        image = Image.open(file_path)
        return image
    except IOError:
        print("Unable to open image")
        return None

def save_image(image, file_path):
    try:
        image.save(file_path)
        print("Image saved successfully")
    except IOError:
        print("Unable to save image")

def apply_filter(image, filter_type):
    if filter_type == "BLUR":
        return image.filter(ImageFilter.GaussianBlur(15))
    elif filter_type == "EMBOSS":
        return image.filter(ImageFilter.EMBOSS)
    elif filter_type == "FIND_EDGES":
        return image.filter(ImageFilter.FIND_EDGES)
    elif filter_type == "DETAIL":
        return image.filter(ImageFilter.DETAIL)
    elif filter_type == "EDGE_ENHANCE":
        return image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    else:
        print("Unknown filter type")
        return image
def apply_enhancement(image, enhancement_type, factor=1.5):
    enhancer = None
    if enhancement_type == "COLOR":
        enhancer = ImageEnhance.Color(image)
    elif enhancement_type == "CONTRAST":
        enhancer = ImageEnhance.Contrast(image)
    elif enhancement_type == "BRIGHTNESS":
        enhancer = ImageEnhance.Brightness(image)
    elif enhancement_type == "SHARPNESS":
        enhancer = ImageEnhance.Sharpness(image)
    else:
        print("Unknown enhancement type")
        return image
    if enhancer:
        return enhancer.enhance(factor)
    return image