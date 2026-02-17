from django.http import HttpResponse
from django.shortcuts import render

from .forms import ProductForm
from .models import Product

from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View


def home(request):
    # Выбираем 5 последних продуктов
    latest_products = Product.objects.order_by('-id')[:5]

    # Выводим их в консоль
    print('Вывод 5 последних продуктов:')
    for product in latest_products:
        print(f"id: {product.id}, Название: {product.name}, цена за покупку: {product.price}")

    return render(request, 'catalog/home.html', {'products': latest_products})


class ContactView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(f"Сообщение от {name}: {message}")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'
    paginate_by = 2


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')
