def menu():
    option = input("""
    Is the user using:
    [1] The legacy username system
    [2] 
    """)

userID = int(input("User ID: "))

shiftedID = userID >> 22 #Right binary shift userID by 22 places
modID = shiftedID % 6 #shiftedID modulo 6

print (f"PFP: https://cdn.discordapp.com/embed/avatars/{modID}.png")