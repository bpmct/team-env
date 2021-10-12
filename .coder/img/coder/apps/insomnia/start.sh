#!/bin/bash

# start Insomnia app on the VNC desktop
DISPLAY=:90 insomnia&
# make it fullscreen 
sleep 2
DISPLAY=:90 xdotool key F11