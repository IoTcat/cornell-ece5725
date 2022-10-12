#!/bin/bash

gcc -Wall -pthread -o blink_v7 blink_v7.c -lpigpio -lrt
sudo killall pigpiod
sudo ./blink_v7
sudo pigpiod
