from django.contrib import admin
from .models import (
    ContactMessage,
    NewsletterSubscriber,
    ContactInfo,
    ContactEmail,
    ContactPhone,
    ContactAddress,
    SocialLink,
)


class ContactEmailInline(admin.TabularInline):
    model = ContactEmail
    extra = 1


class ContactPhoneInline(admin.TabularInline):
    model = ContactPhone
    extra = 1


class ContactAddressInline(admin.TabularInline):
    model = ContactAddress
    extra = 1


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [
        ContactAddressInline,
        ContactPhoneInline,
        ContactEmailInline,
        SocialLinkInline,
    ]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    readonly_fields = ('created_at',)