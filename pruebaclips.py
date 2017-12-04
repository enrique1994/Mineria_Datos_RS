import sys
import urllib
import re
import codecs
import json
from pattern.web import Twitter
import io

veces=0

s=open("training_marte.txt","w");

si=open("test_marte.txt","w");
engine = Twitter(license="LDC78c9PCsZfPFfadv5aHHlRK", language="en")

for j in range(50):
	for tweet in Twitter().search('#AguaEnMarte',start=1,count=100):
		if veces%5==0:
			m=tweet.text.encode('utf-8')
			
			si.write("El tweet:"+m+"\n")
			
		else:
			m=tweet.text.encode('utf-8')
			s.write("El tweet:"+m+"\n")
			
		veces+=1
		print veces
		


