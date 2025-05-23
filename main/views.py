from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages

from .models import Users, Dorixona, Caetegory_drug, Drug, Commentdrug, Card, Order


# Create your views here.

def index(request):
    reg = Users.objects.all()

    if request.method == "POST":
        regi = Users()
        regi.name = request.POST.get("name")
        regi.family = request.POST.get("family")
        regi.email = request.POST.get("email")
        regi.status = request.POST.get("status")
        regi.password = request.POST.get("password")
        regi.save()
        return redirect("home2")
    return render(request, 'pages/register.html', {'reg': reg})


# def index2(request):
#     regis = Users.objects.all()
#     if request.method == "POST":
#         name = request.POST.get("name")
#         password = request.POST.get("password")
#         user = Users.objects.get(name=name, password=password)
#         request.session['id'] = user.id
#         return redirect("home3")
#     return render(request, 'pages/login.html', {'regis': regis})


def dellsession(request):
    try:
        del request.session["id"]
        del request.session['card']
    except KeyError:
        pass
    return redirect("home2")


def index3(request):
    id = request.session.get("id")
    user = Users.objects.get(id=id)
    cat = Caetegory_drug.objects.all()
    return render(request, 'pages/index.html', {'user': user, 'cat': cat})


def cabinet(request, id):
    category_drug = Caetegory_drug.objects.all()
    id = request.session.get("id")
    user = Users.objects.get(id=id)
    dorixon = Dorixona.objects.filter(users_id=id)
    drugs = Drug.objects.filter(caetegorydorixona__users=id)
    cat = Caetegory_drug.objects.all()
    if request.method == "POST":
        dor = Dorixona()
        dor.title = request.POST.get("title")
        dor.article = request.POST.get("article")
        dor.email = request.POST.get("email")
        dor.users_id = int(user.id)
        dor.save()
        return redirect("cabinet")
    return render(request, 'pages/cabinet.html',
                  {'user': user, 'dorixon': dorixon, 'drugs': drugs, 'category_drug': category_drug, 'cat': cat})


def edituser(request, id):
    try:
        user = Users.objects.get(id=id)

        if request.method:

            if bool(request.FILES.get('img', False)) == True:
                img = request.FILES['img']
                user.name = request.POST.get("name")
                user.family = request.POST.get("family")
                user.email = request.POST.get("email")
                user.password = request.POST.get("password")
                user.img = img
                user.save()
            else:
                user.name = request.POST.get("name")
                user.family = request.POST.get("family")
                user.email = request.POST.get("email")
                user.password = request.POST.get("password")
                user.save()
            return redirect("cabinet", id=id)
        else:
            return render(request, "pages/cabinet.html", {"user": user})
    except Users.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def dorixona(request):
    id = request.session.get("id")
    user = Users.objects.get(id=id)
    dorixon = Dorixona.objects.all()
    cat = Caetegory_drug.objects.all()
    return render(request, 'pages/dorixona.html', {'user': user, 'dorixon': dorixon, 'cat': cat})


def dorixonadrug(request, dori_id):
    id = request.session.get("id")
    user = Users.objects.get(id=id)
    dorixon = Dorixona.objects.get(id=dori_id)
    dorix = Dorixona.objects.all()
    drug = Drug.objects.filter(caetegorydorixona_id=dori_id)
    cat = Caetegory_drug.objects.all()
    return render(request, 'pages/dorixonadrug.html',
                  {'user': user, 'dorixon': dorixon, 'cat': cat, 'drug': drug, 'dorix': dorix})


def categordrug(request, cid):
    id = request.session.get("id")
    user = Users.objects.get(id=id)
    dorix = Dorixona.objects.all()
    cat = Caetegory_drug.objects.all()
    catid = Caetegory_drug.objects.get(id=cid)
    drug = Drug.objects.filter(caetegorydrug_id=cid)
    return render(request, 'pages/categordrug.html',
                  {'user': user, 'cat': cat, 'drug': drug, 'dorix': dorix, 'catid': catid})


