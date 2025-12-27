from django.shortcuts import render

def home(request):
    return render(request, 'portal/home.html')

def about(request):
    return render(request, 'portal/about.html')

def categories(request):
    return render(request, 'portal/categories.html')

def quote(request):
    return render(request, 'portal/quote.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_redirect(request):
    """Redirects users to their specific portal based on their role."""
    if request.user.is_superuser or request.user.role == 'ADMIN':
        return redirect('/admin/') # You (Technical Admin)
    elif request.user.role == 'OWNER':
        return redirect('owner_dashboard') # The Business Owner
    else:
        return redirect('client_dashboard') # The Business Client

@login_required
def client_dashboard(request):
    return render(request, 'portal/client_dashboard.html')

@login_required
def owner_dashboard(request):
    return render(request, 'portal/owner_dashboard.html')