#!/usr/bin/env bash


# firefox
## add-apt-repository を使用するための下準備
## cf. https://kazuhira-r.hatenablog.com/entry/20160116/1452933387
sudo apt install -y software-properties-common

## cf. https://chatnoirlibre.com/ubuntu-22-04-lts-mozilla-firefox-deb/
sudo add-apt-repository -y ppa:mozillateam/ppa <<EOF
\n
EOF

cat <<EOF > mozillateamppa
Package: firefox*
Pin: release o=LP-PPA-mozillateam
Pin-Priority: 1001
EOF
sudo mv mozillateamppa /etc/apt/preferences.d/mozillateamppa
sudo apt -y update
sudo apt install -y firefox

# geckodriver
pip install requests
pip install beautifulsoup4
python3 setting_geckodriver.py

# selenium library
pip install selenium
