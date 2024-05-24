
from PIL import Image
o = Image.open("DSFDSFDS.jpg")
a = o.crop((1, 1, 236, 270))
a.save("VOOOOOLK.jpg")


def b8():
    from PIL import Image
    holiday_cards = {
        "День рождения": "ДР.jpg",
        "Новый год": "НГ.jpg",
        "8 марта": "8М.jpg"
    }
    a = input("введите праздник ")
    if a in holiday_cards:
        b = holiday_cards[a]
        b = Image.open(b)
        b.show()


def c8():
    from PIL import Image, ImageDraw, ImageFont
    img = Image.open("DSFDSFDS.jpg")
    a = img.crop((200, 150, 800, 800))
    a.save("FFFFF.jpg")
    b = input("ведите имя")
    draw = ImageDraw.Draw(a)
    C = ImageFont.truetype("Arial", 30)
    color = (150, 170, 187)
    color2 = (150, 170, 187)
    draw.text((75, 550), b, C, fill == color, stroke_width == 1, stroke_fill == color2)
    draw.text((200, 550), "поздравляем!", font == C, fill == color)
    a.show()
    a.save('УУУУИИИИИ.png')
c8()