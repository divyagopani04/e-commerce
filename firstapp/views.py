from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.db.models import Avg
import base64

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import razorpay

# Create your views here.

from backend.models import productdata
from backend.models import contactinfo
from backend.models import billing_details
from backend.models import userorder

from firstapp.models import registerfront
from firstapp.models import cart
from firstapp.models import customerreview


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def homepage(request):
    currency = 'INR'
    amount = 20000 # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                    currency=currency,
                                                    payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request, 'payment.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

    # only accept POST request.
    if request.method == "POST":
        try:
        
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000 # Rs. 200
                try:

                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)

                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:

                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:

                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:

            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
    # if other than POST request is made.
        return HttpResponseBadRequest()



def header(request):

    return render(request, 'header1.html')


def registeruser(request):

    fname = ''
    lname = ''
    email = ''
    password = ''

    if request.method == 'POST':

        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']

        mydata = registerfront.objects.filter(email=email, password=password)

        if mydata.count() > 0 :
            return  redirect('/register')

        else :
            encoded_text = base64.b64encode(password.encode()).decode()
            a = registerfront(fname=fname, lname=lname, email=email, password=encoded_text)
            a.save()
            return redirect('/')

    return render(request,'registerfront.html')

def loginuser(request):

    email = ''
    password = ''

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        encoded_text = base64.b64encode(password.encode()).decode()

        mydata = registerfront.objects.filter(email=email, password=encoded_text)

        if mydata.count() > 0 :

            admin = mydata.get()
            request.session['username'] = admin.id
            request.session['userfname'] = admin.fname
            # print(request.session['userfname'])

            return redirect('/')
        else :
            return  redirect('/loginuser')

    return render(request, 'loginfront.html')

def logoutuser(request):

    del request.session['username']
    del request.session['userfname']
    return redirect('/')

def index(request):


    # username = request.session['userfname']

    # x = registerfront.objects.get(password=username)

    mydata = productdata.objects.all().values()
    obj= productdata.objects.all().order_by('-id')

    return render(request, 'index.html',{'data':mydata,'obj':obj})

def about(request):
    return render(request, 'about.html')

def blogdetails(request):
    return render(request, 'blog-details.html')

def bloggrid(request):
    return render(request, 'blog-grid.html')

def blog(request):
    return render(request, 'blog.html')

def cartgrocery(request):
    return render(request, 'cart-grocery.html')

def cartpharmacy(request):
    return render(request, 'cart-pharmacy.html')

def addcart(request,id):

    if 'username' not in  request.session:
        return redirect('/loginuser')
    
    userid = request.session['username']
    
    d = cart.objects.filter(productid=id,userid=userid).values()

    if d:
        userdata = d[0]


    if d:
        print("Already exist in cart!!!")
        qty = int(userdata['quantity'])+1

        cart.objects.filter(id=userdata['id']).update(quantity=str(qty),total=str(qty*int(userdata['price'])))
        return redirect('/viewcart')
    
    else:
        mydata = productdata.objects.get(id=id)
        
        # if 'mydata.quantity > 0': 
        #     'mydata.quantity = mydata.quantity - 1'
        #     mydata.save()

        price = int(mydata.price)
        quantity = 1

        x = cart(
            userid=userid,
            productid=mydata.id,
            product=mydata.name,
            discription=mydata.discription,
            image=mydata.image,
            price=mydata.price,
            quantity=str(quantity),
            total= str(price * quantity),
            discount=mydata.discount,
        )
        
        x.save()

        return redirect('/viewcart')

def remove_cart_item(request,id):
    
    mydata = cart.objects.get(id=id)
    mydata.delete()

    return redirect('/viewcart')

def addajax(request):

    return redirect(request,'cart.html')

def update_quantity(request):
    if request.method == 'POST' and request.is_ajax():
        cart_id = request.POST.get('cart_id')
        action = request.POST.get('action')

        cart_item = get_object_or_404(Cart, id=cart_id)

        if action == 'add':
            cart_item.quantity += 1
        elif action == 'minus' and cart_item.quantity > 1:
            cart_item.quantity -= 1

        cart_item.save()
        return JsonResponse({'quantity': cart_item.quantity, 'total': cart_item.total})

    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def viewcart(request):
    
    userid = request.session['username']

    # Retrieve the page number from the request
    page_number = request.GET.get('page')
    
    if request.method == 'POST':
        if 'search' in request.POST:
            query = request.POST['search']
            myobj = cart.objects.filter(product__icontains=query, userid=userid).all()    
        else:
            myobj = cart.objects.filter(userid=userid).all()
    else:
        myobj = cart.objects.filter(userid=userid).all()

    # Paginate the query set
    paginator = Paginator(myobj, 2)  # Show 2 items per page
    page_obj = paginator.get_page(page_number)

    subtotal = 0
    for x in page_obj:
        subtotal = subtotal + int(x.total)

    return render(request, 'cart.html', {'subtotal':subtotal,"page_obj": page_obj})

def checkoutgrocery(request):
    return render(request, 'checkout-grocery.html')

def checkoutpharmacy(request):
    return render(request, 'checkout-pharmacy.html')

