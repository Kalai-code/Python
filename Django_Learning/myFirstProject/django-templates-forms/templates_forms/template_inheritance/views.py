from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Template Inheritance Callers
# results=[[1, 2, 3, 4,], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# https://stackoverflow.com/questions/9388064/django-template-turn-array-into-html-table


def caller_borders(request):
    
    
    multi_line_data = {"data": zip( ["Python Scripts","Python OOP","Python Libraries"]
                                   ,[ "Training for Python as Scripting Language"
                                     ,"Training for Python Object Oriented programming"
                                     ,"Training for Python Libraries for real world usage"])}
    print(multi_line_data)

    # Create Template Object
    template = loader.get_template('inheritance_caller_borders.html')
    context = multi_line_data
    return HttpResponse(template.render(context, request))
# END


def caller_table(request):
    list_of_lists_data = {"data": [ ["Python Scripts","Training for Python as Scripting Language"]
                                   ,["Python OOP","Training for Python Object Oriented programming"]
                                   ,["Python Libraries","Training for Python Libraries for real world usage"]]}

    # Create Template Object
    template = loader.get_template('inheritance_caller_table.html')
    context = list_of_lists_data
    return HttpResponse(template.render(context, request))
# END

"""
def caller_accordian(request):

    multi_line_data_js_control = {"data": zip( ["scripts","oop","lib"]
                                   ,["Python Scripts","Python OOP","Python Libraries"]
                                   ,[ "Training for Python as Scripting Language"
                                     ,"Training for Python Object Oriented programming"
                                     ,"Training for Python Libraries for real world usage"])}
    print(multi_line_data_js_control)

    # Create Template Object
    template = loader.get_template('inheritance_caller_accordian.html')
    context = multi_line_data_js_control
    return HttpResponse(template.render(context, request))
# END
"""
