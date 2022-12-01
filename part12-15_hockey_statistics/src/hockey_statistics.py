# Write your solution here
import json

class Application:
    def __init__(self) -> None:
        self.players = []

    def reading_file(self, myfile):
        with open(myfile) as f:
            data = f.read()
        self.players = json.loads(data)
        f.close()
        print(f"read the data of {len(self.players)} players")
        print("")

    def info(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def search_by_name(self, name):
        for player in self.players:
            if player["name"] == name:
                points = player['goals'] + player['assists']
                print(f"{player['name']:21}{player['team']:3}  {player['goals']:2} + {player['assists']:2} = {points:3}")
                
    def list_all_teams(self):
        result = []
        for player in self.players:
            result.append(player["team"])
        for team_name in sorted(set(result)):
            print(team_name)
        print("")

    def list_all_countries(self):
        result = []
        for player in self.players:
            result.append(player["nationality"])
        
        for country in sorted(set(result)):
            print(country)
        print("")
    
    

    def list_players_in_team(self, team):
        team_players = []
        for player in self.players:
            if player["team"] == team:
                team_players.append(player)
        new_list = sorted(team_players, key= lambda p: p["goals"] + p["assists"], reverse=True)

        for p in new_list:
            self.search_by_name(p["name"])
        print("")
                
    def list_players_country(self, country):
        country_players = []
        for player in self.players:
            if player["nationality"] == country:
                country_players.append(player)
        
        new_list = sorted(country_players, key = lambda p: p["goals"] + p["assists"], reverse = True)
        for n in new_list:
            self.search_by_name(n["name"])
        print("")


    def list_n_players(self, n):
        new_list = sorted(self.players, key = lambda p: (p["goals"] + p["assists"], p["goals"]), reverse = True)

        i = 0
        while (i < n):
            self.search_by_name(new_list[i]["name"])
            i += 1

    def list_n_most_goals(self, n):
        new_list = sorted(self.players, key = lambda p: (p["goals"], 1/p["games"]), reverse = True)
        i = 0
        while (i < n):
            self.search_by_name(new_list[i]["name"])
            i += 1

    def exec(self):
        file_name = input("file name: ")
        self.reading_file(file_name)
        
        self.info()
        print("")
        while True:
            command = int(input("command: "))

            if command == 0:
                break

            elif command == 1:
                name = input("name: ")
                self.search_by_name(name)
            
            elif command == 2:
                self.list_all_teams()

            elif command == 3:
                self.list_all_countries()

            elif command == 4:
                team = input("team: ")
                self.list_players_in_team(team)
            elif command == 5:
                country = input("country: ")
                self.list_players_country(country)
            
            elif command == 6:
                n = int(input("how many: "))
                self.list_n_players(n)
            
            elif command == 7:
                n = int(input("how many: "))
                self.list_n_most_goals(n)


a = Application()
a.exec()
