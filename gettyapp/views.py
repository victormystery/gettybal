from django.shortcuts import render
from .models import LoanApplication, Review
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from gettybalance import settings


# Create your views here.
def services(request):
    return render(request, 'services.html')


from django.contrib import messages

def gettybal(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')

        # Perform validation
        if not rating:
            messages.error(request, 'Please provide a rating.')
            HttpResponseRedirect('/gettybalance')

        review = Review(username=username, email=email, comment=comment, rating=rating)
        review.save()
        # return HttpResponseRedirect('gettybalance/')

    reviews = Review.objects.filter(approved=True)

    context = {
        'reviews': reviews
    }

    return render(request, 'index.html', context)



def apply_now(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        business_name = request.POST.get('business_name')
        email = request.POST.get('email')
        business_phone = request.POST.get('business_phone')
        mobile_phone = request.POST.get('mobile_phone')
        credit_score = request.POST.get('credit_score')
        industry = request.POST.get('industry')
        time_business = request.POST.get('time_business')
        anual_sales = request.POST.get('annual_sales')
        monthly_gross = request.POST.get('monthly_gross')

        loan_application = LoanApplication(
            first_name=first_name,
            last_name=last_name,
            business_name=business_name,
            email=email,
            business_phone=business_phone,
            mobile_phone=mobile_phone,
            credit_score=credit_score,
            industry=industry,
            time_business=time_business,
            anual_sales=anual_sales,
            monthly_gross=monthly_gross
        )

        if loan_application:
            loan_application.save()

            # Compose email message
            subject = 'Loan Application'
            message = f'''
                First Name: {first_name}
                Last Name: {last_name}
                Business Name: {business_name}
                Email: {email}
                Business Phone: {business_phone}
                Mobile Phone: {mobile_phone}
                Credit Score: {credit_score}
                Industry: {industry}
                Time in Business: {time_business}
                Annual Sales: {anual_sales}
                Monthly Gross: {monthly_gross}
            '''
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = 'devcaliban@gmail.com'  # Set the recipient email address

            # Send email
            send_mail(subject, message, from_email, [to_email])

    return render(request, 'apply_now.html')
