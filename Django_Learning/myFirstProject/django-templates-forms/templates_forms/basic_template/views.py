# File: views.py of the New App "app_django_html_templates"
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Python Template
def simple_template_python(request):

    # Create Template Object
    template = loader.get_template('simple-template.html')

    # Data (context) to be passed to template
    context = {
        'course_list': ['basic','advanced','web development'],
        'l_title': 'Welcome to Python Training',
        'course_name':'PYTHON',
    }
    
    # Use the "context" to render the HTML Template to display values
    return HttpResponse(template.render(context, request))
# END

    
# Java Template
def simple_template_java(request):

    # Create Template Object
    template = loader.get_template('simple-template.html')


    # Data (context) to be passed to template
    context = {
        'course_list': ['core','advanced','spring'],
        'l_title': 'Welcome to Java Training',
        'course_name':'JAVA',
    }
    
    # Use the "context" to render the HTML Template to display values
    return HttpResponse(template.render(context, request))
# END


# DB Template
def simple_template_db(request):

    # Create Template Object
    template = loader.get_template('simple-template.html')


    # Data (context) to be passed to template
    context = {
        'course_list': ['SQL','TSQL','ADMIN'],
        'l_title': 'Welcome DB Training',
        'course_name':'DB',
    }
    
    # Use the "context" to render the HTML Template to display values
    return HttpResponse(template.render(context, request))
# END

