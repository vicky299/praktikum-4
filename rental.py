Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=6
>>> y=23
>>> int(y-x)
17
>>> y=23
>>> m= 50/60
>>> int(int(y-x)-12)*10000
50000
>>> int(m*10000)
8333
>>> 200000+int(int(y-x)-12)*10000+int(m*10000)
258333
>>> 