from django.shortcuts import render,redirect
from .models import Stocks,Customer
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ObjectDoesNotExist
from .form import UserSignup,UserSignin,Stockform
from django.contrib import messages
from .stocks import Stocks_data
from time import sleep
import xlwt

# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
            #return redirect('registration')
            return render(request, 'customers/signup.html', {'form': form})
        else:
            messages.error(request,'Form data is invalid, check the mail ID you have given')
            sleep(5)
            return render(request, 'customers/signup.html', {'form': form})
    else:
        form=UserSignup()
        return render(request,'customers/signup.html',{'form':form})

def login_site(request):
    form = UserSignin()
    return render(request,'customers/signin.html',{'form':form})

def login_action(request):
    print('button clicked')
    if request.method=='POST':
        form = UserSignin(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            try:
                if user is not None:
                    login(request,user)
                    sform= Stockform()
                    stock_info = []
                    load = Stocks_data()
                    stock_info = load.latest_data(benutzer=user)
                    loser = load.days_loser()
                    gainer = load.days_gainer()
                    return render(request,'customers/inside_profile.html',{'form':sform,'stock_info':stock_info,'loser':loser,'gainers':gainer})
                else:
                    messages.error(request,"Username and Password not matched")
            except ObjectDoesNotExist:
                messages.error(request,'INVALID USER')
    return redirect('login_site')

def logout_site(request):
    logout(request)
    return redirect('login_site')

def add_stock(request,user):
    if request.method=='POST':
        sform = Stockform(request.POST)
        if sform.is_valid():
            stock_name = sform.cleaned_data["companies_invested"]

            if not Stocks.objects.filter(Stock_name_symbol=stock_name.upper()).exists():
                b=Stocks(Stock_name_symbol=stock_name.upper())
                b.save()
            else:
                b = Stocks.objects.get(Stock_name_symbol=stock_name.upper())

            user = User.objects.get(username=user)
            if not Customer.objects.filter(user=user,companies_invested=b).exists():
                c = Customer(user=user,companies_invested=b)
                c.save()
            else:
                print("Stock already added")
                c = Customer(user=user, companies_invested=b)
            messages.success(request, "Stock has been added to your viewing list")
            stock_info = []
            load = Stocks_data()
            stock_info = load.latest_data(benutzer=user)
            loser = load.days_loser()
            gainer = load.days_gainer()
            sleep(5)
            sform = Stockform()
            return render(request,'customers/inside_profile.html',{'form':sform,'stock_info':stock_info,'loser':loser,'gainers':gainer})

def downloadable(request,company):
    print("Download button clicke")
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="statement.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("sheet 1")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold=True

    columns = ['Breakdown','Current','Year-2019','Year-2018','Year-2018']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style = xlwt.XFStyle()
    load = Stocks_data()
    stat_info = []
    stat_info = load.income_stat(company=company)

    for dic in stat_info:
        row_num = row_num + 1
        col_num = 0
        for key,value in dic.items():
            ws.write(row_num,col_num,value,font_style)
            col_num = col_num + 1

    wb.save(response)
    return response




