from django.db import models
#custom billing codes
CODE_CHOICES = (
    (u'TSK',u'Task, non-billable'),
    (u'billing_code_here',u'Names of multiple offices, customers'),
)
#custom billing rates
TRIP_CHOICES = (
    (u'0', u'description'),
    (u'10', u'description'),
    (u'20', u'description'),
)



class Invoice(models.Model):



    date = models.DateField()
    email = models.EmailField(default='yourdefault@mail.com', help_text="office manager's email went here")
    billing_code = models.CharField(max_length=100, choices=CODE_CHOICES, help_text="to add new billing codes contact admin@thisapp.com - edit billing\models.py")
    invoice_description = models.TextField(default='default text template goes here for your ticket details e.g. who requested:(name)\ndevice worked on:(swr,hwr,model,ip)\nsymptom:\nproblem:\nsolution:\nperson who performed work:\nparts replaced:(none)\nfuture recommendations:\n',help_text="what work was done and description/qty of parts")
    parts = models.DecimalField(max_digits=10, decimal_places=2, default=u'0', help_text="enter price of parts")
    miles = models.IntegerField(default=0, help_text="miles travelled - fixed amounts, see table")
    mileage_rate = models.DecimalField(max_digits=10, decimal_places=3,  default=u'.555', 
help_text="federal mileage rate was used in this situation customize mileage_rate for default in file  billing\models.py file")
    trip_fee = models.DecimalField(max_digits=10, decimal_places=2, choices=TRIP_CHOICES, default=0, help_text="description of custom billing rates for travel")
    hours = models.DecimalField(max_digits=10, decimal_places=2,default=0, help_text=".30hr minimum, enter hours worked, round down to nearest .5hr")
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=u'75', help_text="more help text on custom rates")
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default='0')
    recurring = models.BooleanField(help_text="this check indicates this bill was created automatically from a monthly template in this situation")
    recurring_master = models.BooleanField(help_text="another custom field for this situation...")
    recurring_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default='0')

    def __unicode__(self):
        return (self.billing_code)




