from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

from . models import Contact,Message

# Create your views here.

# def home(request):
#     return render(request,'index.html')

class HomePageView(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager = self.request.user)



class ContactCreateView(LoginRequiredMixin,CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['name','email','phone','designation','info','gender','image']
    
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request,'Contact created successfully !')
        return redirect('home_view')


class ContactDetailView(LoginRequiredMixin,DetailView):
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'c'

@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(phone__iexact=search_term) |
            Q(designation=search_term) |
            Q(gender__iexact=search_term) |
            Q(date_added__icontains=search_term)
        )
        context ={
            'search_term':search_term,
            'contacts':search_results.filter(manager=request.user),

        }
        return render(request,'search.html',context)
    else:
        return redirect('home_view')
        #in case not /GET only in urll


class ContactUpdateView(LoginRequiredMixin,UpdateView):
    model = Contact
    template_name = 'update.html'
    fields = ['name','email','phone','designation','info','gender','image']

    def form_valid(self,form):
        instance = form.save()
        messages.success(self.request,'Contact Updated Successfully !')
        return redirect('detail_view',instance.pk)



class ContactDeleteView(LoginRequiredMixin,DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = '/'
    
    def delete(self,request,**kwargs):
        messages.success(self.request,'Successfully Deleted')
        return super().delete(self,request,**kwargs)


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')#not home


class MessageView(LoginRequiredMixin,CreateView):
    model = Message
    template_name = 'message.html'
    fields = ['subject','description']
    

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        
        messages.success(self.request,'Message sent successfully!')
        return redirect('home_view')

    