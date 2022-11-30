from odoo import models,fields

class Apartment(models.Model):
    #The technical name.
    _name = 'apartment' 
    #Check constraint for the price 
    _sql_constraints = [
        ('price_check','CHECK (price > 0)','The price must be greater than 0 ! '),
        ('surface_apartement_check','CHECK(surface_apartment > 0)' ,'The surface of the apartment must be greater than 0 !'),
        ('surface_terrace_check','CHECK(surface_terrace > 0)','The surface of the terrace must be greater than 0 !')
        ]

    #The name of the apartment (Unique name).
    name = fields.Char(unique=True, string="Nom")
    #The description of the apartment.
    description = fields.Text(string="Description") 
    #The image of the apartment.
    image = fields.Image(max_height = 100, max_width = 100, string="Photo") 
    #The minimum date of availabilty for the apartment !TO-CHANGE!
    available_date = fields.Date(string="Date de disponibilité") 
    #The price of the apartment.
    price = fields.Integer(string="Prix")
    #The surface in m² of the apartment.
    surface_apartment = fields.Integer(string="Surface de l'appartement")
    #The surface in m² of the terrace.
    surface_terrace = fields.Integer(string="Surface de la terrasse")
    #The total surface of the apartment.
    total_surface = fields.Integer(compute = '_calculate_total_surface', string="Surface totale")
    #Buyer of the apartment - An apartment is bought by only one buyer.
    buyer_id = fields.Many2one('res.partner', string='Acheteur')

    #Computes the total surface according the surface apartment and the terrace surface.
    def _calculate_total_surface(self):
        for record in self :
            record.total_surface = record.surface_apartment + record.surface_terrace

     


