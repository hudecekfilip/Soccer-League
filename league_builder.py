import csv

yes = []
no = []

dragons = []
sharks = []
raptors = []

dragons_practice = "March 17, 1pm"
sharks_practice = "March 17, 3pm"
raptors_practice = "March 18, 1pm"

# dividing players to the Teams based on the experiences
def players_divide(my_list):
	count = 0
	for test in my_list:
		count += 1
		if count <= 3:
			dragons.append(test)
		elif count <= 6:
			sharks.append(test)
		elif count <= 9:
			raptors.append(test)

# creating a letter
def letter(team_1, team_2, practice):
	for items in team_1:
		# creating a letter with lowercased names and replacing "space" for "_" between names
		file = open(items["Name"].lower().replace(" ","_") + ".txt", "a")
		file.write("Dear "+ items["Guardian Name(s)"] + ", " + "\n" + "\n")
		file.write("your child " + items["Name"] + " has been placed to the team ")
		file.write(team_2 + " and you should attend their first team practice, ")
		file.write("which will be on " + practice + "\n" + "\n")
		file.write("We are looking forward to see you there!")
		file.close()

if __name__ == '__main__':
	# converting csv file to the dictionary
	reader = csv.DictReader(open('soccer_players.csv'))

	# dividing players to the lists, yes = experienced, no = no-experienced
	for row in reader:
		if row["Soccer Experience"] == "YES":
			yes.append(row)
		else:
			no.append(row)

	players_divide(yes)
	players_divide(no)

	letter(dragons, "Dragons", dragons_practice)
	letter(sharks, "Sharks", sharks_practice)
	letter(raptors, "Raptors", raptors_practice)
