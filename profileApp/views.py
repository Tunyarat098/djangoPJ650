from django.shortcuts import render, HttpResponse, redirect, get_object_or_404  # กระโดดทำงานไปเราเต้อตัวอื่นได้
from django.contrib import messages

import datetime
from profileApp.form import *


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


productList = []


def showOurProduct(request):
    # product = Product('p0001','mouse', 'Aser', '500.00', '120')
    # productList.append(product)
    # product = Product('p0002', 'keyboard', 'Aser', '1200.00', '120')
    # productList.append(product)
    # product = Product('p0003', 'screen', 'Samsung', '3700.00', '120')
    # productList.append(product)
    context = {'products': productList}
    return render(request, 'showOurProduct.html', context)


def newProduct(request):
    if request.method == 'POST':  # submit ข้อมูลจากฟอร์มมา
        id = request.POST['id']
        name = request.POST['name']
        brand = request.POST['brand']
        price = request.POST['price']
        net = request.POST['net']
        product = Product(id, name, brand, price, net)
        productList.append(product)
        return redirect('showOurProduct')
    else:
        return render(request, 'frmProductNormal.html')


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
            product = Product(id, name, brand, price, net)
            productList.append(product)
            return redirect('showOurProduct')
        else:
            form = ProductForm(form)

    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'frmProduct.html', context)


# assignment11

lstOurProduct = []


def listProduct(request):
    details = "instant noodles"
    name = "tanyarat sriyowong"
    date = datetime.datetime.now()
    return render(request, 'listProduct.html', {'lstProduct': lstOurProduct,
                                                'details': details, 'name': name,
                                                'date': date.strftime("%A %d-%m-%Y %H : %M")})


def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # form = form.cleaned_data
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            brand = form.cleaned_data['brand']
            type = form.cleaned_data['type']
            flavor = form.cleaned_data['flavor']
            amount = form.cleaned_data['amount']
            price = form.cleaned_data['price']
            member = form.cleaned_data['member']
            productnew = myProduct(id, name, brand, type, flavor, amount, price, member)
            lstOurProduct.append(productnew)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
            context = {'form': form}
            return render(request, 'inputProduct.html', context)

    else:
        form = ProductForm()
        context = {'form': form}
        return render(request, 'inputProduct.html', context)


# def product_retrieve(request):
#     product = Product.objects.all()
#     context = {'product' : product}
#     return render(request, 'product/retrieveAllProduct.html')

# from .models import *
# from profileApp.form import *
# def retrieveAllProduct(request, pid):
#     products = Product.objects.all()
#     context = {'products':products}
#     return render(request,'product/retrieveAllProduct.html',context)
# def retrieveOneProduct(request, pid):
#     product = Product.objects.get(pid=pid)
#     context = {'product':product}
#     return render(request,'product/retrieveOneProduct.html',context)
#
#
# from django.contrib import messages
# def createProduct(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, 'save laew jaa....')
#             return redirect('retrieveAllProduct')
#
#         else:
#             context = {'form' : form}
#             return  render(request, 'product/createProduct.html', context)
#
#     else:
#         form = ProductMForm()
#         context = {'form':form}
#         return render(request, 'product/createProduct.html',context)


def retrieveAllProduct(request):
    products = Product.objects.all()  # อ่ํานข้อมูลทุกเรคอร์ด All ในฐํานข้อมูลที่เชื่อมโดย Category
    context = {'products': products} #ask abt context #เชื่อมไปทำในฐานข้อมูลอัติโนมัติ คิวรี่มาทั้งหมด
    return render(request, 'product/retrieveAllProduct.html', context)  #รับลิสต์ไปวนลูปแสดงผล ส่งดิ๊ก productsเป็นลิสต์


def retrieveOneProduct(request, pid): #ฟังชั่นที่รับค่าที่แนบกับเราเตอร์ เอา pidที่ใช้เป็นเงื่อนไขในการค้นหา
    product = Product.objects.get(pid=pid)  # อ่ํานข้อมูลทุกเรคอร์ด One ในฐํานข้อมูลที่เชื่อมโดย Category ในเก็ทบอกเงทื่อนไข สีม่วงบอกชื่อแอทที่บิ้วในฐาน ด้านหลังคือค่าตัวแปรที่เรารับมา
    context = {'product': product} #ชื่อตัวแปรเฉยๆ แบบdata หรือไรก็ด้ะขอแค่เป็นดิ๊ก เขาแค่นิยมใช้คำนี้
    return render(request, 'product/retrieveOneProduct.html', context)


