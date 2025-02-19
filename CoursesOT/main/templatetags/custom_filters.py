from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary[str(key)]

@register.filter
def get_item_id(query_set, id):
    return query_set.get(id=id)