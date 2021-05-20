# django is a package
# shortcut is the module
# render is the function
from django.shortcuts import render
from django.http import HttpResponse
from .models import userprofile
# this is the custom form for uploading the image
from .forms import ProfileForm


# Create your views here.

# view with name index
def index(request):
    form = ProfileForm()

    if request.method == 'POST':
        print(request.POST)
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    # this is required only for GET request to show when page is loaded initially.
    elif request.method == 'GET':
        print("Get")
        form = userprofile.objects.all()

    context = {'form': form}
    # This is the default line of code to display a single line
    # return HttpResponse('Hello World from the User Profile view, soon i am going to turn into a amazing profile page!!!')
    return render(request,'index.html',context)


# view with name newprofiletest
def newprofiletest(request):
    return  HttpResponse("This is the new profile page for testing")



