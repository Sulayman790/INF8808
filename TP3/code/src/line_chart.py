'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.

    fig = px.line()
    fig.update_layout(
        annotations=[dict(x=0.5, y=0.5, text="No data to display. Select a cell in the heatmap for more information.",
                          showarrow=False)],
        dragmode=False
    )
    return fig


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    # TODO : Draw the rectangle
    fig.update_layout(
        shapes=[dict(
            type="rect",
            xref="paper",
            yref="paper",
            x0=0,
            y0=0.25,
            x1=1,
            y1=0.75,
            fillcolor=THEME["pale_color"],
        )]
    )
    return fig


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    # TODO : Construct the required figure. Don't forget to include the hover template
    fig = px.line(line_data, x=line_data.columns[0], y=line_data.columns[1])
    fig.update_layout(
        xaxis_title='',
        yaxis_title='Trees',
        title=f'Trees planted in {arrond} in {year[0:4]}',  # Display the year only
    )

    fig.update_traces(hovertemplate=hover_template.get_linechart_hover_template())
    fig.update_xaxes(tickformat='%d %b')

    if len(line_data) == 1:
        fig.update_traces(mode='markers')

    return fig
