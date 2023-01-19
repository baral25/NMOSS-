Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import webbrowser
import sys
kek = int(input('''What speed do you want to test:  
  
1) Continue to Website 
  
2) Terminate Program  
  
Your Choice: '''))
if kek == 1:
  webbrowser . open('https://pedantic-minsky-d0f88a.netlify.app/file_reader.html')
else:
  sys.exit()
  
SyntaxError: multiple statements found while compiling a single statement
>>> import webbrowser
import sys
kek = int(input('''What speed do you want to test:

1) Continue to Website

2) Terminate Program

Your Choice: '''))
if kek == 1:
  webbrowser . open('https://pedantic-minsky-d0f88a.netlify.app/file_reader.html')
else:
  sys.exit()
  
SyntaxError: multiple statements found while compiling a single statement
>>> 

import webbrowser
import sys

kek = int(input('''What speed do you want to test:  
  
1) Continue to Website 
  
2) Terminate Program  
  
Your Choice: '''))
if kek == 1:
  webbrowser . open('https://pedantic-minsky-d0f88a.netlify.app/file_reader.html')
else:
  sys.exit()