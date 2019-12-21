from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
	my_context={
	"my_name": "ansh",
	"my_number":124435,
	"my_list":[1231,4253,3445]
	}
	return render(request,"home.html",my_context)

def contact_view(request,*args,**kwargs):
	return render(request,"contact.html",{})
