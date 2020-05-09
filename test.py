# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Carousel(Component):
    """A Carousel component.
The main carousel component

Keyword arguments:
- id (string; optional): Unique identifier of the element.
- value (boolean | number | string | dict | list; optional): An array of objects to display.
- page (number; default 0): Index of the first item.
- header (boolean | number | string | dict | list; optional): Label of header.
- footer (boolean | number | string | dict | list; optional): Label of footer.
- style (dict; optional): Inline style of the component.
- className (string; optional): Style class of the component.
- itemTemplate (boolean | number | string | dict | list; optional): Function that gets an item in the value and returns the content for it.
- circular (boolean; default False): Defines if scrolling would be infinite.
- autoplayInterval (number; default 0): Time in milliseconds to scroll items automatically.
- numVisible (number; default 1): Number of items per page.
- numScroll (number; default 1): Number of items to scroll.
- responsiveOptions (list; optional): An array of options for responsive design.
- orientation (string; default 'horizontal'): Specifies the layout of the component, valid values are "horizontal" and "vertical".
- verticalViewPortHeight (string; default '300px'): Height of the viewport in vertical layout.
- contentClassName (string; optional): Style class of main content.
- containerClassName (string; optional): Style class of the viewport container.
- dotsContainerClassName (string; optional): Style class of the paginator items."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, page=Component.UNDEFINED, header=Component.UNDEFINED, footer=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, itemTemplate=Component.UNDEFINED, circular=Component.UNDEFINED, autoplayInterval=Component.UNDEFINED, numVisible=Component.UNDEFINED, numScroll=Component.UNDEFINED, responsiveOptions=Component.UNDEFINED, orientation=Component.UNDEFINED, verticalViewPortHeight=Component.UNDEFINED, contentClassName=Component.UNDEFINED, containerClassName=Component.UNDEFINED, dotsContainerClassName=Component.UNDEFINED, onPageChange=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'value', 'page', 'header', 'footer', 'style', 'className', 'itemTemplate', 'circular', 'autoplayInterval', 'numVisible',
                            'numScroll', 'responsiveOptions', 'orientation', 'verticalViewPortHeight', 'contentClassName', 'containerClassName', 'dotsContainerClassName']
        self._type = 'Carousel'
        self._namespace = 'dash_extra_ui_components'
        self._valid_wildcard_attributes = []
        self.available_properties = ['id', 'value', 'page', 'header', 'footer', 'style', 'className', 'itemTemplate', 'circular', 'autoplayInterval', 'numVisible',
                                     'numScroll', 'responsiveOptions', 'orientation', 'verticalViewPortHeight', 'contentClassName', 'containerClassName', 'dotsContainerClassName']
        self.available_wildcard_properties = []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Carousel, self).__init__(**args)
