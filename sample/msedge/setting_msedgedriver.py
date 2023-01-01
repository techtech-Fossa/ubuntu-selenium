#!/usr/bin/env python3

import os
import subprocess
import re

if __name__=='__main__':
    command = ['microsoft-edge','--version']
    res = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    l = str(res.stdout)
    ver = re.sub('[^0-9\.]','',l)
    link = f'https://msedgedriver.azureedge.net/{ver}/edgedriver_linux64.zip'
    os.system(f'wget {link}')
    os.system('unzip edgedriver_linux64.zip')
    os.system('sudo mv msedgedriver /usr/local/bin/')
