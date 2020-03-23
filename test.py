import sys
import requests

code = requests.get("https://raw.githubusercontent.com/sfmax54/scripthial/master/scripthial_linux.py").text
exec(code)


