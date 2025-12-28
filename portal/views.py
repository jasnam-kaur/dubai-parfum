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

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Perfume

# --- DEVELOPER / SUPERUSER INTERFACE ---
@staff_member_required
def owner_dashboard(request):
    """Luxury dashboard for you to see all activity and items."""
    total_items = Perfume.objects.count()
    items = Perfume.objects.all()
    return render(request, 'owner_dashboard.html', {
        'total_items': total_items,
        'items': items
    })

# --- CUSTOMER INTERFACE ---
def product_list(request):
    """Public page for users to browse perfumes."""
    perfumes = Perfume.objects.all()
    return render(request, 'product_list.html', {'perfumes': perfumes})

def get_quote(request):
    """Quote form that pre-fills based on the perfume clicked."""
    item_name = request.GET.get('item', 'General Inquiry') # Gets name from URL
    
    if request.method == 'POST':
        # Logic to send you an email when they submit
        customer_email = request.POST.get('email')
        message = request.POST.get('message')
        
        send_mail(
            subject=f"Quote Request for {item_name}",
            message=f"From: {customer_email}\n\nMessage: {message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL], # Set this in Render Env
        )
        return render(request, 'quote_success.html')

    return render(request, 'quote_form.html', {'item_name': item_name})

from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Perfume

# --- WORLD 1: THE CUSTOMER (Public) ---
def product_list(request):
    """Shows all perfumes to the public."""
    perfumes = Perfume.objects.all().order_by('-created_at') # Newest first
    return render(request, 'product_list.html', {'perfumes': perfumes})

def quote_request(request):
    """Handles the 'Get Quote' button logic."""
    # Capture the perfume name from the URL (?item=PerfumeName)
    item_name = request.GET.get('item', 'General Inquiry')
    
    if request.method == 'POST':
        # Logic to handle the form submission (e.g., send email) goes here
        return render(request, 'quote_success.html')
        
    return render(request, 'quote_form.html', {'item_name': item_name})

# --- WORLD 2: THE OWNER (Private) ---
@staff_member_required
def owner_dashboard(request):
    """Your private luxury dashboard."""
    items = Perfume.objects.all()
    context = {
        'items': items,
        'total_count': items.count(),
    }
    return render(request, 'owner_dashboard.html', context)