def createProduct(request):
    if request.method == 'POST':
        form = ProductMForm(request.POST)
        if form.is_valid(): #มีข้อมูลถูกต้องไหม
            form.save()
            messages.success(request, messages.SUCCESS, 'บันทึกข้อมูลสินค้าใหม่เรียบร้อย...')
            return redirect('retrieveAllProduct') #อ้างถึงชื่อของเราเต้อด้านหลังสุด ไม่ได้อ้างชื่อไฟล์ หรือไม่รีไดเรก็ได้  หรือจะเรียกฟังชั่นที่อยู่ด้านบนก็ด้ะ
        else:
            product = Product.objects.get(pid=request.POST['pid'])  # ask เชคว่าไพรมารี่ซ้ำไหม เทียบกับรหัสสินค้าในฐานข้อมูล ไปเทียบกับรหัสสินค้าที่เราป้อน
            if product:
                messages.error(request, messages.WARNING, 'รหัสสินค้าซ้ำกับที่มีอยู่แล้วในระบบ ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้')
    else:
        form = ProductMForm() #สร้างฟอมเปล่า
    context = {'form': form}
    return render(request, 'product/createProduct.html', context) #ask



def updateProduct(request, pid):
    product = get_object_or_404(Product,pid = pid) #ค้นหาตชจากpidmี่เราแนบมา ค้นหาเสร็จไปลงformด้านล่าง 404 คือฟังชั่นที่ค้นหา
    form = ProductMForm(data=request.POST or None, instance=product) #เอาโพรดีั๊กที่ค้นหา ลิ้งมาครั้งแรก ถ้าเ ปนการpostไปใส่ฟอร์ม เซฟปึ๊ปเอาข้อมูลแนบมากะับโพสไปใส่ในฟอร์ม หรือค่านอนไม่มีค่าใดๆ instatnce คือข้อมูลตั้งต้น เอาข้อมูลออบเจ็คโปรดัก๊ไปใสา่

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, messages.SUCCESS, 'แก้ไขข้อมูลสินค้าเรียบร้อย...')
            return redirect('retrieveAllProduct')
        else:
            context = {'form': form}
            messages.error(request, messages.WARNING,'ข้อมูลไม่สมบูรณ์ ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้')

    else:
        form.updateForm()
        context = {'form':form,'old_pid':product.pid}
        return render(request, 'product/updateProduct.html',context)

def deleteProductOld(request, pid): #กรณีใช้javascriptยืนยัน
    product = get_object_or_404(Product,pid = pid)
    if product:
        product.delete()
        messages.add_message(request, messages.ERROR, 'ลบเรียบร้อย...')
    else:
        messages.add_message(request,messages.ERROR,'ไม่สามารถลบข้อมูลสินค้าตามรหัสที่ระบุได้')
    return redirect('retrieveAllProduct')

def deleteProduct(request,pid=None): #แนบมากับเกต
    if request.method=="POST":
        pid = request.POST['pid']
        product = Product.objects.get(pid=pid)
        product.delete()
        return redirect('retrieveAllProduct')

    else:
        product = Product.objects.get(pid=pid)
        context = {'product':product}
        return render(request,'product/deleteProduct.html',context)



def empCreate(request):  # ฟังก์ชัน create พนักงานใหม่


    if request.method != 'POST':
        newForm = EmployeeForm(initial={'empid': 'auto'})
        return render(request, 'empCreate.html', {'form': newForm})
    else:
        newEmpID = genNewEmpID()
        request.POST._mutable = True
        request.POST['empid'] = newEmpID
        request.POST._mutable = False
        newForm = EmployeeForm(request.POST)
        if newForm.is_valid():
            newForm.save()
            messages.success(request, "New employee data saved...")
        return redirect('home')


def genNewEmpID():  # ฟังก์ชันส าหรับสร้ างรหัสพนักงานอัตโนมัติรูปแบบ EmpYYYY-XXXXX เช่น EMP2022-00015เป็นฟังก์ชันธรรมดา ไม่รับ request

    currentYear = str(datetime.date.today().year)
    lastEmployee = Employee.objects.last()
    if lastEmployee:
        lastID = lastEmployee.empid
        lastID = lastID[8:]
        newID = int(lastID) + 1
        newID = str(newID)
        addZero = 5 - len(newID)
        newID = ("0" * addZero) + newID
    # for i in range(len(newID), 5):
    # newID = '0' + newID
        return "Emp" + currentYear + "-" + newID
    else:
        return "Emp" + currentYear + "-" + "00001"


def groupproduct(request):
    return render(request, 'groupproduct.html')
