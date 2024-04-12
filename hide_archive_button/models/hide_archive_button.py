import logging
from odoo import http

class MyController(http.Controller):
    _name = 'hide_archive_button.model'
    _description = 'Hide Archive Button Model'

    @http.route('/HideArchiveButton/get_archive_group_id', type='json', auth='user')
    def get_archive_group_id(self):
        # Busca el grupo "Permitir archivar" por nombre
        archive_group = http.request.env['res.groups'].search([('name', '=', 'Permitir archivar')], limit=1)
        if archive_group:
            archive_group_id = next(iter(archive_group.get_external_id().values()))
            #logging.info('Permitir archivar: %s, %s', archive_group, 'TEST')#, archive_group_id)
            #print(archive_group, type(archive_group))
            #print(next(iter(archive_group.get_external_id().values())))
            # for item in dir(archive_group):
            #     print(item)
            return archive_group_id
        else:
            return False
