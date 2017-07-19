# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class iscritti(models.Model):
#     _name = 'iscritti.iscritti'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class activity(models.Model):
	_name = 'partner_activities.activity'
    
	activity_start = fields.Datetime(string='Inizio')
	activity_end = fields.Datetime(string='Fine')
	title = fields.Char(string='Titolo')
	description = fields.Text(string='Descrizione')
	finalopinion = fields.Selection([(u'positive', u'Positive'), (u'negative', u'Negative')],string='Esito')
	ngo_employer=fields.Many2one('res.partner',string='Partner')
	ngo_employed=fields.Many2one('res.partner',string='Socio')	

#codice fiscale
#fonte
class ResPartner(models.Model):
	_inherit = 'res.partner'
	
	ngo_ok_privacy = fields.Boolean(string='E\' un socio',track_visibility='onchange',help="Autorizzazione al trattamento dei dati.")
	ngo_ok_email = fields.Boolean(string='E\' un socio', track_visibility='onchange',help="Autorizzazione alla comunicazione via email.")
	ngo_ok_paper = fields.Boolean(string='E\' un socio', track_visibility='onchange',help="Autorizzazione alla comunicazione cartacea.")
	ngo_ok_thankyou = fields.Boolean(string='E\' un socio', track_visibility='onchange',help="Autorizzazione a ricevere i ringraziamenti.")
	
	ngo_is_associated = fields.Boolean(string='E\' un socio', track_visibility='onchange',help="Specifica se il contatto è un socio.")
	ngo_is_club = fields.Boolean(string='E\' un socio', track_visibility='onchange',help="Specifica se il contatto è un socio del club.")
	ngo_is_volontary = fields.Boolean(string='E\' un volontario', track_visibility='onchange',help="Specifica se il contatto è un volontario.")
	ngo_is_employer = fields.Boolean(string='E\' un employer', track_visibility='onchange',help="Specifica se il contatto offre attività.")
	
	ngo_donor_type = fields.Selection([(u'amico',u'Amico'), (u'sostenitore',u'Sostenitore'), (u'benemerito',u'Benemerito')],string='Tipo donatore')
	ngo_hostperson_id=fields.Many2one('res.partner',string='Ref. Colloquio')
	ngo_interviewdate=fields.Date(string='Data colloquio')
	ngo_activities=fields.One2many('partner_activities.activity','id',string='Attività')
	ngo_activities_for=fields.One2many('partner_activities.activity','id',string='Attività')
	ngo_interviewer=fields.Many2one('res.partner',string='Ref. Colloquio')