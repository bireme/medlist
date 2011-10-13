
from json import dumps

medicines = [
    {   'TYPE':'medicine',
        'section': '1.1.1',
        'generic_name': 'halothane',
        'forms' : [
            {   'dosage_form' : 'inhalation',
            },
        ]
    },
    {   'TYPE':'medicine',
        'section': '1.1.1',
        'generic_name': 'oxygen',
        'forms' : [
            {   'dosage_form' : 'inhalation',
                'dosage_note' : 'medicinal gas',
            },
        ]
    },
    {   'TYPE':'medicine',
        'section': '1.1.2',
        'generic_name': 'ketamine',
        'forms' : [
            {
                'dosage_form' : 'injection',
                'strength' : '50 mg (as hydrochloride)/ml in 10-ml vial'
            },
        ],
    },
    {   'TYPE':'medicine',
        'section': '1.1.2',
        'generic_name': 'propofol',
        'medicine_note' : 'Thiopental may be used as an alternative depending on local availability and cost.', 
        'forms' : [
            {
                'dosage_form' : 'injection',
                'strength' : '10 mg/ml; 20 mg/ml'
            },
        ],
    },
    {   'TYPE':'medicine',
        'section': '1.2',
        'generic_name': 'bupivacaine',
        'reference_medicine':True,
        'forms' : [
            {
                'dosage_form' : 'injection',
                'strength' : '0.25%; 0.5% (hydrochloride) in vial'
            },
            {
                'dosage_form' : 'injection for spinal anaesthesia',
                'strength' : '0.5% (hydrochloride) in 4-ml ampoule to be mixed with 7.5% glucose solution'
            },
        ],
    },
    {   'TYPE':'medicine',
        'section': '2.1',
        'generic_name': 'ibuprofen',
        'age_weight_restriction': '>3 months',
        'forms' : [
            {
                'dosage_form' : 'oral liquid',
                'strength' : '40 mg/ml (200 mg/5 ml)'
            },
            {
                'dosage_form' : 'tablet',
                'strength' : '200 mg; 400 mg'
            },
        ],
    },

]


print dumps(medicines, indent=2)