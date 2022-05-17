from .forms import TestForm
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
import ast

# View the Current Cart (get details from Cookie)
def cookie_view(request):

    # Create Template Object
    template = loader.get_template('mycart.html')

    # Check if Cookie exists, Check in the Dictionary "request.COOKIES"
    print(request.COOKIES.get('user_id'))

    if 'user_id' in request.COOKIES:

        # Set Cookies    
        userid_txt = str(request.COOKIES['user_id'])
        #cd_list = list(request.COOKIES['CheckBox_Selected'])
        cd_list = request.COOKIES['CheckBox_Selected']
        #print(cd_list[0])
        print(cd_list)
        print(type(cd_list))
        # Data (context) to be passed to template
        context = {
            'user_id': userid_txt,
            'CheckBox_Selected' : ast.literal_eval(cd_list),
            'cookie_status' : 1
        }
        print(context)
    else:
        context = {
            'cookie_status' : 0
        }

    return HttpResponse(template.render(context, request))


# Accept Inputs and Set Cookie
def cookie_set(request):

    if request.method == 'POST':

        # Create Template Object
        template = loader.get_template('mycart.html')

        # Create a New Global Response Object
        response = HttpResponse('test')

        testForm = TestForm(request.POST)

        if testForm.is_valid():

            # Get Shopping Cart Details
            checkbox_data_list = testForm.cleaned_data['CheckBox']

            # Check Box Selected Choice    
            cd_list = []
            for i in checkbox_data_list:
                cd_list.append(TestForm.form_choices[int(i)-1][1])

            # UserID and Password Text Box values
            userid_txt = testForm['userid'].value()

            # Data (context) to be passed to template
            context = {
                'user_id': userid_txt,
                'CheckBox_Selected' : cd_list,
                'cookie_status' : 1
            }

            response = HttpResponse(template.render(context, request))

        # Set Cookies
        # ===========
        response.set_cookie('user_id', userid_txt,max_age=100)
        response.set_cookie('CheckBox_Selected', cd_list,max_age=100)

        return response

    else:
        form = TestForm()
        return render(request,'shopping.html',{'form':form})


# Delete Cookies
def cookie_delete(request):

    # Create Response Object from the Root View Function
    response = redirect('app_cookies.views.cookie_set')
    response.delete_cookie('user_id')
    response.delete_cookie('CheckBox_Selected')

    return HttpResponse('Cookies Deleted')