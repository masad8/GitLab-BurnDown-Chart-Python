import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import csv
import os

GroupID = '--groupid--' #Replace --groupid-- with gitlab group or project id
GitlabPrivateToken = '--gitlabprivatetoken' #Replace --gitlabprivatetoken with personal access token from https://gitlab.com/profile/personal_access_tokens

cmd1 = 'curl --header "PRIVATE-TOKEN: ' + GitlabPrivateToken + '" "https://gitlab.com/api/v4/groups/' + GroupID + '/issues?labels=Sprint,Task,ToDo" > issues1.json'
cmd2 = 'curl --header "PRIVATE-TOKEN: ' + GitlabPrivateToken + '" "https://gitlab.com/api/v4/groups/' + GroupID + '/issues?labels=Sprint,Task,InProgress" > issues2.json'

#If you need project issues, use https://gitlab.com/api/v4/projects/ in the above commands along with corresponding ProjectID.

os.system(cmd1)
os.system(cmd2)

total_time_estimate=0

with open('issues1.json') as json_file: 
    data = json.load(json_file)
for i in range(len(data)):
  total_time_estimate+= data[i]['time_stats']['time_estimate']
with open('issues2.json') as json_file: 
    data = json.load(json_file)
for i in range(len(data)):
  total_time_estimate+= data[i]['time_stats']['time_estimate']

datetoday =  datetime.strftime(datetime.now() - timedelta(0), '%Y-%m-%d')
fields=[datetoday,int(total_time_estimate/3600)]
with open(r'issues.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

reader = csv.reader(open('issues.csv', 'r'))
d = {}
for row in reader:
   k, v = row
   d[k] = v

chart_plot_days = 14

lists = sorted(d.items())
lists = lists[-chart_plot_days:]
x, y = zip(*lists)
x = list(x)
y = [int(i) for i in y]
plt.clf()
plt.plot(x,y)
plt.xlabel('Date')
plt.ylabel('Estimated Hours')
plt.savefig('burndown.png')