# admin.py
from django.contrib import admin
from .models import Index, DailyPrice, CSVFile
from django import forms
from django.forms import inlineformset_factory

class DailyPriceInline(admin.TabularInline):
    model = DailyPrice
    extra = 1

class CSVFileInlineForm(forms.ModelForm):
    class Meta:
        model = CSVFile
        fields = ['file']

CSVFileInlineFormSet = inlineformset_factory(Index, CSVFile, form=CSVFileInlineForm, extra=1)

class CSVFileInline(admin.TabularInline):
    model = CSVFile
    formset = CSVFileInlineFormSet

class IndexAdmin(admin.ModelAdmin):
    inlines = [DailyPriceInline, CSVFileInline]

admin.site.register(Index, IndexAdmin)
admin.site.register(DailyPrice)
admin.site.register(CSVFile)
