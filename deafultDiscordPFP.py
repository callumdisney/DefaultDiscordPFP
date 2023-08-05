from urllib.request import Request, urlopen #For opening online images
from tkinter import * #For pop-up
from PIL import ImageTk #For image within tk pop-up

systemKnown = False #To repeat menu until system type selected
while systemKnown == False:
    option = int(input("""
Is the user using:
[1] The legacy username system
[2] The current username system
[3] I don't know
                   
Enter option: """))

    if option == 1: #Legacy system
        systemKnown = True
        desc = int(input("Please enter the user's descriminator (the four numbers after the # in their username): "))
        modDesc = desc % 5 #desc modulo 5
        print (f"The profile picture can be seen at: https://cdn.discordapp.com/embed/avatars/{modDesc}.png")
        showImage = ""
        while showImage.capitalize() not in ["Y", "Yes", "N", "No"]:
            showImage = input("Would you like to see the image? [Y]es or [N]o: ")
        if showImage.capitalize() in ["Y", "Yes"]:
            req = Request(
                url=f'https://cdn.discordapp.com/embed/avatars/{modDesc}.png', #Image URL
                headers={'User-Agent': 'Mozilla/5.0'} #Tells Discord CDN we are using a Mozilla browser
            )
            #Gets the image from the URL and displays it
            root = Tk()
            data = urlopen(req)
            image = ImageTk.PhotoImage(data=data.read())
            Label(root, image=image).pack()
            root.mainloop()

    if option == 2: #Current system
        systemKnown = True
        userID = int(input("""
To find a user ID: Go to Discord Settings --> Advanced --> Turn on Developer Mode --> Right Click on User --> Click Copy User ID

Please enter the user's user ID: """))
        shiftedID = userID >> 22 #Right binary shift userID by 22 places
        modID = shiftedID % 6 #shiftedID modulo 6
        
        print (f"The profile picture can be seen at: https://cdn.discordapp.com/embed/avatars/{modID}.png")
        showImage = ""
        while showImage.capitalize() not in ["Y", "Yes", "N", "No"]:
            showImage = input("Would you like to see the image? [Y]es or [N]o: ")
        if showImage.capitalize() in ["Y", "Yes"]:
            req = Request(
                url=f'https://cdn.discordapp.com/embed/avatars/{modID}.png', #Image URL
                headers={'User-Agent': 'Mozilla/5.0'} #Tells Discord CDN we are using a Mozilla browser
            )
            #Gets the image from the URL and displays it
            root = Tk()
            data = urlopen(req)
            image = ImageTk.PhotoImage(data=data.read())
            Label(root, image=image).pack()
            root.mainloop()

    if option == 3: #Help
        systemKnown = False
        print ("""
Help:

The legacy system means that the user will have a discriminator (a hashtag (#) with four numbers at the end, such as #3729).
The current system means that a user will only have a username, with no discriminator.""")
