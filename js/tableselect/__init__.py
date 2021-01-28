from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery
from js.jquery_datatables import fixed_header
from js.jquery_datatables import jquery_datatables


library = Library('namespace', 'resources')

tableselect_css = Resource(library, 'tableselect.css')

tableselect = Resource(library, 'tableselect.js',
                       depends=[
                           jquery, jquery_datatables, fixed_header,
                           tableselect_css])
