from nba_api.stats.static import teams, players
import nbaFuncs

seasonOptions = ['-', '1996-97', '1997-98', '1998-99', '1999-00', '2000-01', '2001-02', '2002-03', '2003-04',
                '2004-05', '2005-06', '2006-07', '2007-08', '2008-09', '2009-10', '2010-11', '2011-12',
                '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20',
                '2020-21', '2021-22']

seasonTypeOptions = ['Regular Season', 'Pre Season', 'Playoffs', 'All Star']

nba_teams = teams.get_teams()

def getSeasonOptions():
    return seasonOptions

def getTeamAbbrevs():
    abbrevOptions = ['-']
    for i in range(len(nba_teams)):
        abbrevOptions.append(nba_teams[i]['abbreviation'])

    return abbrevOptions

def getTeamNames():
    teamNameOptions = ['-']
    for i in range(len(nba_teams)):
        teamNameOptions.append(nba_teams[i]['full_name'])

    return teamNameOptions

def getSeasonTypeOptions():
    return seasonTypeOptions


def isValidValues(fName, lName, team, season, seasonType):

    playerName = fName + " " + lName
    if nbaFuncs.get_player_ID(playerName) == -1:
        return False

    if nbaFuncs.get_team_ID(team) == -1:
        return False

    if not season in seasonOptions:
        return False
    
    if not seasonType in seasonTypeOptions:
        return False

    return True