def drugcreate(request):
    id = request.session.get("id")
    user = Users.objects.get(id=id)
    dorixon = Dorixona.objects.get(id=id)
    dori = Dorixona.objects.filter(users_id=id)
    cat = Caetegory_drug.objects.all()
    drugs = Drug.objects.all()
    if request.method == "POST" and request.FILES.get('img'):
        drug = Drug()
        img = request.FILES['img']
        drug.title = request.POST.get("title")
        drug.price = request.POST.get("price")
        drug.article = request.POST.get("article")
        drug.caetegorydrug_id = request.POST.get("caetegorydrug_id")
        drug.caetegorydorixona_id = request.POST.get("caetegorydorixona_id")
        drug.img = img
        drug.save()
        return redirect("cabinet", id=user.id)
    return render(request, 'pages/createdrug.html',
                  {'user': user, 'dorixon': dorixon, 'cat': cat, 'drugs': drugs, 'dori': dori})


def drugedit(request, dori_id):
    id = request.session.get("id")
    user = Users.objects.get(id=id)
    dorixon = Dorixona.objects.filter(id=dori_id)
    dori = Dorixona.objects.filter(users_id=dori_id)
    cat = Caetegory_drug.objects.all()

    try:
        drug = Drug.objects.get(id=dori_id)

        if request.method == "POST":

            if bool(request.FILES.get('img', False)) == True:
                drug = Drug()
                img = request.FILES['img']
                drug.title = request.POST.get("title")
                drug.price = request.POST.get("price")
                drug.article = request.POST.get("article")
                drug.caetegorydrug_id = request.POST.get("caetegorydrug_id")
                drug.caetegorydorixona_id = request.POST.get("caetegorydorixona_id")
                drug.img = img
                drug.save()
            else:
                drug.title = request.POST.get("title")
                drug.price = request.POST.get("price")
                drug.article = request.POST.get("article")
                drug.caetegorydrug_id = request.POST.get("caetegorydrug_id")
                drug.caetegorydorixona_id = request.POST.get("caetegorydorixona_id")
            return redirect("cabinet", id=id)
        else:
            return render(request, "pages/drugedit.html",
                          {'user': user, 'dorixon': dorixon, 'cat': cat, 'drug': drug, 'dori': dori})
    except Users.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def drugdelete(request, id):
    id = request.session.get("id")
    if not id:
        return redirect('login')
    try:
        drug = Drug.objects.get(id=id)
        drug.delete()
        return redirect("cabinet", id=drug.caetegorydorixona.id)
    except Drug.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def categorucreate(request):
    id = request.session.get("id")
    user = Users.objects.get(id=id)
    if request.method == "POST":
        cat = Caetegory_drug()
        cat.title = request.POST.get("title")
        cat.save()
        return redirect("cabinet", id=id)
    return render(request, 'pages/createcategory.html', {'user': user})


def categoredit(request, tid):
    id = request.session.get("id")
    user = Users.objects.get(id=id)
    try:
        cat = Caetegory_drug.objects.get(id=tid)

        if request.method == "POST":
            cat.title = request.POST.get("title")
            cat.save()
            return redirect("cabinet", id=id)
        else:
            return render(request, 'pages/editcategory.html', {'user': user, 'cat': cat})
    except Caetegory_drug.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def drugdetail(request, cid):
    id = request.session.get("id")
    user = Users.objects.get(id=id)
    dorix = Dorixona.objects.all()
    cat = Caetegory_drug.objects.all()
    drug = Drug.objects.filter(caetegorydrug_id=cid)
    drugs = Drug.objects.get(id=cid)
    randomdrug = Drug.objects.all().order_by('?')[:3]
    coment = Commentdrug.objects.filter(comudrug_id=cid).order_by('-id')
    number = len(coment)
    if request.method == "POST":
        com = Commentdrug()
        com.article = request.POST.get("article")
        com.comusers_id = user.id
        com.comudrug_id = drugs.id
        com.save()
        return redirect("drugdetail", cid=cid)
    return render(request, 'pages/drugdetail.html',
                  {'user': user, 'drugs': drugs, 'cat': cat, 'drug': drug, 'dorix': dorix, 'randomdrug': randomdrug,
                   'coment': coment, 'number': number})


