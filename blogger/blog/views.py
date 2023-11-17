from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from blog.forms import AuthorForm
from blog.models import Author

@login_required
def index_view(request):
    return render(request, 'index.html')
@login_required
def blog_list_view(request):
    return render(request, 'blog_list.html')

def add_author_view(request):
    message = ''
    if request.method == "POST":
        author_form = AuthorForm(request.POST)
        
        if author_form.is_valid():
            author_form.save()
            
            message = 'Author added successfully'
    else:
        author_form = AuthorForm  
    
    authors = Author.objects.all()
     
        
    context = {
        'form' : author_form,
        'msg' : message,
        'authers' : authors,
        
    }  
    
    return render(request, "add_author.html", context)

def edit_author_view(request, author_id):
    message = ''
    author = Author.objects.get(id=author_id)
   
    if request.method == "POST":
       author_Form = AuthorForm(request.POST, instance=author)
       
       if author_Form.is_valid():
           author_Form.save()
           message = 'changes saved successfully!'
       else:
           message = 'Form has invalid data'
    else:
        author_Form = AuthorForm( instance=author)
        
    context = {
        'form': author_Form,
        'author': author
    }
    
    return render(request, 'edit_author.html', context)


def delete_author_view(request, author_id):
    
    author = Author.objects.get(id=author_id)
    
    author.delete
    
    return redirect(add_author_view)

def sign_up_view(request):
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)
        
        if sign_up_form.is_valid():
            sign_up_form.save()
            message ='user created succefully'
        else:
            message = 'something went wrong'
   
    else:
        sign_up_form = UserCreationForm()
    
    context = {
        'form' : sign_up_form
        
    }  
    
    return render(request, 'registration/sign_up.html', context )  





        

#Author.objects.get(pk=2)
# select * FROM author WHERE id=?
    
