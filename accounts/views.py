from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from bookings.models import Booking
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth import logout


class ProfileView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'accounts/profile.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-date', '-time')


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['date', 'time', 'guests']
    template_name = 'accounts/booking_edit.html'
    success_url = reverse_lazy('accounts:profile')  # исправлено

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user, status='active')

    def form_valid(self, form):
        messages.success(self.request, "Бронирование обновлено.")
        return super().form_valid(form)


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'accounts/booking_confirm_delete.html'
    success_url = reverse_lazy('accounts:profile')  # исправлено

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user, status='active')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Бронирование отменено.")
        return super().delete(request, *args, **kwargs)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('/')