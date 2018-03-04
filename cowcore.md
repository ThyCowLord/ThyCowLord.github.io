### [Home](https://thycowlord.github.io)

# CowCore

## What is it?
It's a simple engine for building games. It's mainly set towards RPGs. 

## How do I get it?
It's not open-source, unfortunately. 
I personally use it to create games, so.... yeah.
If you want it, ya gotta ask. 


## Usage

### Initializing events
Before the event code, write this:

> cowcore.events.[event] = False

### Required at the end of sequence

> cowcore.events.[event] = True

### Coding events (aka Sequences)

if cowcore.events.[event] == False:
  [code]
  cowcore.events.[event] = True
  all()

### Recommended after each sequence
To check HP, Level, and all that, after each sequence run:

> cowcore.all()

### Changing player stats:

> cowcore.player.[stat] = [newstat]

Available stats: hp, xp, lv, dmg, arm, money

### Animated text

> cowcore.delay_print("Hello world!")

### Saving

> cowcore.save()

This is auto-activated by the all() sequence.

### Loading

> cowcore.load()

### Dying

> cowcore.die()

This is auto-activated by the all() sequence if the HP is 0 or below.

### Leveling up
Normally, you need 10 XP to level up. To bypass that (e.g Cheat Codes) you can do

> cowcore.player.lv = [level]

