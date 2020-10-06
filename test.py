import re as re
s = "fgbadbgjkerjg3478t54fjk$?kgekleg"
print(re.split('[^0-9a-z]', s))