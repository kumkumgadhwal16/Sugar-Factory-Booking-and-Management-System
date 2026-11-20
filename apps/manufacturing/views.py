"""
manufacturing/views.py
Views for each manufacturing process page.
"""

from django.shortcuts import render, get_object_or_404
from .models import ManufacturingStage

# Static content dict (fallback if DB not yet seeded)
STAGE_CONTENT = {
    'cane_yard': {
        'title': 'Cane Yard',
        'subtitle': 'Sugar Mill — Cane Reception',
        'description': (
            'The Cane Yard operator is responsible for offloading canes from cane transports '
            'and organised feeding of canes into the cane conveyors for efficient cane preparation. '
            'The yard ensures a steady supply of sugarcane to the mill, maintaining quality control '
            'at the entry point of the production process.'
        ),
        'image': 'caneyard.png',
    },
    'mill': {
        'title': 'Milling House',
        'subtitle': 'Sugar Mill — Cane Crushing Unit',
        'description': (
            'The Mill House is the cane crushing unit which consists of cane carrier, cane cutter '
            'having cutting knives, milling tandem, bagasse carrier and conveyor. It extracts juice '
            'from the sugarcane through a series of heavy rollers, producing raw juice and bagasse.'
        ),
        'image': 'millhouse.png',
    },
    'boiler': {
        'title': 'Boiler House',
        'subtitle': 'Sugar Mill — Steam Generation',
        'description': (
            'The function of the boiler is to generate steam at desired pressure and temperature '
            'by transferring heat produced by burning of fuel from water to change it into steam. '
            'Bagasse — the fibrous residue from milling — is used as the primary fuel source, '
            'making the process largely self-sufficient in energy.'
        ),
        'image': 'boilerhouse.png',
    },
    'clarification': {
        'title': 'Clarification Section',
        'subtitle': 'Sugar Mill — Juice Purification',
        'description': (
            'The clarification section is designed to remove as many non-sugar components as possible, '
            'improve the purity of the juice, and reduce its viscosity and colour values. '
            'Lime and heat are applied to the raw juice before it is settled and filtered.'
        ),
        'image': 'clarification.jpg',
    },
    'curing': { 
        'title': 'Curing House',
        'subtitle': 'Sugar Mill — Crystal Separation',
        'description': (
            'Curing is the process of separating sugar crystals from the mother liquor (molasses) '
            'using centrifugal machines. The sugar is spun at high speed to remove the syrup, '
            'resulting in clean, dry sugar crystals ready for drying and packing.'
        ),
        'image': 'curinghouse.jpg',
    },
    'crystalization': {
        'title': 'Crystallization',
        'subtitle': 'Sugar Mill — Crystal Formation',
        'description': (
            'In crystallization, a vacuum boiling pan is used. Thick juice or syrup is fed to the '
            'vacuum pans and evaporated until saturated. Seed crystals are added during a strike '
            'to grow sugar crystals to the desired size. Controlled temperature and concentration '
            'are critical to producing uniform, high-quality crystals.'
        ),

        'image': 'crystalization.jpeg'
    },
}


def manufacturing_overview_view(request):
    """Manufacturing overview page listing all stages ."""
    stages = list(STAGE_CONTENT.items())
    return render(request, 'manufacturing/overview.html', {'stages': stages})


def manufacturing_stage_view(request, slug):
    """Detail page for a single manufacturing stage."""
    content = STAGE_CONTENT.get(slug)
    if not content:
        from django.http import Http404
        raise Http404(f"Stage '{slug}' not found.")
    return render(request, 'manufacturing/stage_detail.html', {
        'slug': slug,
        'content': content,
    })
