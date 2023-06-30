#!/usr/bin/python3

import os

fileout = open("html-table.html", "w")

html = ""
# specify the img directory path
path = "/Users/chris.kelner/Downloads/pop-pop"

# list files in img directory
files = os.listdir(path)

for file in files:
    html += '<img src="https://pop-pop.s3.us-east-1.amazonaws.com/{0}"/><br/>\n'.format(
        file
    )

fileout.writelines(html)
fileout.close()
