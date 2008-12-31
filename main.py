#! user/bin/python3
#author : zal-byte ( github )

from tkinter import *
from functools import *

class GUI(object):
	def __init__(self):

		self.plain = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.cipher = self.toCipher()

		self.var = ""

		self.window = Tk()
		self.window.geometry("500x100")
		self.window.title("Caesar Encryption")
		self.window.resizable(0,0)

		self.window.columnconfigure(0,weight=1)
		self.window.columnconfigure(1,weight=3)

		self.label = Label(self.window, text="Message").grid(row=0,column=0,padx=5,pady=5,sticky="W")
		self.entry = Entry(self.window)
		self.entry.insert(0, "Message here")
		self.entry.grid(row=0,column=1,padx=6,pady=5,sticky="WE")
		self.entry["textvariable"] = self.var

		self.process = partial(self.encrypt, self.entry)
		self.decrypts = partial(self.decrypt, self.entry)

		self.button = Button(self.window, text="Encrypt", command=self.process)
		self.button.grid(row=1,column=0,padx=5,pady=5, sticky="W")

		self.button1 = Button(self.window, text="Decrypt", command=self.decrypts)
		self.button1.grid(row=1, column=1, padx=5, pady=5, sticky="W")
		

		self.entry1 = Entry(self.window)
		self.entry1.grid(row=2,column=0,padx=6,pady=5, sticky="WE",columnspan=2)

		self.window.mainloop()


	def toCipher(self):
		res = ""
		for i in range(len(self.plain)):
			res += self.plain[i - 7]
		return res

	def encrypt(self, msg):
		res = ""
		for i in range(len(msg.get())):
			for o in range(len(self.plain)):
				if msg.get()[i] == self.plain[o]:
					res += self.cipher[o]
			if msg.get()[i] == " ":
				res += " "
		self.entry1.delete(0,'end')
		self.entry1.insert(0,res)

	def decrypt(self, encrypted):
		res=""

		for i in range(len(encrypted.get())):
			for o in range(len(self.cipher)):
				if encrypted.get()[i] == self.cipher[o]:
					res += self.plain[o]
			if encrypted.get()[i] == " ":
				res += " "
		self.entry1.delete(0, 'end')
		self.entry1.insert(0, res)
		return res

app = GUI()