Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 125
>>> y = 62
>>> float(x/y)
2.0161290322580645
>>> float(x/y)*60
120.96774193548387
>>> float(x/y)*60+46
166.96774193548387
>>> float(x/y)*60+45
165.96774193548387
>>> a = 256
>>> b = 70
>>> float(a/b)*60
219.42857142857142
>>> float(x/y)*60+45 + float(a/b)*60
385.3963133640553
>>> (float(x/y)*60+45 + float(a/b)*60)/60
6.4232718894009215
>>> c = 6
>>> float(c+(float(x/y)*60+45 + float(a/b)*60)/60)
12.423271889400922
>>> 