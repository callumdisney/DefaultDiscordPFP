# DeafultDiscordPFP

## What?
This program allows you to find the default profile picture for a Discord user.

## Why?
These profile pictures are not just randomly assigned, as some may assume. They are actually worked out using a bit of mathematics. The method of working it out depends on whether you are using the current username format (the "[Pomelo system](https://discord.fandom.com/wiki/Pomelo)") or legacy username format (with [discriminators](https://discord.fandom.com/wiki/Discriminator)).

### Legacy System
To work out the default profile picture for an account on the legacy username system (a user with a discriminator, such as #3729), Discord takes that discriminator modulo[^1] 5. This number will be a number from 0-4, corresponding to a selection of four different profile pictures. These can be viewed at ```https://cdn.discordapp.com/embed/avatars/#.png```, replacing the ```#``` with the final calculated number.

![discordPFPs0-4](https://github.com/bigmancallum/DeafultDiscordPFP/assets/47284263/8411604f-c18d-4e86-912e-e52ac7a7acb8)

### Current System
To work out the default profile picture for an account on the current system (a user with no discriminator, just a plain username), Discord takes the user's unique user ID modulo[^1] 6. This number will be a number from 0-5, corresponding to a selection of five different profile pictures. These can be viewed at ```https://cdn.discordapp.com/embed/avatars/#.png```, replacing the ```#``` with the final calculated number.

![discordPFPs0-5](https://github.com/bigmancallum/DeafultDiscordPFP/assets/47284263/58917ec9-3a50-4b43-a3fe-0b0cb0f3a02c)

## Footnotes
[^1]: [Modulo](https://en.wikipedia.org/wiki/Modulo) means to divide by and find the remainder.
