# Programacion Bots
**First you have to use python 2.7**

Install Selenium because is a headless Webkit and eliminates the need for a graphical browser, tests run much faster.

This is what you have to do:

```sh
$ pip install selenium
```

Now we can use the package, let's look how works.

```py
from selenium import webdriver
```
to import 

You can change Firefox for PhantomJS() if you don't have firefox installed 

```py
driver = webdriver.PhantomJS()
```
#### When you run the code, a firefox window will open and you should see the outputted URL in the terminal 