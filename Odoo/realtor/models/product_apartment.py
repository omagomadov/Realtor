from odoo import models, fields


class ProductApartment(models.Model):
    _inherit = 'product.template'

    apartment_product = fields.Many2one('apartment', string="Apartment", ondelete="cascade")
