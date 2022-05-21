# A simple master view file added so the root URL of the project 
# will always redirect (302) instead of error (404).
from django.shortcuts import redirect


def redirect_view(request):
    response = redirect('/entries/')
    return response
