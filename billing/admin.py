import csv
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib import admin
from mysite.billing.models import Invoice
from copy import deepcopy
import decimal

def month_action(modeladmin,request,queryset):
    queryset.all()
    month_action.short_description = "copy to next month"
    invoices = queryset.all()
    for i in invoices:
        old = deepcopy(i)
        old.id = None
        old.date = u'2015-01-01' 
        old.recurring_master = False
        old.save()
    return HttpResponse('copies created \n <a href="\">return</a>')

def export_month(modeladmin, request, queryset):
    queryset.all()
    export_month.short_description = "export for star"
    
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=example.csv'
    writer = csv.writer(response)

    one_bill = queryset.all()
    for bill in one_bill:
        writer.writerow([bill.billing_code, bill.total])

    return response

def export_invoice(modeladmin, request, queryset):
    queryset.all()
    export_invoice.short_description = "export for invoice detail"

    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=invoice.csv'
    writer = csv.writer(response)

    one_invoice = queryset.all()
    for invoice in one_invoice:
        writer.writerow([invoice.date, invoice.email, invoice.billing_code])
        writer.writerow([invoice.invoice_description])
        writer.writerow([invoice.parts, invoice.hours, invoice.miles, invoice.trip_fee, invoice.total])
    
    return response



def email_invoice(modeladmin, request, queryset):
    queryset.all()
    email_invoice.short_description = "email invoice(s)"

    e_invoice = queryset.all()
    
    for invoice in e_invoice:
        subj = 'invoice for ticket # %s, date %s' % (invoice.id, invoice.date)
        mesg = 'Date of Service: %s\nDetail: %s\n\n\n\nparts:$%s\ntravel: %smi at $%s/mi trip fee $%s\ntime: %shr at $%s/hr\ntotal: $%s\n\n\n\n\n(For informational purposes only; This is not a bill; Do not remit.)' % (invoice.date, invoice.invoice_description, invoice.parts,invoice.miles,invoice.mileage_rate,invoice.trip_fee,invoice.hours,invoice.hourly_rate,invoice.total)
        email = EmailMessage(subj,mesg, to=[invoice.email])
        email.send()
    
    return HttpResponse('email(s) sent \n <a href="\"> return </a>')



from django.db.models.fields import CharField
def clone_objects(objects):
    def clone(from_object):
        args = dict([(fld.name, getattr(from_object, fld.name))
                for fld in from_object._meta.fields
                        if fld is not from_object._meta.pk]);

        return from_object.__class__.objects.create(**args)

    if not hasattr(objects,'__iter__'):
       objects = [ objects ]

    # We always have the objects in a list now
    objs = []
    for object in objects:
        obj = clone(object)
        obj.save()
        objs.append(obj)

def action_clone(modeladmin, request, queryset):
    objs = clone_objects(queryset)
action_clone.short_description = "Copy the selected objects"



class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id','date','email','billing_code','parts','miles','hours','total','recurring')
    search_fields = ['invoice_description','billing_code']
    save_on_top = True
    radio_fields = {"trip_fee": admin.HORIZONTAL}
    date_hierarchy = 'date'
    list_filter = ('recurring','recurring_master','billing_code',)
    fieldsets = [
        ('Simple',               {'fields': ['date','billing_code','email','invoice_description']}),
        ('Billing',         {'fields': ['parts','miles','mileage_rate','trip_fee','hours','hourly_rate']}),
        ('Monthly Billing', {'fields': ['recurring','total','recurring_master','recurring_amount'], 'classes': ['collapse']}),
    ]

    actions = [export_month, export_invoice, email_invoice,action_clone,month_action]

    def save_model(self, request, obj, form, change):
        if obj.recurring == False:
            decimal.getcontext().prec = 4
            obj.total = decimal.Decimal(obj.parts + (obj.mileage_rate * obj.miles) + obj.trip_fee + (obj.hourly_rate * obj.hours))
            obj.save()
        else:
            obj.save()

admin.site.register(Invoice, InvoiceAdmin)








