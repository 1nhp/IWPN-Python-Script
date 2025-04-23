#bin/sh

progress=1
local_dir=~/.local/bin/iwpn
files=99

create_copying_message () {
  clear
  echo "Copying files... [$progress/$files]"
}

cp1 () {
  cp -r $1 $2 $3 2>/dev/null
}

for n in $(seq 1 $files) 
  do
    if [ $? -eq 0 ]; then
      sleep 0.01
      create_copying_message
      ((progress+=1))
  else
      echo "Command Failed"
    fi
done

mkdir data $local_dir

while true ;do
  yay -Suy python-simpleaudio python-psutil python dunst
  cp1 data $local_dir
  cp1 scripts $local_dir
  cp1 config.ini $local_dir
  cp1 init.py $local_dir
  clear
  echo Done!
  break
done