# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import ugettext as _
from django.views.decorators.http import require_POST

from . import models
from . import forms

def cart(request, typ, form_class=forms.EditCartItemForm):
    cart = models.Cart.objects.get_or_create_from_request(request, typ)

    cart_item_forms = []
    for item in cart.items.all():
        form = form_class(data=request.POST or None, instance=item,
                          prefix='%s-%i'%(typ, item.id))
        if request.method == 'POST' and form.is_valid():
            messages.success(request,
                             _("Cart contents were updated successfully."))
            form.save()
            return redirect(request.get_full_path())
        cart_item_forms.append(form)
    templates = [
        'satchless/cart/%s/view.html' % typ,
        'satchless/cart/view.html'
    ]
    return TemplateResponse(request, templates, {
        'cart': cart,
        'cart_item_forms': cart_item_forms,
    })

@require_POST
def remove_item(request, typ, item_pk):
    cart = models.Cart.objects.get_or_create_from_request(request, typ)
    item = get_object_or_404(cart.items, pk=item_pk)
    cart.set_quantity(item.variant, 0)
    return redirect('satchless-cart-view', typ=typ)
