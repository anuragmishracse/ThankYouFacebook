import requests


print "Lets start"
url="https://graph.facebook.com/744150888971799/feed"

token="Access_Token"				#Your access token here.

payload={'access_token': token }
r=requests.get(url,params=payload)

data=r.json()['data']
c=0
date_field="2014-11-08"				#Put the starting date
for i in data:
	try:
		time_of_creation=i['created_time']
		date = str(time_of_creation)[0:10]
		
		if(date >= date_field):		
			c+=1
			post_id=i['id']
			f=i['from']
			from_id=f['id']
			from_name=f['name']
			
			posturl="https://graph.facebook.com/"+str(post_id)+"/comments"
			payload={'access_token':token,'message' : "Thank You @"+str(from_name)+" :D (y)"}
			p=requests.post(posturl,data=payload)
			if(p.status_code == 200):
				print "Commented on \"",from_name,"'s\" post created on : ",time_of_creation	
			else:
				print "Comment FAILED on \"",from_name,"'s\" post created on : ",time_of_creation
	
	except:
		print "THERE WAS AN EXCEPTION"

print "No of comments : ",c
