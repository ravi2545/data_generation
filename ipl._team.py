import csv
import random

def generate_ipl_teams_and_players():
    """Generate IPL teams with their players and details."""
    teams = [
        'Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore',
        'Kolkata Knight Riders', 'Sunrisers Hyderabad', 'Delhi Capitals',
        'Rajasthan Royals', 'Punjab Kings', 'Gujarat Titans', 'Lucknow Super Giants'
    ]
    
    players = [
        'Virat Kohli', 'MS Dhoni', 'Rohit Sharma', 'Jasprit Bumrah', 'Hardik Pandya',
        'Suryakumar Yadav', 'Rishabh Pant', 'KL Rahul', 'Shubman Gill', 'Ravindra Jadeja',
        'Yuzvendra Chahal', 'Shikhar Dhawan', 'Sanju Samson', 'David Warner', 'Kane Williamson',
        'Andre Russell', 'Sunil Narine', 'Pat Cummins', 'Ben Stokes', 'Faf du Plessis',
        'Trent Boult', 'Kieron Pollard', 'Quinton de Kock', 'Glenn Maxwell', 'Mohammed Shami',
        'Marcus Stoinis', 'Rashid Khan', 'Jofra Archer', 'Bhuvneshwar Kumar', 'Deepak Chahar',
        'Prithvi Shaw', 'Ajinkya Rahane', 'Axar Patel', 'Ishan Kishan', 'Ruturaj Gaikwad',
        'Ravi Bishnoi', 'Harshal Patel', 'Navdeep Saini', 'Washington Sundar', 'Varun Chakravarthy',
        'Shardul Thakur', 'Mohammad Siraj', 'Riley Meredith', 'Tim David', 'Mitchell Marsh',
        'Shimron Hetmyer', 'Chris Jordan', 'Jason Holder', 'Moeen Ali', 'Dinesh Karthik'
    ]
    
    countries = ['India', 'Australia', 'England', 'West Indies', 'South Africa', 'New Zealand', 'Afghanistan', 'Sri Lanka']
    
    # Shuffle the players list
    random.shuffle(players)
    
    # Ensure each team gets more than 20 players
    players_per_team = 22
    team_players = {team: [] for team in teams}
    
    for i, player in enumerate(players):
        age = random.randint(20, 35)
        jersey_number = random.randint(1, 99)
        country = random.choice(countries)
        price = f"${random.uniform(0.5, 15.0):.2f} million"
        
        team_players[teams[i % len(teams)]].append({
            'player': player,
            'age': age,
            'jersey_number': jersey_number,
            'country': country,
            'price': price
        })
    
    # Assign additional players if needed to meet the minimum requirement of 22 players per team
    remaining_players = players[len(teams) * players_per_team:]
    for i, player in enumerate(remaining_players):
        age = random.randint(20, 35)
        jersey_number = random.randint(1, 99)
        country = random.choice(countries)
        price = f"${random.uniform(0.5, 15.0):.2f} million"
        
        team_players[teams[i % len(teams)]].append({
            'player': player,
            'age': age,
            'jersey_number': jersey_number,
            'country': country,
            'price': price
        })

    # If any team has less than the required number of players, add more players from the list
    for team in teams:
        while len(team_players[team]) < players_per_team:
            player = random.choice(players)
            age = random.randint(20, 35)
            jersey_number = random.randint(1, 99)
            country = random.choice(countries)
            price = f"${random.uniform(0.5, 15.0):.2f} million"
            
            team_players[team].append({
                'player': player,
                'age': age,
                'jersey_number': jersey_number,
                'country': country,
                'price': price
            })
    
    return team_players

def write_teams_to_csv(file_path, team_players):
    """Write the teams and their players to a CSV file."""
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Team', 'Player', 'Age', 'Jersey_number', 'Country', 'Price'])  # Write header
        
        for team, players in team_players.items():
            for player_info in players:
                writer.writerow([
                    team, 
                    player_info['player'], 
                    player_info['age'], 
                    player_info['jersey_number'], 
                    player_info['country'], 
                    player_info['price']
                ])
    
    print(f"Data written to {file_path}")

if __name__ == "__main__":
    # Generate IPL teams and their players
    team_players = generate_ipl_teams_and_players()
    
    # Define CSV file path
    file_path = 'ipl_teams_players_details.csv'
    
    # Write teams and players to CSV
    write_teams_to_csv(file_path, team_players)
