import MySQLdb

uid = 30;
my_list = []
counter = 1

conn = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")

c = conn.cursor()
tempStr = ""

c.execute("Select status_p FROM getInfoInsta where uuid = 30")
results = c.fetchall()
for row in results:
	status = row[0]
#	print status
	
t = row[0]
print t

conns = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")

cs = conns.cursor()
tempStr = ""

cs.execute("Select pic FROM getInfoInsta where uuid = 30")
result = cs.fetchall()
for row in result:
	status = row[0]
#	print status
	
s = row[0]

s = s.split(' ');

for i in range(len(s)):
	print s[i]

conn.close()
conns.close()	
