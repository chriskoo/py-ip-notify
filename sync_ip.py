import httplib,urllib2
import re


def sendEmail(subject, body):
    fromaddr = 'sharrajeshspam@gmail.com'
    toaddrs  = ['sharrajesh@gmail.com', 'sharrajesh@hotmail.com']

    username = 'sharrajeshspam@gmail.com'
    password = 'YourPassword'

    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username,password)

    msg = 'Subject: %s\n\n%s' % (subject, body)

    for toad in toaddrs:
        server.sendmail(fromaddr, toad, msg)  
    server.quit()


# connect to server
conn = httplib.HTTPConnection("www.ipchicken.com", 80, False)  

# send request 
conn.request('GET', '/', headers = {"Host": "www.ipchicken.com",  
                                   "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",  
                                  "Accept": "text/html"})  

# get response
result=conn.getresponse() 
#print "Response:"+

# get status
httpStatus=result.status  
print("HTTP STATUS:%d" % (httpStatus ))

# get page content
content = result.read()

#print content
posStart= content.index("<body");
posEnd = content.index("Add to Favorites")
print "EndPOS:%d" % ( posEnd)
focusContent = content[posStart:posEnd]
print "FocusContent:%s" % focusContent 

pt= re.compile( r"(\d+.\d+.\d+.\d+)", re.MULTILINE)
focusContent="my ip is 127.0.0.1 haha"
match = pt.match(focusContent)
#match = re.match(r"(\d)", re.MULTILINE)
if match:
	print "MY IP: %s" % match.group()
else:
	print "Cannot match my IP"
conn.close()

