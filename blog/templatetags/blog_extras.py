from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(name='make_paragraphs')
@stringfilter
def make_paragraphs(text):
    """Transform a string with linefeeds in html paragraphs."""
    paragraphs = text.split('\n')
    html = '</p><p>'.join(paragraphs)
    return('<p>{}</p>'.format(html))
