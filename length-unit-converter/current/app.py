# app.py

import panel as pn
from config import CUSTOM_CSS_PATH, UNIT_FACTORS, ASSETS
from components.widgets import (
    value_in, value_out, unit_in, unit_out, submit_button, image_pane,
    SI_button, US_button, Naut_button, Astro_button, Atom_button
)
from layout.dashboard import get_dashboard

# --- Load Panel Extensions ---
pn.extension(theme='dark', raw_css=[open(CUSTOM_CSS_PATH).read()])

# --- Conversion Logic ---
def load_units(category):
    unit_in.options = UNIT_FACTORS[category]
    unit_out.options = UNIT_FACTORS[category]

def calculate(value, factor_in, factor_out):
    return value * factor_in / factor_out

def submit(event=None):
    result = calculate(value_in.value, unit_in.value, unit_out.value)
    value_out.value = round(result, 4)

def update_banner(category):
    banners = ASSETS['banners']
    idx = {
        'SI_Units': 0, 'US_Units': 1, 'Naut_Units': 2,
        'Astro_Units': 3, 'Atom_Units': 4
    }[category]
    image_pane.object = banners[idx]

# --- Button Callbacks ---
def on_SI_click(event=None):
    load_units('SI_Units')
    update_banner('SI_Units')

def on_US_click(event=None):
    load_units('US_Units')
    update_banner('US_Units')

def on_Naut_click(event=None):
    load_units('Naut_Units')
    update_banner('Naut_Units')

def on_Astro_click(event=None):
    load_units('Astro_Units')
    update_banner('Astro_Units')

def on_Atom_click(event=None):
    load_units('Atom_Units')
    update_banner('Atom_Units')

SI_button.on_click(on_SI_click)
US_button.on_click(on_US_click)
Naut_button.on_click(on_Naut_click)
Astro_button.on_click(on_Astro_click)
Atom_button.on_click(on_Atom_click)
submit_button.on_click(submit)

# --- Serve Layout ---
dashboard = get_dashboard()
dashboard.servable()