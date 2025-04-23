with open("config.ini", "r") as f:
    lines = f.readlines()
    sound_theme_name = lines[8].strip()
    low_battery_level = lines[16].strip()
    full_battery_level = lines[19].strip()
    empty_battery_level = lines[22].strip()

sound_theme = "data/sound_themes/" + str(sound_theme_name) + "/"
last_status = 0
last_percentage = 0