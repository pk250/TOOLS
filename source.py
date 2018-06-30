# coding:utf8
#!/usr/bin/python

import requests

r=requests.post('http://59.63.178.44:90/ncee/temptotal?rnd=0.8068821368636329&StudentNo=18360703150019&SFZH4W=4815')
print(r.text)


