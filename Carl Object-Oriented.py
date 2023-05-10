class Participant:
    def __init__(self, name):
        self.name = name
        self.team = None

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, participant):
        if len(self.members) < 5:
            self.members.append(participant)
            participant.team = self

class Tournament:
    def __init__(self):
        self.teams = [Team("Team 1"), Team("Team 2"), Team("Team 3"), Team("Team 4"), Team("Team 5")]
        self.participants = []

    def add_participant(self, name, team=None):
        if team:
            for t in self.teams:
                if t.name == team:
                    t.add_member(Participant(name))
                    participant = Participant(name)
                    participant.team = t
                    self.participants.append(participant)
                    print(f"{name} added to {team}")
                    return
            print("Invalid team name.")
        elif len(self.participants) < 20:
            participant = Participant(name)
            self.participants.append(participant)
            print(f"{name} added as individual participant")
        else:
            print("No more spaces available for individuals.")

# Menu system
t = Tournament()
menu_choices = ["1. Add participant", "2. View participants", "3. Quit"]
while True:
    print("\nSelect an option:")
    print("\n".join(menu_choices))
    choice = input()
    if choice == '1':
        while True:
            print("Enter participant name (or 'q' to quit adding participants):")
            name = input()
            if name == 'q':
                break
            team_choices = [t.name for t in t.teams]
            team_choices.append('')
            while True:
                print(f"Enter team name ({', '.join(team_choices)}):")
                team = input()
                if team == '' or team in team_choices:
                    break
                print("Invalid team name.")
            t.add_participant(name, team=team if team else None)
    elif choice == '2':
        print("Participants:")
        for p in t.participants:
            print(p.name, "(", p.team.name if p.team else "Individual", ")")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

