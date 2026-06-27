from django.contrib import admin
from .models import Table, Booking

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['number', 'seats', 'location']
    list_filter = ['seats', 'location']
    search_fields = ['number']
    ordering = ['number']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'table', 'date', 'time', 'guests', 'status', 'created_at']
    list_filter = ['status', 'date', 'table']
    search_fields = ['user__username', 'user__email', 'table__number']
    date_hierarchy = 'date'
    ordering = ['-date', '-time']
    list_editable = ['status']   # быстро менять статус прямо из списка
    raw_id_fields = ['user', 'table']   # для удобства при большом количестве записей