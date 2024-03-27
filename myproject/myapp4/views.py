from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from myapp3.models import Product
from myapp4.forms import CreateProductForm


def add_product(request):
    if request.method == 'POST' and request.FILES:
        form = CreateProductForm(request.POST, request.FILES)
        message = 'Ошибка данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            # slug = form.cleaned_data['slug']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product(
                name=name,
                # slug=slug,
                price=price,
                quantity=quantity,
                description=description,
                image=image,
            )
            product.save()
            message = 'Продукт сохранён'
    else:
        form = CreateProductForm()
        message = 'Заполните форму'

    context = {
        'title': 'Добавление продукта',
        'form': form,
        'message': message
    }

    return render(request, 'myapp4/add_product_form.html', context=context)


def change_product(request, product_id=None):
    if product_id is None:
        return redirect('myapp4:add_product')

    if request.method == 'POST' and request.FILES:
        form = CreateProductForm(request.POST, request.FILES)
        message = 'Ошибка данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            # slug = form.cleaned_data['slug']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)

            Product.objects.filter(id=product_id).update(
                name=name,
                price=price,
                quantity=quantity,
                description=description,
                image=image,
            )

            # slug=slug,

            # product.save()
            message = 'Продукт сохранён'
    else:
        form = CreateProductForm()
        message = 'Заполните форму'

    context = {
        'title': 'Добавление продукта',
        'form': form,
        'message': message
    }

    return render(request, 'myapp4/add_product_form.html', context=context)
