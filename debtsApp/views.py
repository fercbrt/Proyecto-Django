from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from debtsApp.forms import DebtForm, DebtorForm

from .models import Debt, Debtor

# Create your views here.
class Index (generic.ListView):
    template_name = "debtsApp/index.html"
    context_object_name = "debtors"
    
    def get_queryset(self):
        """Return the registered debtors."""
        debtors = Debtor.objects.all()
        return sorted(debtors, key=lambda d: d.total_debt(), reverse=True)
    
class DebtorCreateView(generic.CreateView):
    model = Debtor
    template_name="debtsApp/debtor_form.html"
    form_class = DebtorForm
    success_url = reverse_lazy('debtsApp:index')

class DebtorUpdateView(generic.UpdateView):
    model = Debtor
    template_name="debtsApp/debtor_form.html"
    form_class = DebtorForm
    success_url = reverse_lazy('debtsApp:index')

class DebtorDeleteView(generic.DeleteView):
    model = Debtor
    success_url = reverse_lazy('debtsApp:index')

class DebtorDetailView(generic.DetailView):
    model = Debtor
    template_name = "debtsApp/debtor.html"

class DebtCreateView(generic.CreateView):
    model = Debt
    template_name = "debtsApp/debt_form.html"
    form_class = DebtForm
    success_url = reverse_lazy('debtsApp:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['debtor'] = get_object_or_404(Debtor, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.debtor_id = self.kwargs['pk']
        super().form_valid(form)
        return redirect('debtsApp:debtor_detail', pk=self.kwargs['pk'])

class DebtUpdateView(generic.UpdateView):
    model = Debt
    template_name = "debtsApp/debt_form.html"
    form_class = DebtForm
    success_url = reverse_lazy('debtsApp:index')
    pk_url_kwarg = 'debt_pk' # aquí especificas el nombre del parámetro en la URL que contiene la pk de la deuda a actualizar
    
    def form_valid(self, form):
        debtor_pk = self.kwargs['debtor_pk']
        debt_pk = self.kwargs['debt_pk']
        debt = form.save(commit=False)
        debt.debtor_id = debtor_pk
        debt.id = debt_pk
        debt.save()
        return redirect('debtsApp:debtor_detail', pk=debtor_pk)


class DebtDeleteView(generic.DeleteView):
    model = Debt
    template_name = "debtsApp/debt_confirm_delete.html"
    pk_url_kwarg = 'debt_pk'
    success_url = reverse_lazy('debtsApp:index')

    def form_valid(self, form):
        super().form_valid(form)
        return redirect('debtsApp:debtor_detail', pk=self.kwargs['debtor_pk'])