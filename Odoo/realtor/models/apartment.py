from odoo import models,fields, api
from odoo.exceptions import ValidationError

class Apartment(models.Model):
    _name = 'apartment' 
    _sql_constraints = [('unique_name', 'unique(name)', 'An apartment with the same name exist')]

    name = fields.Char(unique=True, string="Name")
    description = fields.Text(string="Description") 
    image = fields.Image(max_height = 100, max_width = 100, string="Picture") 
    available_date = fields.Date(string="Available date") 
    price = fields.Integer(string="Price")
    surface_apartment = fields.Integer(string="Surface of the apartment")
    surface_terrace = fields.Integer(string="Surface of the terrace")
    total_surface = fields.Integer(compute = '_calculate_total_surface', string="Total surface")
    buyer_id = fields.Many2one('res.partner', string='Buyer')

    def _calculate_total_surface(self):
        for record in self :
            record.total_surface = record.surface_apartment + record.surface_terrace

    @api.constrains('price')
    def _check_price(self) :
        for record in self :
            if record.price <= 0 :
                raise ValidationError('Price must be greater than 0')
    
    @api.constrains('surface_apartment')
    def _check_surface_apartment(self) :
        for record in self :
            if record.surface_apartment <= 0 :
                raise ValidationError('Surface apartment must be greater than 0')
    
    @api.constrains('surface_terrace')
    def _check_surface_terrace(self) :
        for record in self :
            if record.surface_terrace <= 0 :
                raise ValidationError('Surface terrace must be greater than 0')
     


