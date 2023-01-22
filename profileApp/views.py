from django.shortcuts import render


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
    name = "tanyarat"
    surname = "sriyowong"
    nickname = "butter"
    gender = "female"
    status = "student"
    hometown = "khon kaen"
    age = "21"
    hobby = "cooking"
    birthdate = "may 12, 2001"
    favsubject = "python"
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
