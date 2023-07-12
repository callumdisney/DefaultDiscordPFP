# DeafultDiscordPFP

## What?
This program allows you to find the default profile picture for a Discord user.

## Why?
These profile pictures are not just randomly assigned, as some may assume. They are actually worked out using a bit of mathematics. The method of working it out depends on whether you are using the current username format (the "[Pomelo system](https://discord.fandom.com/wiki/Pomelo)") or legacy username format (with [discriminators](https://discord.fandom.com/wiki/Discriminator)).

### Legacy System
To work out the deafult profile picture for an account on the legacy username system (a user with a discriminator, such as #3729), Discord takes that discriminator modulo[^1] 5. This number will be a number from 0-4, corresponding to a selection of four different profile pictures. These can be viewed at ```https://cdn.discordapp.com/embed/avatars/#.png```, replacing the ```#``` with the final calculated number.

IMAGE OF PFPs HERE

### Current System
To work out the deafult profile picture for an account on the current system (a user witnh no discriminator, just a plain username), Discord takes the user's unique user ID modulo[^1] 6. This number will be a number from 0-5, corresponding to a selection of five different profile pictures. These can be viewed at ```https://cdn.discordapp.com/embed/avatars/#.png```, replacing the ```#``` with the final calculated number.

IMAGE OF PFPS HERE

## Footnotes
[^1]: [Modulo](https://en.wikipedia.org/wiki/Modulo) means to divide by and find the remainder.
