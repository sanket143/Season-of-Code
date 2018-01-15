import re
import config
from bs4 import BeautifulSoup as bs
import requests
import ast
import string
import tkinter as tk
def innerHTML(element):
    return element.decode_contents(formatter="html")

repos = open("repo.json","r")
JSONdata = ast.literal_eval(repos.read())
repos.close()

for repositories in JSONdata:
	link = "https://github.com/"+repositories+"/"+JSONdata[repositories]+"/issues?q=is%3Apr+is%3Aclosed"
	#/harshvasoya008/Game_of_Cards/issues?q=is%3Apr+is%3Aclosed
	r = requests.get(link)
	soup = bs(r.content,"html.parser")
	contributions = soup.find_all("div",{"class":"float-left col-9 p-2 lh-condensed"})
	for cont in contributions:
		dummy = innerHTML(cont)
		print string.replace(dummy,r'<(.*?)>',"")



	

