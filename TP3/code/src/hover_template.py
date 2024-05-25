'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    neighbourhood = "<span style=\"font-family:'Roboto Slab'; font-weight: bold\">Neighbourhood: </span><span style=\"font-family:'Roboto'; font-weight: normal\">%{y}</span><br>"
    year = "<span style=\"font-family:'Roboto Slab'; font-weight: bold\">Year: </span><span style=\"font-family:'Roboto'; font-weight: normal\">%{x}</span><br>"
    trees = "<span style=\"font-family:'Roboto Slab'; font-weight: bold\">Trees Planted: </span><span style=\"font-family:'Roboto'; font-weight: normal\">%{z}</span><br>"

    return neighbourhood + year + trees + "<extra></extra>"

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template

    neighbourhood = "<span style=\"font-family:'Roboto Slab'; font-weight: bold\">Neighbourhood: </span><span style=\"font-family:'Roboto'; font-weight: normal\">%{y}</span><br>"
    year = "<span style=\"font-family:'Roboto Slab'; font-weight: bold\">Year: </span><span style=\"font-family:'Roboto'; font-weight: normal\">%{x}</span><br>"
    trees = "<span style=\"font-family:'Roboto Slab'; font-weight: bold\">Trees Planted: </span><span style=\"font-family:'Roboto'; font-weight: normal\">%{z}</span><br>"

    return neighbourhood + year + trees + "<extra></extra>"

