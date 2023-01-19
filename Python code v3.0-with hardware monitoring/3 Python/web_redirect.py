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

