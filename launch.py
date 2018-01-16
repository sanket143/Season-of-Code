from __future__ import print_function
import re
import config
from bs4 import BeautifulSoup as bs
import requests
import ast
import string
import tkinter as tk
info = ""
def start():
	global info
	repos = open("repo.json","r")
	JSONdata = ast.literal_eval(repos.read())
	repos.close()

	for obj in JSONdata:
		link = "https://github.com/"+obj["mentor"]+"/"+obj["project"]+"/issues?q=is%3Apr+is%3Aclosed"
		r = requests.get(link)
		soup = bs(r.content,"html.parser")
		contributions = soup.find_all("div",{"class":"float-left col-9 p-2 lh-condensed"})
		print ("Mentor:",obj["mentor"],"\t",obj["project"])
		for cont in contributions:
			cont = re.sub(r'\s+'," ",str(cont))
			cont = (re.sub(r'<(.*?)>',"",str(cont)))
			if obj["mentor"] not in str(cont):
				info = info + str(cont) + "\n"
		content.config(text=str(info))
		info += "\n"

window = tk.Tk()

window.title("Season of Code (Evaluator)")

window.geometry("800x600")

# LABEL
title = tk.Label(text="Welcome to DAWoC and welcome to SoC Evaluator",font=("Times New Roman", 20))
title.grid(column=1,row=0)

content = tk.Label(text="Please Wait")
content.grid(column=1,row=2)
window.after(1000,start)

window.mainloop()
