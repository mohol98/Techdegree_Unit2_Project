from constants import PLAYERS,TEAMS
import copy
app_constants = copy.deepcopy(PLAYERS)
experienced_players = []
inexperienced_players = []
panthers = app_constants[:6]
bandits = app_constants[6:12]
warriors = app_constants[12:] 


def clean_data(app_constants):
   for app_players in app_constants:
       if app_players['experience'] == "YES":
           app_players['experience'] = True
           experienced_players.append(app_players)
       else:
            app_players['experience'] = False
            inexperienced_players.append(app_players)
       
            app_players['height'] = app_players['height'].split(" inches")
            app_players['height'] = int(app_players['height'])
            app_players['team'] = None
            app_players['guardians'] = app_players['guardians'].split(" and ")
       
def main():
    print('BASKETBALL TEAM STATS TOOL\n\n')
    print('----MENU----\n\n')
    print('  Here are your choices')
    print('    1) Display Team Stats')
    print('    2) Quit')
    selection1 = input('Enter an option >')
   
    if selection1 == '1':
        print('\n1) Panthers\n')
        print('2) Bandits\n')
        print('3) Warriors\n')
    else:
        print('Come back to check out the latest stats!')
        return
    
    valid_input = [1,2,3]
    
    while True:
        try:
            selection2 = int(input('Enter an option >'))
            if selection2 in valid_input:
                break
            print("/n That's not a valid input, please enter 1,2, or 3. ")
        except:
            print("/n That's not a valid input, please enter 1,2, or 3. ")
            
    
    team_selection = TEAMS[selection2-1]
    print('\nTeam: ', team_selection)
    print('--------------------')
    
    
    def balance_teams(app_constants):
        if team_selection == 'Panthers':
            panthers_list = [app_players['name'] for app_players in panthers]
            print("Total players: ", len(panthers), "\n" )
            print(', '.join(panthers_list))
        elif team_selection == 'Bandits':
            bandits_list = [app_players['name'] for app_players in bandits]
            print("Total players: ", len(panthers), "\n" )
            print(', '.join(bandits_list))
        elif team_selection == 'Warriors':
            warriors_list = [app_players['name'] for app_players in warriors]
            print("Total players: ", len(panthers), "\n" )
            print(', '.join(warriors_list))
    balance_teams(app_constants)
    end_app = input('\nPress Enter to continue: ')
    if end_app == '':
        main()
    else:
        print("See you next time")
        return
    
        

if __name__ == '__main__':
    main()
    
