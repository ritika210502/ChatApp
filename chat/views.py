from django.shortcuts import redirect,render

# Create your views here.
def chatPage(request,*args,**kwargs):
    if not request.user.is_authenticated:
        return redirect('login-user')
        
    context={}
    return render(request, "chat/chatPage.html", context)
