from __future__ import print_function
import re
import config
from bs4 import BeautifulSoup as bs
import requests
import tkinter as tk
import ast
from Tkinter import *
info = ""
def start():
	print ("Evalution going on..")
	global info
	track = 0
	repos = open("repo.json","r")
	JSONdata = ast.literal_eval(repos.read())
	repos.close()
	progress = 0;
	for obj in JSONdata:
		track+=1
		link = "https://github.com/"+obj["mentor"]+"/"+obj["project"]+"/issues?q=is%3Apr+is%3Aclosed"
		try:
			r = requests.get(link)
		except:
			print ("Check your Internet Connection.")
			exit()
		soup = bs(r.content,"html.parser")
		contributions = soup.find_all("div",{"class":"float-left col-9 p-2 lh-condensed"})
		if track is len(JSONdata):
			progress = 100;
		print(str(progress)+"%..........")
		for cont in contributions:
			cont = re.sub(r'\s+'," ",str(cont))
			cont = re.sub(r'<(.*?)>',"",str(cont))
			if obj["mentor"] not in str(cont):
				info = info + str(cont) + "\n"
		content.config(text=str(info))
		progress += 100/len(JSONdata)
		info += "\n"

window = tk.Tk()
scroll = tk.Scrollbar(window)

window.title("Season of Code (Evaluator)")

window.geometry("800x600")

# LABEL
title = tk.Label(text="Welcome to DAWoC and welcome to SoC Evaluator",font=("Times New Roman", 20))
title.grid(column=1,row=0)

content = tk.Label(text="Please Wait")
content.grid(column=0,row=2)
window.after(1000,start)

window.mainloop()
