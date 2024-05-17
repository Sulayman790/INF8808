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
    # TODO : Modify the dataframe, removing the line content and replacing

    # it by line count and percent per player per act
    df = my_df.loc[:, ['Act', 'Player', 'Line']].groupby(['Act', 'Player']).count().reset_index()
    df.columns = ['Act', 'Player', 'LineCount']
    total_line_count = df.groupby('Act')['LineCount'].sum()
    df['LinePercent'] = (df['LineCount'] / df['Act'].map(total_line_count)) * 100

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
    # TODO : Replace players in each act not in the top 5 by a
    # new player 'OTHER' which sums their line count and percentage
    
    top_5_players_per_act = my_df.groupby('Act').apply(lambda x: x.nlargest(5, 'LineCount')).reset_index(drop=True)    
    
    total_line_count = my_df.groupby('Act')['LineCount'].sum().reset_index()   
    mask = ~my_df.set_index(['Act', 'Player']).index.isin(top_5_players_per_act.set_index(['Act', 'Player']).index)
    other_lines = my_df[mask]
    other_line_counts = other_lines.groupby('Act')['LineCount'].sum().reset_index()
    other_line_counts['Player'] = 'OTHER'
    other_line_counts['LinePercent'] = (other_line_counts['LineCount'] / total_line_count['LineCount']) * 100
    other_line_counts = other_line_counts[['Act', 'Player', 'LineCount', 'LinePercent']]
    
    df = pd.concat([top_5_players_per_act, other_line_counts], ignore_index=True)
    result_df = df.sort_values(by=['Act', 'LineCount'])
    return result_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # TODO : Clean the player names
    my_df['Player'] = my_df['Player'].str.title()
    return my_df
