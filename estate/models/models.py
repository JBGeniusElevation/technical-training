from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property"

    name = fields.Char(required=True)
    description = fields.Text()
    date_avaliability = fields.Date(copy=False, default=fields.Date.add(fields.date.today(), months=3))
    postcode = fields.Char()
    expected_price= fields.Float()
    selling_price= fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation= fields.Selection([("north","North"),("south","South"),("east","East"),("west","West")])
    active = fields.Boolean(default=False)
    state = fields.Selection([("new","New"),("offer_received","Offer Received"),("offer_accepted","Offer Accepted"),("sold","Sold "),("cancelled","Cancelled ")],default="new",required=True, copy=False)