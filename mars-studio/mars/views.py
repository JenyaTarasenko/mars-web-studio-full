from django.shortcuts import render, redirect
from .models import WebSait, Contact
from .forms import ContactForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView





def submith_question(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mars:index')
    else:
        form = ContactForm()
    items =   WebSait.objects.all()   
    return render(request, 'app/pages/index.html', {'form': form, 'items': items})


class DetailViewItem(DetailView):
    
    model = WebSait
    template_name = 'app/pages/detail.html'
    context_object_name = 'detail'
    
    
    


    
   