from django.db import models
import secrets
from aensongaApp.paystack import PayStack
# Create your models here.

class HomeSlideshowImage(models.Model):
    picture = models.ImageField(upload_to="pictures/Carousel")
    title = models.CharField(max_length=500)
    caption = models.TextField()
    
    
    def __str__(self):
        return self.title
    

class Cause(models.Model):
    picture = models.ImageField(upload_to="pictures/Courses")
    title = models.CharField(max_length=200)
    caption = models.TextField()
    targetAmount = models.PositiveBigIntegerField()
    def __str__(self):
        return self.title
    
    
class Event(models.Model):
    flyer = models.ImageField(upload_to="pictures/Events")
    title = models.CharField(max_length=200)
    caption = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} is happening live at {self.venue}"
    
    
class TeamMember(models.Model):
    fullName = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    profile = models.ImageField(upload_to="pictures/teamMembers")
    #social media handels
    twitter = models.URLField()
    facebook = models.URLField()
    linkedIn = models.URLField()
    instagram = models.URLField()
    
    def __str__(self):
        return self.fullName
    
    
class Volunteer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    reason = models.TextField()
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    picture = models.ImageField(upload_to="pictures/Blog")
    title = models.CharField(max_length=200)
    caption = models.TextField()
    
    def __str__(self):
        return self.title
    
class Donation(models.Model):
    email = models.EmailField()
    amount = models.PositiveBigIntegerField()
    reference = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("-date_created", )
    
    def __str__(self):
        return f"An amount of GH {self.amount} was donated by {self.email}"
    
    def save(self, *args, **kwargs):
        while not self.reference:
            ref = secrets.token_urlsafe(15)
            object_with_similar_ref = Donation.objects.filter(reference=ref)
            if not object_with_similar_ref:
                self.reference = ref
        super(Donation, self).save(*args, **kwargs)
        
        
    def amount_value(self):
        return self.amount * 100
    
    def verify_donation(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.reference, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
            
        if self.verified:
            return True
        return False