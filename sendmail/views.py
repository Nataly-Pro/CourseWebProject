from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from sendmail.forms import MailingCreateForm
from sendmail.models import Message, Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingCreateForm
    success_url = reverse_lazy('sendmail:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingCreateForm
    #success_url = reverse_lazy('sendmail:mailing_list')

    def get_success_url(self):
        return reverse('sendmail:mailing_view', args=[self.kwargs.get('pk')])


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('sendmail:mailing_list')


class MessageCreateView(CreateView):
    model = Message
    fields = ('title', 'content',)
    success_url = reverse_lazy('sendmail:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('title', 'content',)

    def get_success_url(self):
        return reverse('sendmail:message_view', args=[self.kwargs.get('pk')])


class MessageDetailView(DetailView):
    model = Message
    template_name = 'sendmail/message_detail.html'


class MessageListView(ListView):
    model = Message
    extra_context = {
        'title': 'Список Ваших сообщений'
    }


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('sendmail:home')
