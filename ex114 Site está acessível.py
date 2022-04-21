import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.sapo.pt/')
except urllib.request.URLError:
    print('\033[31mO site do sapinho está OFF\033[m')
else:
    print('\033[33mO site do sapinho está ONLINE\033[m')
