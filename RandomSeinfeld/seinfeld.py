'''
Created on Aug 13, 2013

@author: aduba_000
'''

import random 
from episode_names import episode_names



season1 = {1: 'The Seinfeld Chronicles',
           2: 'The Stakeout',
           3: 'The Robbery',
           4: 'Male Unbonding',
           5: 'The Stock tip'        
          }


def select_season():
    
    season = random.randrange(1,9)
    return season 


def select_episode(season):
    
    if(season == 1):
        episode = random.randrange(1,5)
        return episode
    elif(season == 2):
        episode = random.randrange(1,12)
        return episode
    elif(season == 3):
        episode = random.randrange(1,23)
        return episode
    elif(season == 5) or (season == 8):
        episode = random.randrange(1,22)
        return episode
    else:
        episode = random.randrange(1,24)
        return episode
        
    
def print_episodes():
    season = select_season()
    episode = select_episode(season)


    print "Season: " + str(season) + " "
    print "Episode: " + str(episode)+ " "
    print episode_names.get( (season, episode) )
    
print_episodes()
h = raw_input()