# def card(request):
#     user_id = request.session.get("id")
#     user = Users.objects.get(id=user_id)
#     drug = Drug.objects.all()
#     card = request.session.get('card', {})
#     cat = Caetegory_drug.objects.all()
#     dorix = Dorixona.objects.all()
#     total_price = sum(item['quantity'] * item['price'] for item in card.values())
#     if request.method == "POST":
#
#             us = Users.objects.get(id=user_id)
#             name = us.name
#             family = us.family
#             email = us.email
#
#             for  item in card.keys():
#
#
#                 # order = Check()
#                 # order.name = name
#                 # order.family = family
#                 # order.email = email
#                 # order.user_id = user_id
#                 # order.name = item['name']
#                 # order.price = item['price']
#                 # order.quantity = item['quantity']
#                 # order.total = total_price
#                 # order.save()
#                 # try:
#                 #     del request.session['card']
#                 #
#                 # except KeyError:
#                 #     pass
#                 return redirect('card')
#
#     return render(request, 'pages/card.html', {'user': user, 'card':card, 'total_price':total_price, 'cat':cat, 'dorix':dorix})


# def add_to_card(request, drug_id):
#     if 'card' not in request.session:
#         request.session['card'] = {}
#     card = request.session['card']
#     drug = Drug.objects.get(id=drug_id)
#     quantity = int(request.POST.get('quantity', 1))
#     if str(drug_id) in card:
#         card[str(drug_id)]['quantity'] += quantity
#     else:
#         card[str(drug_id)] = {
#             'name': drug.title,
#             'price': drug.price,
#             'quantity': quantity,
#             'img': drug.img.url,
#         }
#     request.session['card'] = card
#     return redirect('card')

def cardpage(request):
    id = request.GET['id']
    user_id = request.session.get("id")
    user = Users.objects.get(id=user_id)
    card = Card.objects.filter(user_id=user_id)
    total_price = sum(item['quantity'] * item['price'] for item in card.values())
    return render(request, 'pages/cardpage.html', {'card': card, 'user': user, 'total_price': total_price})


def card(request):
    user_id = request.session.get("id")
    user = Users.objects.get(id=user_id)
    drug = Drug.objects.all()
    card = Card.objects.filter(user_id=user_id)
    cat = Caetegory_drug.objects.all()
    dorix = Dorixona.objects.all()
    total_price = sum(item['quantity'] * item['price'] for item in card.values())
    if request.POST:
        for item in card:
            title = item.title
            qty = item.quantity
            price = item.price
            prod_id = item.id
            user_id = item.user_id
            order = Order()

            order.title = title
            order.price = price
            order.qty = qty
            order.prod_id = prod_id
            order.user_id = user_id
            order.save()

        card.delete()

        return redirect("card")
    return render(request, 'pages/card.html',
                  {'user': user, 'card': card, 'cat': cat, 'dorix': dorix, 'total_price': total_price})


def werajax(request, id):
    drug = Drug.objects.get(id=id)
    return render(request, "pages/werajax.html", {'drug': drug})


# def addajax(request):
#     id = request.GET['id']
#
#     prod = Drug.objects.get(id=id)
#     title = prod.title
#     price = prod.price
#     prid = prod.id
#     user_id = request.session.get("id")
#     cart = Card()
#     cart.title = title
#     cart.price = price
#     cart.quantity = 1
#     cart.prod_id = prid
#     cart.user_id = user_id
#     cart.save()
#     card = Card.objects.filter(user_id=user_id)
#     return render(request,"pages/ajax.html", {'card':card})

