from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('namespace', 'resources')

tableselect = Resource(library, 'tableselect.js', depends=[jquery])
