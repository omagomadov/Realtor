from odoo import models, fields, api
import logging


class ProductApartment(models.Model):
    _inherit = 'product.template'

    apartment_product = fields.Many2one('apartment', string="Apartment", ondelete="cascade", required=True)
    list_price = fields.Float(compute='_product_price')
    

    def _product_price(self):
        for record in self:
            record.list_price = record.apartment_product.price
