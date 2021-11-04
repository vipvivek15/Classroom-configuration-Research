# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 06:32:39 2021

@author: vipvi
"""

# import re
# def get_text(path):
#         pattern = '(\d{3}+\s+^[p|P]+[s|S]$)|(^[E|e]+[N|n]$)|(^[E|e]+[S|s]$)|(^[P|p]+[N|n]$)|(^[M|m]+[S|s]$)|(^[P|p]+[R|r]$)'
#         result = re.compile(pattern)
#         text = []
#         with open(path,mode='rb',encoding='utf-8') as f:
#             contents = f.read()
#             matches = result.finditer(contents)
#             for match in matches:
#                 text.append(match.group())
#             return text  
# rgx = get_text('sample.txt')
# words = " ".join(rgx)
# try:
#     f = open('regex.txt',mode='w')
#     f.write(words)
# finally:
#     f.close()

#necessary libraries to import
import PyPDF2
import re


#get all text from pdf
try:
    f = open('sample.pdf',mode='rb') 
    pdfReader = PyPDF2.PdfFileReader(f)
    numofpages = pdfReader.getNumPages()
    text = ""
    for i in range(0,numofpages):
        pageObject = pdfReader.getPage(i)
        text+= pageObject.extractText()
finally:
    f.close()


#patterns to identify
w = r'\bExamination|Midterms|Paper|Points'
n = r'\d{3}|\d{2}|\d{1}'
wr = re.compile(w)
nr = re.compile(n)
wm = wr.finditer(text)
nm = nr.finditer(text)
matches = zip(wm,nm)
rgx = []
for a,b in matches:
    rgx.append(a.group())
    rgx.append(b.group())
    
words = " ".join(rgx)
try:
    f = open('regex.txt',mode='w') 
    f.write(words)    
finally:
    f.close()
    
