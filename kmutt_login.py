import urllib
import urllib2
import getpass

url_login = "https://isaaclogin.kmutt.ac.th/radius.demo.php"
url_aup = "https://isaaclogin.kmutt.ac.th/aup.php"
url_pre = "https://isaaclogin.kmutt.ac.th/pre_addobject.php"
url_detect = "https://isaaclogin.kmutt.ac.th/detectBrowserObject.php"
url_add = "https://isaaclogin.kmutt.ac.th/addobjectfx.php"

usr = raw_input("Student ID : ")
pwd = getpass.getpass("Password : ")

value = { "user":usr, "pass":pwd}
data = urllib.urlencode(value)

req = urllib2.Request(url_login,data)
res = urllib2.urlopen(req)
cookie = res.headers.get('Set-Cookie')

html = res.read()

if 'addobjectfx.php' in html:
	req = urllib2.Request(url_add)
	req.add_header('cookie',cookie)
	res = urllib2.urlopen(req)
	print(res.read())
elif 'aup.php' in html:
	print("Authenticating...")
	req = urllib2.Request(url_aup)
	req.add_header('cookie',cookie)
	res = urllib2.urlopen(req)
	print("Adding your IP address to the system...")	
	req = urllib2.Request(url_pre)
	req.add_header('cookie',cookie)
	res = urllib2.urlopen(req)
	req = urllib2.Request(url_detect)
	req.add_header('cookie',cookie)
	res = urllib2.urlopen(req)
	req = urllib2.Request(url_add)
	req.add_header('cookie',cookie)
	res = urllib2.urlopen(req)
	print("Success")	
else:
	print("Access Denied!")


