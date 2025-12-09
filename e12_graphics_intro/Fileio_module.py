#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE IO module

Has all the input-output functions involving files. 
    
Created on Sun Dec  1 11:57:15 2024

@author: selena
"""
# import menu2
def read_high_scores(filename):
    """ 
    
    Reads high scores from a file and returns them as a dictionary.
    Each line in the file should have the format: player_name,score.
    
    """
    high_scores = {}
    high_scores_list = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines() # each line is a single string
            # now split each line into a list with two values
            for line in lines:
                score_item_pair = line.rstrip().split(",")
                print(score_item_pair)
                # make score an integer
                score_item_pair[1] = int(score_item_pair[1])
                high_scores_list.append(score_item_pair)
    except IOError:
        print(f"The file {filename} does not Exist!")
    
    
    high_scores = dict(high_scores_list)
    return high_scores


def write_high_scores(filename, high_scores):
    """ 
    
    Writes high scores to a file.
   Expects high_scores to be a dictionary with player_name as keys and scores as values.
    """
    try:
        # Save updated scores
        # ---------------
        # NOTE this function assumes scores are already sorted
        
        # nos write high_scores_sorted to file
        with open(filename , 'w') as fwrite:  
            for key, value in high_scores.items():  
                fwrite.write(f"{key},{value}\n")
    except IOError:
        print(f"The file {filename} does not Exist!")

    return 

def get_score(item):
    """
    Helper function to return the score (second element)
    """
    return item[1]
    

def update_high_scores(high_scores, player_name, score, max_recent_players=5):
    """
    
    """"""
    Updates the high scores with a new player's score.
    Adds or updates the player's score in the dictionary and retains the highest scores.

    """
    if player_name in high_scores:
        high_scores[player_name] = max(high_scores[player_name], score)
    else:
        high_scores[player_name] = score
        
    high_scores_list = list(high_scores.items())
    sorted_scores = sorted(high_scores_list, key = get_score, reverse = True)
    top_scores = sorted_scores[:max_recent_players]
    return dict(top_scores)

def calculate_score(difficulty, turns, percent_ships):
    score = int(((difficulty*percent_ships)//((turns-14)//2))*10000)
    return score



# def read_recent_players(filename2):
#     """ 
#     Reads high scores from a file and returns them as a dictionary.
#     Each line in the file should have the format: player_name,score.
#     """
#     recent_list = ['angela']
#     try:
#         with open(filename2, 'r') as file:
#             lines = file.readlines() # each line is a single string
#             print(lines)
#             recent_list.append(lines)
#             # make score an integer
#     except IOError:
#         print(f"The file {filename2} does not Exist!")

#     return recent_list


# def write_recent_players(filename2, recent_list):
#     """ 
    
#     Writes high scores to a file.
#    Expects high_scores to be a dictionary with player_name as keys and scores as values.
#     """
#     try:
#         # Save updated scores
#         # ---------------
#         # NOTE this function assumes scores are already sorted
        
#         # nos write high_scores_sorted to file
#         with open(filename2 , 'w') as fwrite:  
#             for names in recent_list:  
#                 fwrite.write(f"{names}\n")
#     except IOError:
#         print(f"The file {filename2} does not Exist!")

#     return 
# recent_list = read_recent_players('recent_players.txt')
# write_recent_players('recent_players.txt', recent_list)
# read_recent_players('recent_players.txt')


# def main():
#     filename = "high_scores,txt"
#     high_scores = read_high_scores(filename)
#     playername = ''
#     high_scores = update_high_scores(high_scores, playername, 140)
#     write_high_scores (filename, high_scores)
#     print("Updated High Scores:")
#     for name, score in high_scores.items():
#         print(f"{name}: {score}")
    
# if __name__ == "__main__":
#     main()