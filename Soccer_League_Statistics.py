#----------------------------------------------------------------------
#	
# Evan Urquhart - 100554128
#
# Auth Token =>  e6c83dbc0d254be9a411b2a4ecdf5fd3
#
#----------------------------------------------------------------------


import http.client
import json
import csv
import os

#create a directory for the Data 
if not os.path.exists('Data'):
	os.makedirs('Data')

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'e6c83dbc0d254be9a411b2a4ecdf5fd3', 'X-Response-Control': 'minified' }
#get list of leagues
connection.request('GET', '/v1/competitions', None, headers )
response1 = json.loads(connection.getresponse().read().decode())

#open/create a .csv file to store the information for the leagues
myFile = open('Data/leaguesTOC.csv', 'w+', newline='')
with myFile:
	fields1 = ['caption', 'numberOfTeams', 'lastUpdated', 'currentMatchday', 'year', 'id', 'league', 'numberOfGames', 'numberOfMatchdays']
	writer1 = csv.DictWriter(myFile, fieldnames=fields1)	
	writer1.writeheader()
	writer1.writerows(response1)
	
#create a list of all league ids 	
games = [];
for i in response1:
	games.append(i['id'])
	if not os.path.exists('Data/' + str(i['id'])):
		os.makedirs('Data/' + str(i['id']))

for g in games:
	#get league table for a particular league
	connection.request('GET', '/v1/competitions/'+str(g)+'/leagueTable', None, headers )
	response2 = json.loads(connection.getresponse().read().decode())
	
	#open/create a .csv file for the league table
	leagueTable = open('Data/' + str(g)+'/league_Table_'+str(g)+'.csv', 'w+', newline='', encoding='utf-8')
	
	#write the data to the .csv file
	try:
		with leagueTable:
			fields2 = list(response2['standing'][0].keys())
			writer2 = csv.DictWriter(leagueTable, fieldnames=fields2)
			writer2.writeheader()
			writer2.writerows(response2['standing'])
	#if data does not exist or is not stored in the standard format catch KeyError
	except KeyError as e:
		print ('KeyError in league ' + str(g)) 
		print (response2.keys())
	leagueTable.close()



for g in games:
	#get teams in a particular league
	connection.request('GET', '/v1/competitions/'+str(g)+'/teams', None, headers )
	response3 = json.loads(connection.getresponse().read().decode())
	
	#open/create a .csv file for the teams
	leagueTeams = open('Data/' + str(g)+'/league_Teams_'+str(g)+'.csv', 'w+', newline='', encoding='utf-8')
	
	#write the data to the .csv file
	try:
		with leagueTeams:
			fields3 = ['squadMarketValue', 'name', 'crestUrl', 'shortName', 'id']
			print(fields3)
			writer3= csv.DictWriter(leagueTeams, fieldnames=fields3)
			writer3.writeheader()
			writer3.writerows(response3['teams'])
	#if data does not exist or is not stored in the standard format catch KeyError
	except KeyError as e:
		print ('KeyError in league ' + str(g)) 
		print (response3.keys())
	leagueTeams.close()

		
		
		
		
		
		
		
		