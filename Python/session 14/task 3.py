#3.Download a sample CSV file of IPL cricket match scores (or create your own with columns: Match, Team1, Team2, Winner), 
# then write Python code to read the CSV and print the name of the winning team for each match


import csv

data = [
    ["Match", "Team1", "Team2", "Winner"],
    [1, "CSK", "MI", "CSK"],
    [2, "RCB", "KKR", "KKR"],
    [3, "GT", "RR", "GT"],
    [4, "DC", "PBKS", "PBKS"],
    [5, "SRH", "LSG", "LSG"]
]

with open("ipl_matches.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("ipl_matches.csv created successfully!")

# reading the csv file 

with open("ipl_matches.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Winning Teams:")
    for row in reader:
        print(f"Match {row['Match']}: {row['Winner']}")