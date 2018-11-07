# -*- coding: utf-8 -*-

import subprocess
import os
import hashlib

def hash_file(path, block_size=4096):
    hash_string = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            hash_string.update(chunk)
    return hash_string.hexdigest()
icons = os.listdir("../img")
for (dirpath, dirnames, files) in os.walk("../exámenes"):
    for filename in files:
        fpath = None
        if filename[-4:] in [".pdf", ".PDF"]:
        	fpath = dirpath+"/"+filename+'[0]'
        elif filename[-4:] in [".png", ".PNG", ".jpg", ".JPG", "JPEG", "jpeg"]:
        	fpath = dirpath+"/"+filename
        if( fpath != None):
        	md5 = hash_file(dirpath+"/"+filename)
                if not str(md5)+".jpg" in icons:
        	        subprocess.call(['gm', 'convert','-sampling-factor', '4:2:0', '-colorspace', 'RGB', '-strip', '-crop', '100x50%', '-resize', '315x384','-quality','50', fpath, "../img/"+md5+".jpg"])
