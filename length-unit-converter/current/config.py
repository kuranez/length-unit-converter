# config.py

import panel as pn

# Conversion factors for different unit types
UNIT_FACTORS = {
    'SI_Units': {
        'km': 10**3, 'hm': 10**2, 'dam': 10**1, 'm': 10**0,
        'dm': 10**-1, 'cm': 10**-2, 'mm': 10**-3, 'μm': 10**-6,
        'nm': 10**-9, 'pm': 10**-12, 'fm': 10**-15
    },
    'US_Units': {
        'm': 1, 'km': 1000, 'cm': 10**-2, 'mile': 1609.44, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254
    },
    'Naut_Units': {
        'm': 1, 'km': 1000, 'mile': 1609.44, 'nautical mile': 1852
    },
    'Astro_Units': {
        'AU': 1.49*10**11, 'light year': 9.461*10**15, 'light hour': 1.079*10**12,
        'light minute': 1.799*10**9, 'light second': 2.998*10**6, 'parsec': 3.086*10**16,
        'kiloparsec': 3.086*10**19, 'megaparsec': 3.086*10**22, 'meter': 1, 'kilometer': 10**3,
        'gigameter': 10**9, 'megameter': 10**10, 'terameter': 10**12, 'petameter': 10**15,
        'exameter': 10**18, 'zettameter': 10**21, 'yottameter': 10**24, 'ronnameter': 10**27    
    },
    'Atom_Units': {
        'femtometer': 10**-15, 'picometer': 10**-12, 'angstrom': 10**-10,
        'nanometer': 10**-9, 'micrometer': 10**-6
    }
}

# Styling: Path to custom CSS
CUSTOM_CSS_PATH = "assets/custom.css"

# Assets paths (relative to project root)
ASSETS = {
    "logo": "assets/images/logo/logo.png",
    "labels": {
        "from": "assets/images/labels/FROM_UNIT-50px.png",
        "to": "assets/images/labels/TO_UNIT-50px.png",
        "input": "assets/images/labels/INPUT-50px.png",
        "output": "assets/images/labels/OUTPUT-50px.png",
    },
    "banners": [
        "assets/images/banners/1-BANNER-SI.png",
        "assets/images/banners/2-BANNER-IMPERIAL-METRIC.png",
        "assets/images/banners/3-BANNER-NAUT.png",
        "assets/images/banners/4-BANNER-ASTRO.png",
        "assets/images/banners/5-BANNER-ATOM-MOL.png",
    ]
}