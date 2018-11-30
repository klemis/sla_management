from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Country, Operator

#Drugim opcjonalnym argumentem jest nazwa klasy odpowiedzialnej za dostosowanie klasy i
#zmianę parametrów i sposobu wyświetlania w panelu administracyjnym.

class CountryAdmin(admin.ModelAdmin):
    pass

class OperatorAdmin(ImportExportModelAdmin):
	pass

# Register your models here.

admin.site.register(Country, CountryAdmin)
admin.site.register(Operator, OperatorAdmin)

# @admin.register(Person)
# class PersonAdmin(ImportExportModelAdmin):
#     pass
