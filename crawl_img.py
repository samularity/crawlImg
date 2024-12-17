from playwright.sync_api import sync_playwright
from PIL import Image

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.google.com/search?q=wetter+ludwigsburg")
    page.get_by_role("button", name="Alle ablehnen").click()
    page.wait_for_timeout(1000)#in milliseconds
    page.get_by_role("button", name="Niederschlag").click()
    page.wait_for_timeout(1000)#in milliseconds
    #page.screenshot(path="example.png", scale="css",full_page=True)
    page.screenshot(path="crop.png", scale="css", full_page=True, clip={'x': 85, 'y': 200, 'width': 700 , 'height':370})
    browser.close()


with Image.open("crop.png") as im:

    #cropped_image = im.crop((left, upper, right, lower))
    temp = im.crop((21, 32, 21+123, 32+42))

    #rain = im.crop((21, 150, 21+313, 150+103))
    lowerblock = im.crop((21, 150, 21+313, 150+209))
    lowerblock = lowerblock.resize((200,130 ))
    
    #lowerblock.save("part.png","PNG")

    new_image = Image.new('RGB', (200, 200))
    new_image.paste(temp,(0,0))
    new_image.paste(lowerblock,(0,50))
    #new_image.paste(image2,(image1_size[0],1))
    new_image.save("resized.png","PNG")