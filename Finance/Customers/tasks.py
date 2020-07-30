from yahoo_fin.stock_info import get_data
import pandas as pd
from background_task import background
from Finance.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import Stocks,Customer
from django.contrib.auth.models import User

@background(schedule=120)
def bg_task():
    customers = Customer.objects.all()
    for customer in customers:
        stock = customer.companies_invested
        print(stock)
        data = get_data(str(stock))
        df = pd.DataFrame(data)
        close_data=df['adjclose']
        percent_change = close_data.pct_change()
        last_percentage = percent_change[-1]
        if last_percentage >= 0.02:
            ''' 
            # Action to be taken
            user = User.objects.get(username=customer.user)
            email = user.email
            # plotting RSI
            # difference in price from previous day
            delta = close_data.diff(1)
            delta.dropna()
            # get positive gain and negative gain (loss)
            up = delta.copy()
            down = delta.copy()
            up[up<0]=0
            down[down>0]= 0
            period = 14
            #calculate avg gain and avg loss
            avg_gain = up.rolling(window=period).mean()
            avg_loss = abs(down.rolling(window=period).mean())
            #calculate relative strength (RS)
            RS = avg_gain / avg_loss
            #calutating rsi
            RSI = 100.0 -(100.0 / (1.0 + RS))
            # RSI visually
            pass'''
            subject = f'Finance Buzz Stock Notification for {stock}'
            message = f'{stock} is giving a return of {round(last_percentage*100)} '
            user = User.objects.get(username=customer.user)
            email = user.email
            recepient = str(email)
            print(recepient)
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)

