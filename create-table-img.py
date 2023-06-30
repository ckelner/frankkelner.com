#!/usr/bin/python3

import os

fileout = open("html-table.html", "w")

table = "<table>\n"
# specify the img directory path
path = "/Users/chris.kelner/Downloads/pop-pop"

# list files in img directory
files = os.listdir(path)
count = 0

for file in files:
    if count == 0:
        table += "  <tr>\n"
    table += "    <td>https://pop-pop.s3.us-east-1.amazonaws.com/{0}</td>\n".format(
        file
    )
    if count == 2:
        table += "  </tr>\n"
        count = 0
    else:
        count += 1

table += "  </tr>\n"
table += "</table>"

fileout.writelines(table)
fileout.close()
