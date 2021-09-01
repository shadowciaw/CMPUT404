import requests

print(requests.__version__)
response = requests.get('http://google.com')

# download itself from github and print source code
response = requests.get('https://raw.githubusercontent.com/shadowciaw/CMPUT404/main/lab1/python_script.py?token=AKJ443XF5PPXZ76NKMNON4LBHE5Z4')
print(response.text)