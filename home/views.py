from django.shortcuts import render,HttpResponse
def index(request):
    context={
        'variable':'this is sent'}
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
    #return HttpResponse('this is about')
def services(request):
    return render(request,'services.html')
   # return HttpResponse('this is services')
def contact(request):
    return render(request,'contact.html')
    #return HttpResponse('this is contact')
    
# Create your views here.
