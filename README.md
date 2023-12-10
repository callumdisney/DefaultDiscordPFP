# DefaultDiscordPFP

## What?
This program allows you to find the default profile picture for a Discord user. It then allows you to view this image online, or display it in a little window.

## Why?
These profile pictures are not just randomly assigned, as some may assume. They are actually worked out using a bit of mathematics. The method of working it out depends on whether you are using the current username format (the "[Pomelo system](https://discord.fandom.com/wiki/Pomelo)") or legacy username format (with [discriminators](https://discord.fandom.com/wiki/Discriminator)).

### Legacy System
To work out the default profile picture for an account on the legacy username system (a user with a discriminator, such as #3729), Discord takes that discriminator modulo[^1] 5. This number will be a number from 0–4, corresponding to a selection of four different profile pictures. These can be viewed at ```https://cdn.discordapp.com/embed/avatars/#.png```, replacing the ```#``` with the final calculated number.

![MergedImages](https://github.com/bigmancallum/DefaultDiscordPFP/assets/47284263/34d3eef8-f6c9-4b0b-bcd4-67134e6d22ef)

### Current System
To work out the default profile picture for an account on the current system (a user with no discriminator, just a plain username), Discord takes the user's unique user ID, performs a 22 place [binary shift](https://en.wikipedia.org/wiki/Binary_shift) on it, and takes that number modulo[^1] 6. This number will be a number from 0–5, corresponding to a selection of five different profile pictures. These can be viewed at ```https://cdn.discordapp.com/embed/avatars/#.png```, replacing the ```#``` with the final calculated number.

![MergedImages-](https://github.com/bigmancallum/DefaultDiscordPFP/assets/47284263/d56f6df5-64a6-4bf3-ba77-c84b2472f649)

## Footnotes
[^1]: [Modulo](https://en.wikipedia.org/wiki/Modulo) means to divide by and find the remainder.
