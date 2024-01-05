from django.urls import path

from . import views

app_name = "debtsApp"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path('debtor/new/', views.DebtorCreateView.as_view(), name='debtor_create'),
    path('debtor/edit/<int:pk>', views.DebtorUpdateView.as_view(), name='debtor_edit'),
    path('debtor/delete/<int:pk>', views.DebtorDeleteView.as_view(), name='debtor_delete'),
    path('debtor/<int:pk>', views.DebtorDetailView.as_view(), name='debtor_detail'),
    path('debtor/<int:pk>/debt/create/', views.DebtCreateView.as_view(), name='debt_create'),
    path('debtor/<int:debtor_pk>/debt/<int:debt_pk>/update/', views.DebtUpdateView.as_view(), name='debt_edit'),
    path('debtor/<int:debtor_pk>/debt/<int:debt_pk>/delete/', views.DebtDeleteView.as_view(), name='debt_delete'),
]