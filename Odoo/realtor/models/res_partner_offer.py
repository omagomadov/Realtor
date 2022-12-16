from odoo import models, fields


class Offer(models.Model):
    _inherit = 'res.partner'

    apartment = fields.Many2one('apartment', string='Apartment', ondelete='cascade')
    offered_price = fields.Integer(string="Offered price", default=0)
