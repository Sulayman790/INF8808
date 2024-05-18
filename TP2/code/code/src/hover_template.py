'''
    Provides the template for the hover tooltips.
'''
from modes import MODES


def get_hover_template(name, mode):
    '''
        Sets the template for the hover tooltips.

        The template contains:
            * A title stating player name with:
                - Font family: Grenze Gotish
                - Font size: 24px
                - Font color: Black
            * The number of lines spoken by the player, formatted as:
                - The number of lines if the mode is 'Count ("X lines").
                - The percent of lines fomatted with two
                    decimal points followed by a '%' symbol
                    if the mode is 'Percent' ("Y% of lines").

        Args:
            name: The hovered element's player's name
            mode: The current display mode
        Returns:
            The hover template with the elements descibed above
    '''
    # TODO: Generate and return the over template
  
    # return template
    title = '<span style="font-family: Grenze Gotisch; font-size: 24px; color: black;">%{x}</span>'
    player_name = '<b>Player :</b> {player_name}'.format(player_name=name)

    player_line_format = '{y}' if mode == MODES['count'] else '{y:.2f}%'
    player_line = '<b>Lines :</b> %{format}'.format(format=player_line_format) 

    # br is used to add spacing between the title and the player name and extra is used to remove the extra side title
    return title + '</br> </br> </br>' + player_name + '</br>' + player_line + '<extra></extra>'
