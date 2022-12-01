from odoo import models,fields, api
from odoo.exceptions import ValidationError

class Apartment(models.Model):
    _name = 'apartment' 
    _description = 'Apartment'
    _sql_constraints = [('unique_name', 'unique(name)', 'An apartment with the same name exist')]

    name = fields.Char(string="Name")
    description = fields.Text(string="Description") 
    image = fields.Image(max_height = 100, max_width = 100, string="Picture") 
    available_date = fields.Datetime(string="Available date") 
    price = fields.Integer(string="Price")
    surface_apartment = fields.Integer(string="Surface of the apartment")
    surface_terrace = fields.Integer(string="Surface of the terrace")
    total_surface = fields.Integer(compute = '_calculate_total_surface', string="Total surface")
    buyer = fields.Char(string="Buyer with the best offer", readonly=True, default=None, compute='_find_buyer')
    offer = fields.Integer(string="Highest offer", readonly=True, default=0)


    def _calculate_total_surface(self):
        for record in self :
            record.total_surface = record.surface_apartment + record.surface_terrace

    def _find_buyer(self) :
        for record in self :
            record.buyer = None
            record.offer = 0
            min_offer = (record.price / 100) * 90
            buyers = self.env['res.partner'].search([("apartment", "in", record.name)])
            best_buyer = None
            offer = 0
            for buyer in buyers :
                if buyer.offered_price > offer and buyer.offered_price >= min_offer :
                    offer = buyer.offered_price
                    best_buyer = buyer.name
            record.buyer = best_buyer
            record.offer = offer
            

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

    @api.constrains('available_date')
    def _check_available_date(self) :
        for record in self :
            if record.create_date.year == record.available_date.year and record.create_date.month + 3 > record.available_date.month :
                raise ValidationError('Available date must be minimum 3 month after the creation of the apartment')
     


