'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    player_appearances = my_df.groupby(['Act', 'Player']).size().reset_index(name='PlayerLine')
    player_appearances.columns = ['Act', 'Player', 'LineCount']
    total_line_count = my_df.groupby('Act')['PlayerLine'].size().reset_index(name='TotalLineCount')
    df = pd.merge(player_appearances, total_line_count, on='Act')
    df['LinePercent'] = (df['LineCount'] / df['TotalLineCount']) * 100

    return df

def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
  
    top_5_players = my_df.groupby('Player')['LineCount'].sum().sort_values(ascending=False).head(5).reset_index()
    mask = my_df['Player'].isin(top_5_players['Player'])
    player_data = my_df[mask]
    
    total_line_counts_per_act = my_df.groupby('Act')['LineCount'].sum().reset_index()
    total_line_counts_per_act.columns = ['Act', 'TotalLineCount']
 
    other_data = my_df[~mask]
    other_line_counts_per_act = other_data.groupby('Act')['LineCount'].sum().reset_index()
    other_line_counts_per_act['Player'] = 'OTHER'
    other_line_counts_per_act['LinePercent'] = (other_line_counts_per_act['LineCount'] / total_line_counts_per_act['TotalLineCount']) * 100
    
    my_df = pd.concat(
        [player_data, other_line_counts_per_act], ignore_index=True)
    my_df = my_df.drop('TotalLineCount', axis=1)
    return my_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''

    my_df['Player'] = my_df['Player'].str.title()
    return my_df
