1. https://github.com/shadowciaw/cmput404_lab4
2. The page at 127.0.0.1:8000 shows "The install worked successfully! Congratulations!"
3. When navigating to /, it says Page not found and that empty path did not match any of the URLconf defined in mysite.urls. When navigating to /polls, it shows "Hello, world. You're at the polls index."
4. Migrations are how Django stores changes to models and database schema. (https://docs.djangoproject.com/en/3.1/intro/tutorial02/). Without migrations, changes to models will not be reflected in the database and therefore will not function as expected.
5. After logging in, we're taken to the Django administration page which contains the Site administration menu. There are options to edit authentication and authorization for groups and users (add or change), as well as edit polls for choices and questions (add or change). A recent changes module is also viewable.
6. At /polls/38/, I see a page with the text "You're looking at question 38." At /polls/38/results and /polls/38/vote, I see the pages with texts "You're looking at the results of question 38." and "You're voting on question 38." respectively. When using a string, a page not found error is returned. In urls.py, str instead of int would be used for the type of question ids.
7. Hardcoded urls into templates decrease reusability, and may cause vulnerabilities. Thus, it is bad practice.
8. Using Django's generic views saves time rewriting boiler plate code and minimizes errors due to it. You should use a generic view when required functionalities align with what generic view provides, and not when more work is needed to build atop of what generic view has.

=====

# lab 6

1. What are some ways you can deploy your code to Heroku?
2. A Procfile is "used to explicitly declare your application's process types and entry points." (https://devcenter.heroku.com/articles/django-app-configuration)
3. What is the link to your deployed application (on herokuapps)?
