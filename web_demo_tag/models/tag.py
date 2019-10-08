# -*- coding: utf-8 -*-

from odoo import models, api

class WebDemoTag(models.AbstractModel):

    _name = 'web.demo.tag'
    _description = 'Web Demo Tag'

    @api.model
    def _prepare_demo_tag_format_vals(self):
        return {
            'db_name': self.env.cr.dbname,
        }

    @api.model
    def _prepare_demo_tag_name(self):
        name_tmpl = self.env['ir.config_parameter'].sudo().get_param('demo_tag.name')
        vals = self._prepare_demo_tag_format_vals()
        return name_tmpl.format(**vals)

    @api.model
    def set_tag(self):
        """
        This method returns the demo_tag data from ir config parameters
        :return: dictionary
        """
        ir_config_model = self.env['ir.config_parameter']
        name = self._prepare_demo_tag_name()
        return {
            'name': name,
            'color': ir_config_model.sudo().get_param('demo_tag.color'),
            'background_color': ir_config_model.sudo().get_param('demo_tag.background.color'),
        }