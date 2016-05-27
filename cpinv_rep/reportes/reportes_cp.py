# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
#
#   jorgescalona@riseup.net   @jorgemustaine  https://github.com/jorgescalona
#
##############################################################################

from openerp.report import report_sxw
from openerp.osv import osv


class reportes_cp(report_sxw.rml_parse):
    def __init__(self,cr,uid,name,context):
        super(reportes_cp,self).__init__(cr,uid,name,context)

class reportes_cp_inv(osv.AbstractModel):
    _name="report.cpinv_rep.cp_inv"
    _inherit="report.abstract_report"
    _template="cpinv_rep.cp_inv"
    _wrapped_report_class=reportes_cp

