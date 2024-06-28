def team_lineup(*football_teams):
    countries_teams = {}

    for player_name, country_name in football_teams:
        if country_name not in countries_teams:
            countries_teams[country_name] = []
        countries_teams[country_name].append(player_name)

    sorted_countries_teams = sorted(countries_teams.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for country, names in sorted_countries_teams:
        result.append(f'{country}:')
        result.extend(f'  -{name}' for name in names)

    return '\n'.join(result)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
