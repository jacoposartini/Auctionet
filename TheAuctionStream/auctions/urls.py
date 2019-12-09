from django.urls import path
from auctions.views import AuctionListView, AuctionDetailView, AuctionCreate
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('', AuctionListView.as_view(), name='auction-list'),
    path('filter/<name>/', AuctionListView.as_view(), name='filtered-auction-list'),
    path('new/', AuctionCreate.as_view(), name='auction-create'),
    path('<int:pk>/', AuctionDetailView.as_view(), name='auction-detail'),

]
