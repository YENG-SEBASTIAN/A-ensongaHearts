from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.shortcuts import get_object_or_404

from aensongaApp.models import (HomeSlideshowImage, Cause, Event, TeamMember, Blog, Volunteer, Contact, Donation, President, Project, 
                                ProjectGallary, Fact)
from aensongaApp.forms import ContactForm, DonationForm
from aensongaApp.utils import (send_volunteer_confirmation_email, send_contact_confirmation_email)



# Create your views here.

def about(request):
    volunteer = Volunteer.objects.count()
    projectCount = Project.objects.count()
    facts = Fact.objects.all().first()
    context = {
        "volunteer":volunteer,
        "projectCount":projectCount,
        "facts":facts,
    }
    return render(request, 'aensonga/about.html',context)

def blog(request):
    blogs = Blog.objects.all()
    context = {
        "blogs":blogs,
    }
    return render(request, 'aensonga/blog.html', context)

def causes(request):
    courses = Cause.objects.all()
    context = {
        "courses":courses,
    }
    return render(request, 'aensonga/causes.html', context)

def contact(request):
    return render(request, 'aensonga/contact.html')

def donate(request):
    return render(request, 'aensonga/donate.html')

def event(request):
    events = Event.objects.all()
    context = {
        "events":events,
    }
    return render(request, 'aensonga/event.html', context)

def index(request):
    carousel = HomeSlideshowImage.objects.all()
    courses = Cause.objects.all()
    events = Event.objects.all()
    blogs = Blog.objects.all()
    volunteer = Volunteer.objects.count()
    president = President.objects.latest()
    projectCount = Project.objects.count()
    facts = Fact.objects.all().first()
    print(facts.country)
    context = {
        "carousel":carousel,
        "courses":courses,
        "events":events,
        "facts":facts,
        "president":president,
        "blogs":blogs,
        "volunteer":volunteer,
        "projectCount":projectCount,
    }
    return render(request, 'aensonga/index.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        "projects":projects,
    }
    return render(request, 'aensonga/projects.html', context)

def service(request):
    courses = Cause.objects.all()
    context = {
        "courses":courses,
    }
    return render(request, 'aensonga/service.html', context)

def single(request, project_name):
    project_name = Project.objects.get(project_name=project_name)
    projects = ProjectGallary.objects.filter(project=project_name)
    context = {
        "projects":projects,
        "project_name":project_name
    }
    return render(request, 'aensonga/single.html', context)

def team(request):
    teamMembers = TeamMember.objects.all()
    context = {
        "teamMembers":teamMembers,
    }
    return render(request, 'aensonga/team.html', context)

def volunteer(request):
    return render(request, 'aensonga/volunteer.html')



def become_volunteer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        reason = request.POST.get("reason")
        
        if not name or not email or not reason:
            messages.error(request, 'All fields are required.')
        else:
            # Save data to the Volunteer model
            contact = Volunteer(name=name, email=email, reason=reason)
            contact.save()

            # Send confirmation email
            send_volunteer_confirmation_email(name, email)

            messages.success(request, 'Form submitted successfully.')

            return redirect("/")

    return redirect("volunteer")

def contact_us(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            # If the form is valid, save to the Contact model
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contact.save()

            # Send confirmation email
            send_contact_confirmation_email(contact.name, contact.email)

            messages.success(request, 'Your message was successfully sent!')
            return redirect("/")
        else:
            messages.error(request, 'Please correct the errors in the form.')

    return redirect("contact")



# Paystack payment views
def donate_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        amount = request.POST.get('amount')

        form_data = {'email': email, 'amount': amount}
        form = DonationForm(form_data)

        if form.is_valid():
            donation = form.save()
            
            context = {
                "donation":donation,
                "paystack_public_key": settings.PAYSTACK_PUBLIC_KEY
            }
            return render(request, 'paystack/payment_confirmation.html', context)
        else:
            messages.error(request, 'Please correct the errors in the form.')

    return render(request, 'aensonga/donate.html')



#payment confirmation view
def verify_donation(request, ref):
    donation = get_object_or_404(Donation, reference=ref)
    verified = donation.verify_donation()
    if verified:
        messages.success(request, "Your donation was successful. Thank you.")
        return redirect("/")
    messages.success(request, "We were not able to verify your transaction! please try again")
    redirect("donate")