# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name="hospital.appointment"
    _description = "hospital appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    gender = fields.Selection(string = 'Gender', related='patient_id.gender')
    appointment_date_time = fields.Datetime("Appointment Date & Time", default=fields.Datetime.now())
    appointment_date= fields.Date("Appointment Date ",default=fields.Date.context_today)
    
    
    
