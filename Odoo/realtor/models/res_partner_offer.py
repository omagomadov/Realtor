from odoo import models, fields

class Offer(models.Model) :
    _inherit = 'res.partner'

    apartment = fields.Many2one('apartment', string='Apartment', on_delete='cascade')
    offered_price = fields.Integer(string="Offered price", default=0)