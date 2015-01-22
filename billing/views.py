import csv
from django.http import HttpResponse
from mysite.billing.models import Invoice
from django.shortcuts import render_to_response

def home(request):
    html= ('Billing Application  | <a href="/admin">login</a>')    
#    return HttpResponse(html)
    return render_to_response('index.html', {'home_con': html})

def invoices(request):
    return render_to_response('billing/invoices.html', {'invoices': Invoice.objects.all().order_by('-date')})


def invoices_detail(request, invoice_id):
    return render_to_response('billing/invoices_detail.html', {'invoice': Invoice.objects.get(pk=invoice_id)})


def csv_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=example.csv'
    writer = csv.writer(response)

    onebill = Invoice.objects.all()
#    allbill = Invoice.ojbects.all()
    for bill in onebill:
        writer.writerow([bill.billing_code, bill.total])


#    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
#    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response



