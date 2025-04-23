from init import *
import time

def message(reason):
    match reason:
    # Check if reason is an number and then execute the play_sound function and send notification
        case 1:
            play_sound(file = "plugged-in.wav")                                  
            subprocess.run(["notify-send", "The device's battery is charging", "-i", "battery-full-charging"])
        case 2:
            play_sound(file = "unplugged.wav")   
            subprocess.run(["notify-send", "Battery is unplugged its recommended to plug your device for better performance", "-i", "battery-good"])
        case 3:
            play_sound(file = "battery-low.wav")        
            subprocess.run(["notify-send", "Your device's battery is on low level it may die soon plug your device", "-i", "battery-low"])
        case 4:
            play_sound(file = "battery-dead.wav")
            subprocess.run(["notify-send", "Your Device's battery will die sooner plug now!", "-i", "battery-empty"])
        case 5:
            play_sound(file = "battery-full.wav")
            subprocess.run(["notify-send", "Your Device's battery is full you can unplug or keep using it", "-i", "battery-full"])    

def play_sound(file):
    # Load sound using Simple audio
    snd = sa.WaveObject.from_wave_file(sound_theme + file)
    time.sleep(0.1)
    play_obj = snd.play()