def addajax(request):
    id = request.GET['id']
    user_id = request.session.get("id")
    prod = Drug.objects.get(id=id)
    title = prod.title
    price = prod.price
    prid = prod.id
    try:
        # Проверяем, есть ли товар в корзине текущего пользователя
        cart = Card.objects.get(prod_id=prid, user_id=user_id)
        cart.quantity += 1
        cart.save()
    except Card.DoesNotExist:
        # Если товара нет в корзине, создаём новый элемент
        cart = Card()
        cart.title = title
        cart.price = price
        cart.quantity = 1
        cart.prod_id = prid
        cart.user_id = user_id
        cart.save()
    card = Card.objects.filter(user_id=user_id)
    return render(request, "pages/ajax.html", {'card': card})


def addcart(request, id, farm_id):
    prod = Drug.objects.get(id=id)

    title = prod.title
    price = prod.price
    prid = prod.id

    try:

        getcart = Card.objects.get(prod_id=prid)

        if getcart.prod_id == prid:
            getcart.quantity += 1
            getcart.save()
            return redirect('card')

    except Card.DoesNotExist:
        user_id = request.session.get("id")
        print(user_id)
        cart = Card()
        cart.title = title
        cart.price = price
        cart.quantity = 1
        cart.prod_id = prid
        cart.user_id = user_id
        cart.save()
        return redirect('card')


def plus(request):
    user_id = request.session.get("id")
    id = request.GET['id']
    getcart = Card.objects.get(id=id)
    getcart.quantity += 1
    getcart.save()
    card = Card.objects.filter(user_id=user_id)
    return render(request, "pages/ajax.html", {'card': card})


def minus(request):
    user_id = request.session.get("id")
    id = request.GET['id']
    getcart = Card.objects.get(id=id)
    getcart.quantity -= 1
    getcart.save()
    card = Card.objects.filter(user_id=user_id)
    return render(request, "pages/ajax.html", {'card': card})


def catdrug(request, cid):
    id = request.GET['id']
    print(id)
    catid = Caetegory_drug.objects.get(id=cid)
    drug1 = Drug.objects.filter(caetegorydrug_id=id)
    return render(request, "pages/catdrugpage.html", {'drug1': drug1, 'catid': catid})


# def minus(request, id):
#     take_cart = Card.objects.get(prod_id=id)
#     qty = take_cart.quantity - 1
#     take_cart.quantity = qty
#     take_cart.save()
#     return redirect("cart")


def dellproduct(request, drug_id):
    prod = Card.objects.get(id=drug_id)

    prod.delete()
    return redirect('card')


def clear_cart(request):
    prod = Card.objects.all()
    prod.delete()
    return redirect('card')


def dorixonapage(request):
    id = request.GET['id']
    drug3 = Drug.objects.filter(caetegorydorixona_id=id)
    dorixon2 = Dorixona.objects.get(id=id)
    return render(request, "pages/dorixonapage.html", {'drug3': drug3, 'dorixon2': dorixon2})


def poiskpage(request):
    user_id = request.session.get("id")
    user = Users.objects.get(id=user_id)
    q = request.GET['q']
    drug4 = Drug.objects.filter(title=q)
    return render(request, "pages/poisk.html", {'user': user, 'drug4': drug4})


# def index(request):
#     reg = Users.objects.all()
#
#     if request.method == "POST":
#         regi = Users()
#         regi.name = request.POST.get("name")
#         regi.family = request.POST.get("family")
#         regi.email = request.POST.get("email")
#         regi.status = request.POST.get("status")
#         regi.password = request.POST.get("password")
#         regi.save()
#         return redirect("home2")
#     return render(request, 'pages/register.html', {'reg': reg})

def registrpage(request):
    if request.method == "GET":
        regi = Users()
        regi.name = request.GET.get("name")
        regi.family = request.GET.get("family")
        regi.email = request.GET.get("email")
        regi.status = request.GET.get("status")
        regi.password = request.GET.get("password")
        regi.save()
    return HttpResponse("jr")


def index2(request):
    regis = Users.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = Users.objects.get(name=name, password=password)
        request.session['id'] = user.id
        return redirect("home3")
    return render(request, 'pages/login.html', {'regis': regis})


def login(request):
    return render(request, 'pages/cabinet.html')
