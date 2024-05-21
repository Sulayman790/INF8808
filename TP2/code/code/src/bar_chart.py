'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN
from template import THEME


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()


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

    fig.data = []
    
    for player, player_data in data.groupby(by='Player'):
        fig.add_trace(go.Bar(name=player, x=player_data['Act'], 
                             y=player_data[MODE_TO_COLUMN[mode]], 
                             # hovertext part :
                             hovertemplate=get_hover_template(player, mode)))


    fig.update_layout(barmode='stack', xaxis= {'tickprefix': 'Act '})
    return update_y_axis(fig, mode)


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    
    fig.update_layout(yaxis_title='Lines (%)' if mode == MODES['percent'] else 'Lines (Count)')
    return fig