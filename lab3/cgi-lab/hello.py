#!/usr/bin/env python3
print("Content-type:text/html\r\n\r\n")
print("<title>Testing CGI</title>")

# Note: questions 1-3 are from lab code given by Hareeme Sahar

# QUESTION 1
import json, os
env_vars = json.dumps(dict(os.environ))
print(env_vars)


# QUESTION 2
print("<hr>")
for param in os.environ.keys():
  if param == "QUERY_STRING":
    print("<b>{}</b>: {}<br>".format(param, os.environ[param]))

# QUESTION 3
print("<hr>")
for param in os.environ.keys():
  if param == "HTTP_USER_AGENT":
    print("<b>{}</b>: {}<br>".format(param, os.environ[param]))