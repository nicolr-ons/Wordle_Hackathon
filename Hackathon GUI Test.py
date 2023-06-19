# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:20:29 2023

@author: pikes
"""
#Import packages
import pandas as pd
import tkinter as tk

#Import dataset
words = pd.read_csv("C:/Users/pikes/Downloads/valid_solutions.csv", names = ["WORD"])

#Choose word and break it down into list for comparison
#word_selection = words.sample(n=1)
word_selection = "hello"
wl1 = word_selection[0]
wl2 = word_selection[1]
wl3 = word_selection[2]
wl4 = word_selection[3]
wl5 = word_selection[4]

#Create gameplay window
window = tk.Tk()
window.geometry("200x500")

#User submitted word
text = tk.Entry(window, width = 20)
text.focus_set()
text.grid(row = 0, column = 0)


def check_letter(sl, wl, r, c):
    if sl not in word_selection:
        tk.Label(window, text = sl, bg = "white").place(x = c, y = r)
    elif sl == wl:
        tk.Label(window, text = sl, bg = "#90ee90").place(x = c, y = r)
    else:
        tk.Label(window, text = sl, bg = "#FFD580").place(x = c, y = r)
        return
    
#Word test function
def word_test():
    submitted_word = text.get()
    sl1 = submitted_word[0]
    sl2 = submitted_word[1]
    sl3 = submitted_word[2]
    sl4 = submitted_word[3]
    sl5 = submitted_word[4]
    check_letter(sl1, wl1, 30, 90)
    check_letter(sl2, wl2, 30, 100)
    check_letter(sl3, wl3, 30, 110)
    check_letter(sl4, wl4, 30, 120)
    check_letter(sl5, wl5, 30, 130)
    return

#Submit button 
sbmt_btn = tk.Button(window, text = "Submit", command = word_test).grid(row = 0, column = 1)

window.mainloop()


    
    