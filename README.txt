AUTHOR Evan Urquhat - 100554128

SETUP/EXECUTION INSTRUCTIONS (WINDOWS)
*if virtualenv is not alreay installed, run the following in a command window*
	pip install virtualenv 
	pip install virtualenvwrapper
*open a command terminal in the folder contaning the files*
*run the following commands*
	virtualenvv venv
	pip install -r requirements.txt
	python Soccer_League_Statistics.py
	deactivate

DATA SET DISCRIPTION
This dataset contains information about various soccer leagues, the teams that played in each league, and the reusults from that league. The data is collected from 'https://api.football-data.org/' and is stored into multiple .csv files in the Data folder organized as follows.

Data
└───LeaguesTOC
└───#LeagueID
│    └───league_Table
│    └───league_Teams

The LeagueTOC (table of contents) contains a list of leagues that were avaliable from the dataset and information for
	- the name of the league
	- the number of teams compeating in the league 
	- the year the league took place 
	- the unique numerical ID associated with the league 
	- the number of games that will be played in the league 
	- the number of days the league will last for
	- the current day of the league 
Each folder in the Data folder has a number that is associated with the numerical ID of the league. In each folder there are two additional .csv files that contain the following: 
	1- information about the teams that are compeating in the league 
	2- the standings of the league and each team in it 
each team in a league is given a unique numerical ID that is used to associate each team in the league_Teams file with the league_table file

several leagues provide information in a non-standard format or do not provide any information at all, in these situations the .csv file for that particular league is left empty.

 
	