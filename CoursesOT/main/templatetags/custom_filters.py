from django import template
from django.urls import reverse

register = template.Library()

@register.filter
def get_item(dictionary, key):
    try:
        item = dictionary[str(key)]
    except:
        item = None

    return item

@register.filter
def get_item_id(query_set, id):
    try:
        item = query_set.get(id=id)

    except:
        item = None

    return item

@register.filter
def get_object_db_param(object, param):
    try:
        object_param = getattr(object, param).all()
    except:
        object_param = []

    return object_param

@register.filter
def get_url(name_url):
    return reverse(name_url)

@register.filter
def get_url_join(name_url, last_part:int):
    return reverse(f'{name_url}-{last_part}')

@register.filter
def _in(value, list):
    return value in list

@register.filter
def tag_filter(courses, tags):
    if tags:
        filtred_courses = []

        for course in courses:
            for tag in course.tag.all():
                if tag.title in tags and course not in filtred_courses:
                    filtred_courses.append(course)

        return filtred_courses
    return courses