from django.views import generic# Generic provides views for generic purposes, customizable by overriding attributes and methods methods.

from django.contrib.auth.mixins import LoginRequiredMixin
from auctions.models import Auction

class AuctionListView(LoginRequiredMixin, generic.ListView):
    model = Auction
    context_object_name = 'auction_list'
    template_name = 'auction_list.html'

    def get_queryset(self):
        filter = self.kwargs.get("name")
        if filter:
            return Auction.objects.filter(name__contains=filter)
        return Auction.objects.all().order_by("-id")

class AuctionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Auction
    context_object_name = 'auction_object'
    template_name = 'auction_detail.html'

class AuctionCreate(LoginRequiredMixin, generic.edit.CreateView):
    model = Auction
    fields = ["name", "description", "image",
                "starting_price", "expiration_date"]
    template_name = 'auction_form.html'

    def form_valid(self, form):
        form.instance.vendor = self.request.user
        form.instance.current_price = form.instance.starting_price
        form.instance.winner = self.request.user
        form.instance.image = self.request.FILES['image']
        return super().form_valid(form)
