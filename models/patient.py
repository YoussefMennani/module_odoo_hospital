# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from duplicity.tempdir import default
from datetime import date


class HospitalPatient(models.Model):
    _name="hospital.patient"
    _description = "hospital patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string = 'Name')
    ref = fields.Char(string = 'reference')
    # default=fields.Date.context_today
    date_birth= fields.Date("Date Of Birth ")
    age = fields.Integer(string = 'Age', compute='_compute_age',tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string = 'Gender')
    active = fields.Boolean(string = 'active',default=1)
    
    @api.depends('date_birth')
    def _compute_age(self):
        
        for rec in self:
            today = date.today()
            
            if rec.date_birth:
                rec.age = today.year - rec.date_birth.year
            else:
                rec.age = 1
        