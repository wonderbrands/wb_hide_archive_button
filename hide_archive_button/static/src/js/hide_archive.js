odoo.define('hide_archive_button.BasicView', function (require) {
"use strict";

var session = require('web.session');
var BasicView = require('web.BasicView');
BasicView.include({
        init: function(viewInfo, params) {
            var self = this;
            this._super.apply(this, arguments);
            var model = self.controllerParams.modelName in ['res.partner','product.template'] ? 'True' : 'False';
            if(model) {
            // Llamada a la función Python para obtener el ID externo del grupo
                session.rpc('/HideArchiveButton/get_archive_group_id', {}).then(function(archive_group_id) {
                    //let archive_group_id = '__export__.res_groups_66_e4e34c00'
                    session.user_has_group(archive_group_id).then(function(has_group) {
                        if (!has_group) {
                            self.controllerParams.archiveEnabled = 'False' in viewInfo.fields;
                        }
                    });
                });
            }
        },
    });
});

//                session.user_has_group('__export__.res_groups_66_e4e34c00').then(function(has_group) {
//                    if(!has_group) {
//                        self.controllerParams.archiveEnabled = 'False' in viewInfo.fields;
//                    }
//                });
//            }
//        },
//    });
//});