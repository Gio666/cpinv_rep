# -*- encoding: utf-8 -*-

from openerp.report import report_sxw
from openerp.osv import osv


class reportes_cp(report_sxw.rml_parse):
    def __init__(self,cr,uid,name,context):
        super(reportes_cp,self).__init__(cr,uid,name,context)

class reportes_cp_inv(osv.AbstractModel):
    _name="report.cpinv_rep.cp_inv"
    _inherit="report.abstract.report"
    _template="cpinv_rep.cp_inv"
    _wrapped_report_class=reportes_cp

