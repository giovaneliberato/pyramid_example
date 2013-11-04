from pyramid.renderers import get_renderer

def base_layout():
    renderer = get_renderer("../templates/base.pt")
    layout = renderer.implementation().macros['layout']
    return layout