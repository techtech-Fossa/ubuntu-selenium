#!/usr/bin/env bash

# chrome
sudo apt -y update
sudo apt install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
sudo apt install -y -f

# chromedriver
pip install chromedriver-autoinstaller
python3 setting_chromedriver.py

# selenium library
pip install selenium