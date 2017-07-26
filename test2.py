# bin/user/python

import urllib3

url ='http://urllib3.readthedocs.org/'
http_pool = urllib3.connection_from_url(url)
r = http_pool.urlopen('GET', url)

print (r.data)