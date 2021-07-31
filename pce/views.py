from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        a=int(request.POST['number1'])
        b=int(request.POST['number2'])
        
        c=a/b
        print(c)
        return render(request, 'result.html',{'key':c})
    return render(request, 'index.html')
   
def res(request):
    return render(request, 'result.html')


          
