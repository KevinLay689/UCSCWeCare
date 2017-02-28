
import MySQLdb
import time
import json
import urllib2
import urllib

#conn = MySQLdb.connect("169.233.202.215", "amit", "mediumnight", "pulvid_schema")
conn = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")
c = conn.cursor()

class listener():
    idd = 30
    url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=196701503.1c6771e.08d31360dd0b443c886e961e22f865f0"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    str1final =""
    str2final = ""
    for i in range(20):
        s_temp = ""
        str1 = str(data["data"][i]["images"]["standard_resolution"]["url"])
        str2 = data["data"][i]["caption"]["text"];
        
        for i in range(0,len(str2)):
            if(ord(str2[i])<=128):
                s_temp += str2[i]
            
        str1final += str1
        s_temp += str(s_temp)   
        str2final += s_temp
        #print s_temp
        #print type(s_temp)
        str1final += " "
        str2final += " "
        #print("id: " + str(idd))
    #print(str1final)
    #print(str2final)
    c.execute("INSERT INTO getInfoInsta (pic,status_p, timestamp_p,uuid,username) VALUES (%s,%s,%s,%s,%s)",(str1final,str2final,"00:40", idd, "Kevingotlayed"))
    idd+=1
    conn.commit()

