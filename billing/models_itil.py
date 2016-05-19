
from django.db import models
from django.forms import ModelForm
         
class Source(models.Model):
    name_source = models.CharField(max_length=100)
    contact_source = models.CharField(max_length=100, blank=True, null=True)
    phone_source = models.CharField(max_length=100,blank=True, null=True)
    email_source = models.EmailField(blank=True, null=True)
    website_source = models.URLField(blank=True, null=True)
    notes_source = models.TextField(blank=True, null=True)
    account_number = models.CharField(max_length=100,blank=True, null=True)
 
    def __unicode__(self):
        return self.name_source  
 
class SourceForm(ModelForm):
    class Meta:
        model = Source
 
class Software(models.Model):
 
    name_software = models.CharField(max_length=100)
    website_software = models.URLField(blank=True, null=True)
    settings_software = models.TextField(blank=True, null=True)
    source = models.ForeignKey(Source)
    def __unicode__(self):
        return self.name_software
         
class Device(models.Model):
 
    TYPE_DEVICE_CHOICES = (
        (u'CMP', u'Computer'),
        (u'SRV', u'Server'),
        (u'PRN', u'Printer'),
        (u'SCN', u'Scanner'),
        (u'NTW', u'Network'),
        (u'OTH', u'Other'),
    )
    name_device = models.CharField(max_length=100)
    type_device = models.CharField(max_length=100, choices=TYPE_DEVICE_CHOICES,blank=True, null=True)
    ip_device = models.IPAddressField(blank=True, null=True)
    model_device = models.CharField(max_length=100,blank=True, null=True)
    settings_device = models.TextField(blank=True, null=True)
    software = models.ManyToManyField(Software)
    source = models.ForeignKey(Source)
    def __unicode__(self):
        return u'%s %s' % (self.name_device, self.ip_device)
 
class People(models.Model):
    name_people = models.CharField(max_length=100)
    role_people = models.CharField(max_length=100,blank=True, null=True)
    office_manager = models.BooleanField()
    phone_people = models.CharField(max_length=100,blank=True, null=True)
    device = models.ManyToManyField(Device)
    notes_people = models.TextField(blank=True, null=True)
 
    def __unicode__(self):
        return u'%s %s' % (self.name_people, self.phone_people)
         
class Office(models.Model):
    name_office = models.CharField(max_length=100, verbose_name='name')
    address = models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(max_length=100,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    zip = models.CharField(max_length=100,blank=True, null=True)
    ip_office = models.IPAddressField(verbose_name='network segment',blank=True, null=True)
    phone_office = models.CharField(max_length=100,verbose_name='phone',blank=True, null=True)
    notes_office = models.TextField(verbose_name='notes',blank=True, null=True)
    billing_code = models.CharField(max_length=100,blank=True, null=True)
    miles = models.CharField(max_length=100,blank=True, null=True)
    monthly_fees = models.CharField(max_length=1000,blank=True, null=True)
    connection = models.TextField(blank=True, null=True)
    people = models.ManyToManyField(People,blank=True, null=True)
    device = models.ManyToManyField(Device,blank=True, null=True)
    source = models.ManyToManyField(Source,blank=True, null=True)
    ms = models.BooleanField()
    pho = models.BooleanField()
    def __unicode__(self):
        return self.name_office
      
   
class Ticket(models.Model):
    date_ticket = models.DateTimeField()
    subject_ticket = models.CharField(max_length=100)
    details_ticket = models.TextField(blank=True, null=True)
    scheduled_ticket = models.DateField()
    ready = models.BooleanField()
    waiting_on = models.TextField(blank=True, null=True)
    closed = models.BooleanField()
    office = models.ForeignKey(Office)
    people = models.ForeignKey(People)
    device = models.ForeignKey(Device)
    miles = models.CharField(max_length=100,blank=True, null=True)
    hours = models.CharField(max_length=100,blank=True, null=True)
    total_charge = models.CharField(max_length=100,blank=True, null=True)
    add_to_special_settings = models.BooleanField()
 
    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.date_ticket, self.subject_ticket, self.details_ticket, self.scheduled_ticket, self.ready, self.waiting_on, self.closed, self.office, self.people, self.device, self.miles, self.hours, self.total_charge, self.add_to_special_settings)
