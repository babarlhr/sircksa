{
    'name' : 'Recruitment Custom',
    'description' : 'Adding fields to recruitment module',
    'version': '1.1',
    'author' : 'Odoo Advantage Ireland',
    'website' : 'www.erp.odoo.ie',
    'depends' : [
        'hr', 'hr_recruitment',
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/job_position.xml',
        'reports/job_position_reports.xml',
        'reports/job_position_template.xml',
        'views/applications.xml',
    ],
    'installable' : True,
}