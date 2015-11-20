{
    'name': 'Global Supplier System',
    'version': '1.0',
    'summary': 'Gestiona procesos de auditoría para segundas partes',
    'description': 'Gestiona procesos de auditoría para segundas partes',
    'application': True,
    'depends': ['mail'],
    'data': [
        'views/gsos_menu.xml',
        'views/audit_view_form.xml',
        'views/audit_view_tree.xml',
        'views/audit_view_calendar.xml',
        'views/audit_view_graph.xml',
        'views/checklist_view_form.xml',
        'views/checklist_view_tree.xml',
        'views/complaint_view_form.xml',
        'views/complaint_view_tree.xml',
        'views/complaint_view_graph.xml',
        'views/severity_view_form.xml',
        'views/supplier_view_form.xml',
        'views/supplier_view_tree.xml',
        'views/report_template_view_form.xml',
        'views/report_template_view_tree.xml',
        'security/gsos_security.xml'
    ]
}
