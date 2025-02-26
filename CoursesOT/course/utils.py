import os
from pathlib import Path
from .models import Course

def load_courses_id():
    courses = Course.objects.all()
    ids = []

    for course in courses:
        ids.append(str(course.id))

    return ids
    