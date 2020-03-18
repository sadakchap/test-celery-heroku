from django.shortcuts import render
from accounts.tasks import test_mail, add, mul, xsum

def home(request):
    mail_res = test_mail.delay()
    add_res = add.delay(4, 5)
    mul_res = mul.delay(4,5)
    xsum_res = xsum.delay([1,2,3,4,5])
    context = {
        'mail_res': mail_res,
        'add_res': add_res,
        'mul_res': mul_res,
        'xsum_res': xsum_res,
    }
    return render(request, "home.html", context=context)
