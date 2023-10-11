from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings



def send_volunteer_confirmation_email(name, email):
    """
    Send a confirmation email to the user who filled out the volunteer form.
    """
    subject = 'Volunteer Form Submission Confirmation'
    text_content = f'Thank you, {name}, for volunteering with us! We appreciate your support.'

    # You can customize the HTML email template using render_to_string
    html_content = render_to_string('aensonga/volunteer_confirmation_email.html', {'name': name, 'company_name': 'A-ensonga Hearts'})

    # Replace 'from@example.com' with your email address
    msg = EmailMultiAlternatives(
        subject,
        text_content,
        settings.EMAIL_HOST_USER,  # from email
        [email],  # to email
        reply_to=[settings.EMAIL_HOST_USER],  # Reply option
    )
    msg.attach_alternative(html_content, "text/html")

    try:
        msg.send()
    except Exception as e:
        print(f"Error sending confirmation email: {e}")



# Contact us emails method
def send_contact_confirmation_email(name, email):
    """
    Send a confirmation email to the user after successful contact.
    """
    subject = 'Thank you for contacting us!'
    message = f'Thank you, {name}, for reaching out to us. We will get back to you as soon as possible.'

    # You can customize the email template using render_to_string
    email_message = render_to_string('aensonga/contact_confirmation_email.html', {'name': name, 'company_name': 'A-ensonga Hearts'})

    # Replace 'from@example.com' with your email address
    email = EmailMultiAlternatives(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # from email
        [email],  # to email
        reply_to=[settings.EMAIL_HOST_USER],  # Reply option
    )
    email.attach_alternative(email_message, "text/html")

    try:
        email.send()
    except Exception as e:
        print(f"Error sending contact confirmation email: {e}")
