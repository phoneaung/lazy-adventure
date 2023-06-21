from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# use built in UserCreationForm from django for signup 
def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        
        return redirect('/login/')
    
    else:
        form = UserCreationForm
    
    return render(request, 'userprofile/signup.html', {
        'form': form,
    })
