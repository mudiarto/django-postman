"""
A mock of django-pagination's pagination_tags.py that do nothing.
Just to avoid failures in template rendering during the test suite,
if the real application is not installed.

To activate this mock, just rename it to ``pagination_tags.py``
for the time of the test session.
"""
from django.template import Node, Library

register = Library()

class AutoPaginateNode(Node):
    def render(self, context):
        return u''

@register.tag
def autopaginate(parser, token):
    return AutoPaginateNode()

class PaginateNode(Node):
    def render(self, context):
        return u''

@register.tag
def paginate(parser, token):
    return PaginateNode()
