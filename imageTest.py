from urllib.request import Request, urlopen #For opening online images
from tkinter import * #For pop-up
from PIL import ImageTk #For image within tk pop-up

num = int(input("Num: "))
req = Request(
    url=f'https://cdn.discordapp.com/embed/avatars/{num}.png', #Image URL
    headers={'User-Agent': 'Mozilla/5.0'} #Tells Discord we are using a Mozilla browser
)

#Gets the image from the URL and displays it
root = Tk()
data = urlopen(req)
image = ImageTk.PhotoImage(data=data.read())
Label(root, image=image).pack()
root.mainloop()