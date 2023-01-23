from django.shortcuts import render,HttpResponse, redirect #กระโดดทำงานไปเราเต้อตัวอื่นได้


# Create your views here.
def profile(request):
    return render(request, 'profile.html')


def edu(request):
    return render(request, 'edu.html')


def interest(request):
    return render(request, 'interest.html')


def influ(request):
    return render(request, 'influ.html')


def product(request):
    return render(request, 'product.html')


def test(request):
    return render(request, 'test.html')


def showMydataGroup(request):
    name = "yyy"
    surname = "sriyowong"
    gender = "female"
    status = "student"
    educations = "rmuti kkc"

    return render(request, 'showMydataGroup.html',
                  {'name': name, 'surname': surname, 'gender': gender, 'status': status, 'educations': educations})


def showMyData(request):
    name = "Tanyarat"
    surname = "Sriyowong"
    nickname = "Butter"
    gender = "Female"
    status = "Student"
    hometown = "Khon kaen"
    age = "21"
    hobby = "Cooking"
    birthdate = "May 12, 2001"
    favsubject = "Python"
    productlist = [
        ['เบสท์ฟู้ดส์ผงฟูดับเบิลแอ็คติง', '69.00', 'images/co1.jpg'],
        ['แป้งเค้ก ตราริบบิ้น', '70.00', 'images/co2.jpg'],
        ['ยีสต์', '159.00', 'images/co3.jpg'],
        ['ครีมชีส', '129.00', 'images/co4.jpg'],
        ['วิปครีม', '119.00', 'images/co5.jpg'],
        ['กลิ่นวนิลลาบัตเตอร์', '39.00', 'images/co6.jpg'],
        ['บิสคอฟ โลตัส', '189.00', 'images/co7.jpg'],
        ['นูลเทลล่า (ถัง)', '1149.00', 'images/co8.jpg'],
        ['เนย', '99.00', 'images/co9.jpg'],
        ['ชา', '279.00', 'images/co10.jpg'],
        ]
    return render(request, 'lab10.html',
                  {"fname": name, "lname": surname, "nick": nickname, "gen": gender, "sta": status,
                   "home": hometown, "old": age, "hob": hobby, "birth": birthdate, "fav": favsubject,
                   "product": productlist})

from profileApp.models import *
productList = []
def showOurProduct(request):
    # product = Product('p0001','mouse', 'Aser', '500.00', '120')
    # productList.append(product)
    # product = Product('p0002', 'keyboard', 'Aser', '1200.00', '120')
    # productList.append(product)
    # product = Product('p0003', 'screen', 'Samsung', '3700.00', '120')
    # productList.append(product)
    context = {'products': productList}
    return render(request,'showOurProduct.html',context)

def newProduct(request):
    if request.method == 'POST': #submit ข้อมูลจากฟอร์มมา
        id = request.POST['id']
        name = request.POST['name']
        brand = request.POST['brand']
        price = request.POST['price']
        net = request.POST['net']
        product = Product(id, name, brand, price, net)
        productList.append(product)
        return  redirect ('showOurProduct')
    else: return render(request,'frmProductNormal.html')

from profileApp.form import *
def frmProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            name = form.get('name')
            brand = form.get('brand')
            price = form.get('price')
            net = form.get('net')
            product = Product(id, name, brand,price, net)
            productList.append(product)
            return redirect('showOurProduct')
        else:
            form = ProductForm(form)

    else:
        form = ProductForm ()
    context = {'form':form}
    return render(request,'frmProduct.html',context)


