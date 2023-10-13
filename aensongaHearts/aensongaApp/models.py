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
    month = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} will be happening live in {self.month} {self.year}"
    
    
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
    

class President(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="pictures/ceo")
    about_me = models.TextField(max_length=500)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        get_latest_by = 'created_at'
    
    def __str__(self):
        return self.name
    

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_pic = models.ImageField(upload_to="pictures/project")
    
    def __str__(self):
        return self.project_name
    
class ProjectGallary(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pictures/projectGallary")
    description = models.TextField()
    
    def __str__(self):
        return self.project.project_name
    

class Fact(models.Model):
    country = models.IntegerField(default=0)
    our_goal = models.IntegerField(default=0)
    raised = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Country {self.country},  Our goal {self.our_goal}, Raised {self.raised}"