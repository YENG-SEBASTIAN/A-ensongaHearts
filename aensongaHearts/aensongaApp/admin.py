from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html


# Register your models here.
from aensongaApp.models import (HomeSlideshowImage, Cause, Event, TeamMember, Volunteer, Contact, 
                                Blog, Donation, President, Project, ProjectGallary, Fact )

class HomeSlideshowImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption', 'display_picture')
    search_fields = ('title', 'caption')

    def display_picture(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" width="100" height="100" />')

    display_picture.short_description = 'Picture Preview'
    
admin.site.register(HomeSlideshowImage, HomeSlideshowImageAdmin)


class CauseAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption', 'display_picture')
    search_fields = ['title', 'caption']
    list_filter = ('title', 'caption')

    def display_picture(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" width="100" height="100" />')

    display_picture.short_description = 'Picture Preview'

admin.site.register(Cause, CauseAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption', 'month', 'year',  'display_flyer')
    search_fields = ['title', 'caption', 'year']
    list_filter = ['month', 'year']

    def display_flyer(self, obj):
        return mark_safe(f'<img src="{obj.flyer.url}" width="100" height="100" />')

    display_flyer.short_description = 'Flyer Preview'

admin.site.register(Event, EventAdmin)

# class TeamMemberAdmin(admin.ModelAdmin):
#     list_display = ('fullName', 'designation', 'display_profile', 'display_twitter', 'display_facebook', 'display_linkedIn', 'display_instagram')
#     search_fields = ['fullName', 'designation']
#     list_filter = ['fullName', 'designation']

#     def display_profile(self, obj):
#         return format_html('<img src="{}" width="100" height="100" />', obj.profile.url)

#     display_profile.short_description = 'Profile Preview'

#     def display_twitter(self, obj):
#         return format_html('<a href="{}" target="_blank">{}</a>', obj.twitter, obj.twitter)

#     display_twitter.short_description = 'Twitter'

#     def display_facebook(self, obj):
#         return format_html('<a href="{}" target="_blank">{}</a>', obj.facebook, obj.facebook)

#     display_facebook.short_description = 'Facebook'

#     def display_linkedIn(self, obj):
#         return format_html('<a href="{}" target="_blank">{}</a>', obj.linkedIn, obj.linkedIn)

#     display_linkedIn.short_description = 'LinkedIn'

#     def display_instagram(self, obj):
#         return format_html('<a href="{}" target="_blank">{}</a>', obj.instagram, obj.instagram)

#     display_instagram.short_description = 'Instagram'

# admin.site.register(TeamMember, TeamMemberAdmin)

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'reason')
    search_fields = ['name', 'email']
    list_filter = ['reason']

admin.site.register(Volunteer, VolunteerAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'display_message')
    search_fields = ['name', 'email', 'subject']
    list_filter = ['subject']

    def display_message(self, obj):
        # Limiting the displayed message length to 50 characters for brevity
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message

    display_message.short_description = 'Message'

admin.site.register(Contact, ContactAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_picture', 'display_caption')
    search_fields = ['title', 'caption']

    def display_picture(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" width="100" height="100" />')

    display_picture.short_description = 'Picture Preview'

    def display_caption(self, obj):
        # Limiting the displayed caption length to 50 characters for brevity
        return obj.caption[:50] + '...' if len(obj.caption) > 50 else obj.caption

    display_caption.short_description = 'Caption'

admin.site.register(Blog, BlogAdmin)


class DonationAdmin(admin.ModelAdmin):
    list_display = ('email', 'amount', 'reference', 'verified', 'date_created')
    search_fields = ['email', 'reference']
    list_filter = ['verified', 'date_created']

    def amount_formatted(self, obj):
        return f"GH {obj.amount}"

    amount_formatted.short_description = 'Amount (GH)'

admin.site.register(Donation, DonationAdmin)



class PresidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('created_at',)

admin.site.register(President, PresidentAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_description', 'display_image')
    search_fields = ('project_name', 'project_description')
    list_filter = ('project_name',)

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.project_pic.url}" width="100" height="100" />')

    display_image.short_description = 'Project Image'

admin.site.register(Project, ProjectAdmin)


class ProjectGalleryAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'image', 'description_preview')
    search_fields = ('project__project_name', 'description')
    list_filter = ('project__project_name',)

    def project_name(self, obj):
        return obj.project.project_name if obj.project else ''
    

    def description_preview(self, obj):
        return obj.description[:50] + '...' if obj.description else ''

    project_name.short_description = 'Project Name'
    description_preview.short_description = 'Description Preview'

admin.site.register(ProjectGallary, ProjectGalleryAdmin)


class FactAdmin(admin.ModelAdmin):
    list_display = ('country', 'our_goal', 'raised')

admin.site.register(Fact, FactAdmin)