from django.utils import timezone
from django.shortcuts import render,redirect
import pytz
import datetime

from money.forms import SpendingForm

from .models import Money

# Create your views here.

def index(request):
    today = str(timezone.now()).split('-')
    money = Money.objects.all()
    for num in money:
        date = str(num.use_date).split(' ')[0]
        num.use_date = '/'.join(date.split('-')[1:3])

    form =SpendingForm()

    context = {
        'year' : today[0],
        'month' : today[1],
        'money' : money,
        'form' : form
    }

    if request.method == 'POST':
        data = request.POST
        use_date = data['use_date']
        cost = data['cost']
        detail = data['detail']

        use_date = timezone.datetime.strptime(use_date, "%Y/%m/%d")
        tokyo_timezone = pytz.timezone('Asia/Tokyo')
        use_date = tokyo_timezone.localize(use_date)
        use_date = use_date + datetime.timedelta(hours=9)

        Money.objects.create(
            use_date = use_date,
            detail = detail,
            cost = int(cost),
        )

        return redirect(to='/money')

    return render(request, 'money/index.html', context)