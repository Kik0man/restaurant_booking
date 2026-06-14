from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from .forms import BookingForm
from .models import Booking

class BookingView(LoginRequiredMixin, FormView):
    template_name = 'bookings/booking_form.html'
    form_class = BookingForm
    success_url = reverse_lazy('bookings:booking_success')

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user
        # Проверка на существующее активное бронирование
        existing = Booking.objects.filter(
            table=booking.table,
            date=booking.date,
            time=booking.time,
            status='active'
        ).exists()
        if existing:
            messages.error(self.request, "Этот столик уже забронирован на выбранное время.")
            return self.form_invalid(form)
        booking.save()
        messages.success(self.request, "Бронирование успешно создано!")
        return super().form_valid(form)

def booking_success_view(request):
    return render(request, 'bookings/booking_success.html')