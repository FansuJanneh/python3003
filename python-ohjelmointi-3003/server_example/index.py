#!/usr/bin/python3

import os  # Ympäristömuuttujat
import cgi
import cgitb

cgitb.enable()  # Tuotantokäytössä tätä ei enabloida

print('Content-type: text/html; charset=utf-8')

htmlHeader = '''
<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="utf-8">
<title>Webbisivu</title>
</head>
<body>
'''

htmlFooter = '''
</body>
</html>
'''


def printPage(page):
    if page == 2 or page == 3:
        print("Sivu", page, sep=" ")
        print('''
        <br>
        <a href="?page=1">Takaisin etusivulle</a>
        ''')
    else:
        print('''
      <ul>
         <li><a href="?page=2">Sivu 2</a></li>
         <li><a href="?page=3">Sivu 3</a></li>
         <li><a href="jsonPage.py">JSON Page</a></li>
      </ul>
      ''')


httpMethod = os.environ["REQUEST_METHOD"]

data = cgi.FieldStorage()

try:
    page = int(data.getvalue("page", default=1))
except ValueError:
    page = 1


print(htmlHeader)
print(httpMethod)
print("<br>")
printPage(page)
print(htmlFooter)
