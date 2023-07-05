# DeafultDiscordPFP

## What?
This program allows you to find the default profile picture for a Discord user.

## Why?
These profile pictures are not just randomly assigned, as some may assume. They are actually worked out using a bit of mathematics. The method of working it out depends on whether you are using the current username format (the "[Pomelo system](https://discord.fandom.com/wiki/Pomelo)") or legacy username format (with [discriminators](https://discord.fandom.com/wiki/Discriminator)).

### Legacy System
To work out the deafult profile picture for an account on the legacy username system (a user with a discriminator, such as #3729), Discord takes that discriminator, divides it by 5, and finds the remainder (doing this is also known as using the [modulo](https://en.wikipedia.org/wiki/Modulo) operator). This number is will be a number 0-4, corresponding to a selection of four different profile pictures. These can be viewed at ```https://cdn.discordapp.com/embed/avatars/#.png```, replacing the ```#``` with the final calculated number.

### Current System
To work out the deafult profile picture for an account on the current system (a user witnh no discriminator, just a plain username), Discord takes the user's unique user ID, does a 
