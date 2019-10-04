# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, http
from odoo.http import request
import odoo, os, time, socket, logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import UserError

try:
    from xmlrpc import client as xmlrpclib
except ImportError:
    import xmlrpclib

def execute(connector, method, *args):
    res = False
    try:
        res = getattr(connector, method)(*args)
    except socket.error as error:
        _logger.critical('Error while executing the method "execute". Error: ' + str(error))
        raise error
    return res


class DatabaseBackup(models.Model):
    _name = 'database.backup'
    
    @api.model
    def _default_db(self):
        return request.session.db

    name = fields.Char('Refferal Name', index=True, required=True)
    db_name = fields.Char('Database', required=True, default=_default_db, readonly=True)
    user_id = fields.Many2one('res.users', string='Responsible', required=False, default=lambda self: self.env.user, readonly=True)
    remarks = fields.Text('Remarks') 
    
    @api.multi
    def generate_backup(self):
        self.schedule_backup()

    @api.multi
    def get_db_list(self, context={}):
        conn = xmlrpclib.ServerProxy(self.url + '/xmlrpc/db')
        db_list = execute(conn, 'list')
        return db_list

    @api.multi
    def _get_db(self):
        return self._cr.dbname
    
    @api.multi
    def _fetch_url(self):
        return http.request.env['ir.config_parameter'].get_param('web.base.url')

    name = fields.Char('Refferal Name', index=True, required=True)
    url = fields.Char('URL', required=True, default=_fetch_url)
    db_name = fields.Char('Database', required=True, default=_get_db)
    folder = fields.Char('Backup Directory', required='True', default='/odoo/backups',
                         help='Absolute path for storing the backups')
    backup_type = fields.Selection([('zip', 'Zip'), 
                                    ('dump', 'Dump')], 
                                   'Backup Type', required=True, default='zip')

    @api.multi
    def _check_db_exist(self):
        self.ensure_one()

        db_list = self.get_db_list()
        if self.db_name in db_list:
            return True
        return False

    _constraints = [(_check_db_exist, _('Error ! No such database exists!'), [])]

    @api.model
    def schedule_backup(self):
        conf_ids = self.search([])

        for rec in conf_ids:
            db_list = self.get_db_list()

            if rec.db_name in db_list:
                try:
                    if not os.path.isdir(rec.folder):
                        os.makedirs(rec.folder)
                except:
                    raise
                # Create name for dumpfile.
                bkp_file = '%s_%s.%s' %  (rec.db_name, time.strftime('%Y_%m_%d_%H_%M_%S'), rec.backup_type)
                file_path = os.path.join(rec.folder, bkp_file)
#                 conn = xmlrpclib.ServerProxy(self.url + '/xmlrpc/db')
                try:
                    # try to backup database and write it away
                    fp = open(file_path, 'wb')
                    odoo.service.db.dump_db(rec.db_name, fp, rec.backup_type)
                    raise UserError(_('Success in generating backup !'))
                    fp.close()
                except Exception as error:
                    _logger.debug("Can't take backup %s." % (rec.db_name))
                    _logger.debug("Exact error from the exception: " + str(error))
                    continue

            else:
                _logger.debug("database %s doesn't exist" % (rec.db_name))
