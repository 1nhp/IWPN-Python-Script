<p align="center">
  <img width="160" src="iwpn-icon.svg">
  <p align="center" style="color:rgb(170, 170, 170);"><i>Icon made by me</i></p>
  <hr>
</p>

### IWPN 
Stands For, Incredibly Lightweight Power Notify is my first ever python script, / project i've been working on, its a Power Notify system, script written in python, with only 66 lines of code!


# Showcase
<video src="iwpn-showcase.mp4" width="700" height="240" controls autoplay>
</video>

# Features

- Easy to install!
- Little to no cpu usage (tested)!
- Executable is only 8.6mb!
- Uses dunst to show notifications!
- Plays sound effect on notifications!
- An sound theming system now you can change sounds to whatever theme you like changed in config file!
- Can change battery level threshold in config file!

> # NOTE 1
  >Copyrighted sound themes such as Sonic, that was in the source code and windows 11, WILL not be included because it is not free for use, if you, want to install copyrighted themes go to my themes, repository to download and install themes.
  > # NOTE 2
  >See for theming instructions.

## Also See: [FAQ](Faq.md) for commonly asked questions and dont try to report already answered ones in issues!

# Installation

### 1 Run this command in your terminal
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/1nhp/IWPN-Python-Script/refs/heads/release/install.sh)"

### 2 Add the script to autostart in dwm at .local/dwm/autostart.sh for now
    python ~/.local/bin/iwpn/init.py
### or just execute it
    python ~/.local/bin/iwpn/init.py
  > # NOTE
  > I may provide making the script autostart at boot for other wms aswell


# Istalling Sound Themes

### 1 Download the zip file of the theme in my themes repository

### My themes repository link is ![] Here!

### 2 Open it with preferred archiving program xarchiver in my case

### 3 Extract the theme folder to ~./local/bin/ipwn/data/sound_themes/

# Making Sound themes

bca im too lazy to make an tutorial on it for not i'll make an tutorial on that later!

# Roadmap

- Custom icons for battery for dunst notification daemon
- Make version for Windows
- Make version For Android (someday not soon!)
- Try to adopt for Linux basis usage
- Be able to play sounds on different speaker e.g laptop speaker while it doesnt play on the headphones