def checkout(request):

    userid = request.session['username']

    currency = 'INR'
    amount = 20000 # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                    currency=currency,
                                                    payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    bcountry = ''
    bfirstname = ''
    blastname = ''
    bcompanyname = ''
    baddress = ''
    bcity = ''
    bstate =''
    bzipcode = ''
    bemail = ''
    bphone = ''
    bmessage = ''        

    if request.method == 'POST':
        bcountry = request.POST['bcountry']
        bfirstname = request.POST['bfirstname']
        blastname = request.POST['blastname']
        bcompanyname = request.POST['bcompanyname']
        baddress = request.POST['baddress']
        bcity = request.POST['bcity']
        bstate = request.POST['bstate']
        bzipcode = request.POST['bzipcode']
        bemail = request.POST['bemail']
        bphone = request.POST['bphone']
        bmessage = request.POST['bmessage']

        obj = billing_details(
            bcountry=bcountry,
            bfirstname=bfirstname,
            blastname=blastname,
            bcompanyname=bcompanyname,
            baddress=baddress,
            bcity=bcity,
            bstate=bstate,
            bzipcode=bzipcode,
            bemail=bemail,
            bphone=bphone,
            bmessage=bmessage,
            buserid=userid,
        )
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        obj.save()

    # pass the values

    mydata = cart.objects.filter(userid=userid).all()

    subtotal = 0
    for x in mydata:
        subtotal = subtotal + int(x.total)

    context['subtotal'] = subtotal
    context['mydata'] = mydata

    # order coading
    
    orderdata = cart.objects.filter(userid=userid).all()

    for data in orderdata:
        c = userorder(
            ouserid=userid,
            oproductid=data.productid,
            oproduct=data.product,
            oimage=data.image,
            odiscount=data.discount,
            oquantity=data.quantity,
            oprice=data.price,
            ototal=data.total,
        )
                                                            
        c.save()
    
    orderdata.delete()

    orders = userorder.objects.filter(ouserid=userid).all()

    context['orders'] = orders

    return render(request, 'checkout.html',context=context)

def comingsoon(request):
    return render(request, 'coming-soon.html')

def contact(request):

    cname = ''
    cemail = ''
    cphone = ''
    cbirthdate = ''
    cclinic = ''
    cdoctor = ''
    cmessage = ''

    if 'contact' in request.POST:
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        cphone = request.POST['cphone']
        cbirthdate = request.POST['cbirthdate']
        cclinic = request.POST['cclinic']
        cdoctor = request.POST['cdoctor']
        cmessage = request.POST['cmessage']

    info = contactinfo(
        cname=cname,
        cemail=cemail,
        cphone=cphone,
        cbirthdate=cbirthdate,
        cclinic=cclinic,
        cdoctor=cdoctor,
        cmessage=cmessage,
    )

    info.save()

    return render(request, 'contact.html')

def error(request):
    return render(request, 'error.html')

def faq(request):
    return render(request, 'faq.html')

def grocerydetails(request):
    return render(request, 'grocery-details.html')

def groceryproduct(request):
    return render(request, 'grocery-product.html')

def grocery(request):
    return render(request, 'grocery.html')

def pharmacydetails(request):
    return render(request, 'pharmacy-details.html')

def pharmacyproduct(request):
    return render(request, 'pharmacy-product.html')

def pharmacy(request):
    return render(request, 'pharmacy.html')

def portfoliodetails(request):
    return render(request, 'portfolio-details.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def productdetails(request,id):

    if 'username' not in  request.session:
        return redirect('/loginuser')
    
    userid = request.session['username']


    mydata = productdata.objects.get(id=id)
        
    
    if 'addreview' in request.POST:
        rating = request.POST['rating']
        review = request.POST['review']
        rname = request.POST['rname']
        remail = request.POST['remail']

        data = customerreview(
                userid=userid,
                productid=id,
                rating=rating,
                review=review,
                rname=rname,
                remail=remail,
        )
        data.save()
    
    myreview = customerreview.objects.filter(productid=id).all()
    avg_rating = myreview.aggregate(Avg('rating'))['rating__avg']

    return render(request, 'product-details.html',{'data':mydata, 'review':myreview, 'avg_rating': avg_rating})

def product(request):

    if 'search' in request.POST:
        query = request.POST['search']
        myobj = productdata.objects.filter(name__icontains=query).all()    

    else:
                
        myobj = productdata.objects.all().order_by('-id')


    return render(request, 'product.html',{'obj':myobj})

def store(request):
    return render(request, 'store.html')

def wishlistgrocery(request):
    return render(request, 'wishlist-grocery.html')

def wishlistpharmacy(request):
    return render(request, 'wishlist-pharmacy.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def myprofile(request): 

    return render(request, 'myprofile.html',)

def orderlist(request):

        userid = request.session['username']

        orders = userorder.objects.filter(ouserid=userid).all()
                                                            
        return render(request, 'order.html',{'orders':orders})

def delete_orderlist(request,id):

    mydata = userorder.objects.get(id=id)
    mydata.delete()

    return redirect('/orderlist')


