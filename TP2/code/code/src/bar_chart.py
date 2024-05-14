'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    # TODO : Update the template to include our new theme and set the title

    fig.update_layout(
        title = "Lines per act", 
        template=pio.templates['simple_white'],
        dragmode=False,
        barmode='relative',
        font=dict(color="grey")
    )

    return fig


def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    fig = go.Figure(fig)  # conversion back to Graph Object
    # TODO : Update the figure's data according to the selected mode
    color_dic = {'Romeo' : 0,
                 'Juliet': 1, 
                 'Nurse':2, 
                 'Mercutio':3, 
                 'Benvolio':4, 
                 'Others':5 }
    data['Color'] = [THEME['bar_colors'][color_dic[x]] for x in data['Player']]
    
    fig.data=[]
    if mode ==  MODES['count']:
        for player, group in data.groupby('Player'):
            fig.add_trace(go.Bar(x=group["Act"], y=group["Count"], name=player, marker_color = group['Color'], 
            # * hovertext part : *
            hovertemplate = get_hover_template(player, mode), hoverlabel= dict(bgcolor = 'white', font_size = 24, font_family = "Grenze Gotish", font_color = 'black')))
    else: 
        for player, group in data.groupby('Player'):
            fig.add_trace(go.Bar(x=group["Act"], y=group["Percentile"], name=player, marker_color = group['Color'],
            # * hovertext part : *
            hovertemplate = get_hover_template(player, mode), hoverlabel= dict(bgcolor = 'white', font_size = 24, font_family = "Grenze Gotish", font_color = 'black') ))
    return fig


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    # TODO : Update the y axis title according to the current mode
    fig.update_layout(yaxis_title='Lines (%)' if mode == MODES['percent'] else 'Lines (Count)')
    return fig