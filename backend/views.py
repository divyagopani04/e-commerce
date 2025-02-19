from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse

from backend.models import reg
from backend.models import maincategory
from backend.models import subcategory
from backend.models import productdata
from backend.models import imagedata 
from django.core import serializers


# Create your views here.

def dashboard(request):

    if 'username' not in request.session:
         
        print('hello....')
        return redirect('/dashboard')

    return render(request,'home.html')

def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
    
        mydata = reg.objects.filter(email=email)

        if mydata.count() > 0 :
            print("Please enter valid email address!!!")
            return  redirect('/register')
        else :
            new_user = reg(name=name,email=email,password=password)
            new_user.save()

        return redirect('/dashboard')

    return render(request, 'registeruser.html')


def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        mydata = reg.objects.filter(email=email, password=password)

        if mydata.count() > 0 :

            admin = mydata.get()
            request.session['username'] = admin.id
            print(admin)

            return redirect('/dashboard')
        else :
            return  redirect('/login')
    
    return render(request, 'login.html')


def update(request,id):

    user = reg.objects.get(id=id)

    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        user.name = name
        user.email = email
        user.password = password

        user.save()

        return redirect('/viewdata')

    return render(request,'updateuser.html',{'user':user})

def delete(request,id):

    mydata = reg.objects.get(id=id)
    mydata.delete()

    return redirect('/viewdata')


def viewdata(request):

    if 'username' not in request.session:

        return redirect('/')
        
    user = reg.objects.all().values()

    return render(request,'viewuser.html',{'user':user})

def logout(request):

    request.session.delete()

    return redirect('/login')


def addcategory(request):
    category = ''

    if request.method == 'POST':
        category = request.POST['category']
    
        a = maincategory(category=category)
        a.save()

        return redirect('/dashboard')
      
    return render(request, 'addcategory.html')

def viewcategory(request):

    if 'username' not in request.session:

        return redirect('/')
        
    mydata = maincategory.objects.all().values()

    return render(request,'viewcategory.html',{'data':mydata})

def deletecategory(request,id):

    mydata = maincategory.objects.get(id=id)
    mydata.delete()

    return redirect('/viewcategory')

def updatecategory(request,id):

    mydata = maincategory.objects.get(id=id)

    if request.method=="POST":
        category = request.POST['category']

        mydata.category = category
    
        mydata.save()

        return redirect('/viewcategory')

    return render(request,'updatecategory.html',{'data':mydata})

def change(request,id):

    if 'username' not in request.session:

        return redirect('/')
        
    mydata = maincategory.objects.get(id=id)

    if mydata.status == 0:
        mydata.status = 1
    else:
        mydata.status = 0

    mydata.save()

    return redirect('/viewcategory')


def addsubcate(request):

    subitem = ''
    item = ''

    id = request.session['username']

    if request.method == 'POST':
            
        subitem = request.POST['subitem']
        item = request.POST['item']

        a=subcategory(subitem=subitem, item=item,userid=id)
        a.save()

        return redirect('/viewsubcate')
    
    mydata = maincategory.objects.all().values()
    return render(request, 'addsubcate.html',{'data':mydata})


def viewsubcate(request):

    if 'username' not in request.session:

        return redirect('/')
        
    mydata = subcategory.objects.all().values()

    return render(request,'viewsubcate.html',{'data':mydata})

def deletesubcate(request,id):

    mydata = subcategory.objects.get(id=id)
    mydata.delete()

    return redirect('/viewsubcate')

def updatesubcate(request,id):

    mydata = subcategory.objects.get(id=id)

    if request.method=="POST":
        item = request.POST['category']
        subitem = request.POST['subcategory']

        mydata.item = item
        mydata.subitem = subitem

        mydata.save()

        return redirect('/viewsubcate')

    return render(request,'updatesubcate.html',{'data':mydata})

def subcatechange(request,id):

    if 'username' not in request.session:

        return redirect('/')
        
    mydata = subcategory.objects.get(id=id)

    if mydata.substatus == 0:
        mydata.substatus = 1
    else:
        mydata.substatus = 0

    mydata.save()

    return redirect('/viewsubcate')

def addproduct(request):

    frm = imagedata()

    if request.method == 'POST':

        frm = imagedata(request.POST, request.FILES)
        frm.save()

    mydata = maincategory.objects.all().values()
    subcate = subcategory.objects.all().values()
    return render(request, 'addproduct.html',{'data':mydata, 'subcate':subcate , 'frm':frm})

def viewproduct(request):

    if 'username' not in request.session:

        return redirect('/')
        
    mydata = productdata.objects.all().values()
    category = maincategory.objects.all().values()
    subcate = subcategory.objects.all().values()

    return render(request,'viewproduct.html',{'data':mydata , 'category':category , 'subcate':subcate})

def deleteproduct(request,id):

    mydata = productdata.objects.get(id=id)
    mydata.delete()

    return redirect('/viewproduct')

def updateproduct(request,id):

    mydata = productdata.objects.get(id=id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(mydata.image) > 0:
                mydata.image = request.FILES['image']
        mydata.name = request.POST.get('name')
        mydata.discription = request.POST.get('discription')
        mydata.price = request.POST.get('price')
        mydata.quantity = request.POST.get('quantity')
        mydata.discount = request.POST.get('discount')

        mydata.save()

        return redirect('/viewproduct')

    return render(request,'updateproduct.html',{'data':mydata})

def pchange(request,id):

    if 'username' not in request.session:

        return redirect('/')
        
    mydata = productdata.objects.get(id=id)
    print(mydata)

    if mydata.pstatus == '0':
        mydata.pstatus = '1'
    else:
        mydata.pstatus = 0
    print(mydata)

    mydata.save()

    return redirect('/viewproduct')



def allreguser(request):

    # data = reg.objects.all().values()
    json_data = {'name':'divya'}
    SomeModel_json = serializers.serialize("json", reg.objects.all())
    data = {"SomeModel_json": SomeModel_json}
    return JsonResponse({'data':data})







