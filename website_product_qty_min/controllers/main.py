# -*- coding: utf-8 -*-

from odoo import fields, http, tools, _
from odoo.http import request

from odoo.addons.sale.controllers.product_configurator import ProductConfiguratorController

# from odoo.addons.website_sale.main.WebsiteSale import ProductConfiguratorController


class WebsiteSale(ProductConfiguratorController):
    @http.route(['/shop/checkout'], type='http', auth="public", website=True)
    def checkout(self, **post):
        order = request.website.sale_get_order()
        order_status_fail = True
        for row in order.order_line:
            min_qty = int(row.product_id.min_qty)
            uom_qty = int(row.product_uom_qty)
            print(order_status_fail, "*****order*****************QTY*",min_qty," < ", uom_qty)
            if (min_qty < uom_qty) and (min_qty!=0):
                order_status_fail = True
                continue
            else:
                order_status_fail = False
                continue

        print(order_status_fail)    
        if order_status_fail==False:
            redirection = self.checkout_redirection(order)
            if redirection:
                return redirection
    
            if order.partner_id.id == request.website.user_id.sudo().partner_id.id:
                return request.redirect('/shop/address')
    
            for f in self._get_mandatory_billing_fields():
                if not order.partner_id[f]:
                    return request.redirect('/shop/address?partner_id=%d' % order.partner_id.id)
    
            values = self.checkout_values(**post)
    
            if post.get('express'):
                return request.redirect('/shop/confirm_order')
    
            values.update({'website_sale_order': order})
    
            # Avoid useless rendering if called in ajax
            if post.get('xhr'):
                return 'ok'
            return request.render("website_sale.checkout", values)
        else:
            print("minimal qty")
            
            values = {
                'valid':True,
            }
            return request.render("website_sale.cart", values)
        