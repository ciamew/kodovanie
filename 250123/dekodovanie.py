from PIL import Image

pic = Image.open("citynew.png")
pixels = pic.load()


def done():
    text = []
    for j in range(pic.size[1]):
        for k in range(pic.size[0]):
            pixel_blue = pixels[k,j][2]
            blue = bin(pixel_blue)
            text.append(blue[-1])
    return text
text = done()

length = 8
def decoding(text):
    number = ""
    hiddentext = ""
    for i in text:
        y = ""
        number += i
        if len(number) == length:
            h = chr(int(number,2))
            hiddentext += h
            number = ""
        if "#" in hiddentext:
            break
    return hiddentext

print(decoding(text))