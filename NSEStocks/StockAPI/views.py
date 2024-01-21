
from rest_framework import generics
from rest_framework.response import Response
from .models import Index, DailyPrice, CSVFile
from .serializers import IndexSerializer, DailyPriceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CSVFileForm
from django.contrib import admin
from django.urls import path

class IndexList(generics.ListAPIView):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer

class DailyPriceList(generics.ListAPIView):
    serializer_class = DailyPriceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'open_price', 'high_price', 'low_price', 'close_price', 'shares_traded', 'turnover']

    def get_queryset(self):
        index_id = self.kwargs['index_id']
        return DailyPrice.objects.filter(index_id=index_id)



def index_detail(request, index_id):
    index = get_object_or_404(Index, pk=index_id)
    csv_files = CSVFile.objects.filter(index=index)

    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index-detail', index_id=index_id)
    else:
        form = CSVFileForm(initial={'index': index})

    return render(request, 'StockAPI/index_detail.html', {'index': index, 'csv_files': csv_files, 'form': form})


def delete_csv(request, csv_id):
    csv_file = get_object_or_404(CSVFile, pk=csv_id)
    index_id = csv_file.index.id
    csv_file.delete()
    return redirect('index-detail', index_id=index_id)


class IndexAdmin(admin.ModelAdmin):
    list_display = ['name']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('custom_view/', self.admin_site.admin_view(self.custom_view), name='custom-view'),
        ]
        return custom_urls + urls

    def custom_view(self, request):
        # Your custom view logic here
        return render(request, 'admin/your_app/custom_view.html')

admin.site.register(Index, IndexAdmin)
