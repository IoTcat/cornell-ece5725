#!/bin/bash
#
# Script Name : start_video.sh
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
#
# Description: Start the python video_contro script
# and launch the mplayer so that the buttons on the 
# PiTFT can control the behavior of the video playing
# on the PiTFT screen.

# Start video_control python script in the background
if [ $# -gt 0 ];
then 
    /usr/bin/python3 $1 &
fi
# Start mplayer in the foreground
sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb0 mplayer -input file=test_fifo -vo sdl -framedrop bigbuckbunny320p.mp4
