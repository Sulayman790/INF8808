'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    template =  "<br>".join([
        "<span style='font-weight: bold'>Country</span> : %{customdata[0]}",
        "<span style='font-weight: bold'>Population</span> : %{customdata[1]}",
        "<span style='font-weight: bold'>GDP</span> : %{x} $ (USD)",
        "<span style='font-weight: bold'>CO2 emissions</span> : %{y} metric tons",
        "<extra></extra>"
        ])
    return template
