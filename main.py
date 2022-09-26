import re 

textfile = open('fb_sub.csv' , 'r')
filetext = textfile.read()

match = re.search(r'\w*\sINC\b',filetext)[0]

fileout = open("company.txt" , "w")

fileout.write(match)



