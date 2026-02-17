from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from blogs.models import Record
from django import forms


class RecordListView(ListView):
    model = Record
    template_name = 'blogs/records_list.html'
    context_object_name = 'records'

    def get_queryset(self):
        return Record.objects.filter(is_published=True)


class RecordDetailView(DetailView):
    model = Record
    template_name = 'blogs/record_detail.html'
    context_object_name = 'record'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.number_of_views += 1
        obj.save()

        if obj.number_of_views == 100:
            print(f"Статья {obj.title} популярна, набрала 100 просмотров.\nПисьмо отправлено.")
        return obj


class RecordCreateView(CreateView):
    model = Record
    fields = ['title', 'content', 'is_published', 'image']
    template_name = 'blogs/record_form.html'
    success_url = reverse_lazy('blogs:records_list')


class RecordUpdateView(UpdateView):
    model = Record
    fields = ['title', 'content', 'is_published', 'image']
    template_name = 'blogs/record_form.html'

    def get_success_url(self):
        return reverse('blogs:record_detail', kwargs={'pk': self.object.pk})


class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'blogs/record_confirm_delete.html'
    success_url = reverse_lazy('blogs:records_list')


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'content', 'image', 'is_published']
