#!/usr/bin/env python3
import secret
import cgi
from os import environ
from templates import login_page, secret_page, after_login_incorrect
from http.cookies import SimpleCookie 

cookie = SimpleCookie(environ['HTTP_COOKIE'])
cookie_username = None
cookie_password = None

# QUESTION 4
s = cgi.FieldStorage()
un = s.getfirst("username")
pw = s.getfirst("password")
# check if existing cookie w/ un + pw exists in browser

if cookie.get('username'):
    cookie_username = cookie.get('username').value
if cookie.get('password'):
    cookie_password = cookie.get('password').value

# skip login if already 
if cookie_username == secret.username and cookie_password == secret.password:
    un = cookie_username
    pw = cookie_password


# QUESTION 5
print("Content-type:text/html")

if un == secret.username and pw == secret.password:
  print("Set-Cookie:username={};".format(secret.username))
  print("Set-Cookie:password={};".format(secret.password))
  print()

# if not logged in, show login; elif incorrect print incorrect; else secret
if not cookie_username and not cookie_password:
    print(login_page())
elif not un and not pw:
    print(after_login_incorrect())
else:
    print(secret_page(un, pw))