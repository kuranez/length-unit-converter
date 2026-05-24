# components/widgets.py

import panel as pn
from config import UNIT_FACTORS, ASSETS, CUSTOM_CSS_PATH

# --- Load Panel Extensions ---
pn.extension(theme='dark', raw_css=[open(CUSTOM_CSS_PATH).read()])

# Input/Output widgets
value_in = pn.widgets.FloatInput(value=1, sizing_mode='stretch_both', format='0.4f', css_classes=['custom-style'])
value_out = pn.widgets.FloatInput(value=1, sizing_mode='stretch_both', css_classes=['custom-style'], disabled=True)
unit_in = pn.widgets.Select(options=UNIT_FACTORS['SI_Units'], sizing_mode='stretch_both', css_classes=['custom-style'])
unit_out = pn.widgets.Select(options=UNIT_FACTORS['SI_Units'], sizing_mode='stretch_both', css_classes=['custom-style'])

submit_button = pn.widgets.Button(name='Click to convert!', icon='transform', icon_size='4em', css_classes=['custom-button'], sizing_mode='stretch_both')

# Sidebar buttons
SI_button = pn.widgets.Button(name='SI Units', icon='world', icon_size='4em', sizing_mode='stretch_both', css_classes=['custom-button'])
US_button = pn.widgets.Button(name='Imperial Units', icon='star', icon_size='4em', sizing_mode='stretch_both', css_classes=['custom-button'])
Naut_button = pn.widgets.Button(name='Nautical Units', icon='anchor', icon_size='4em', sizing_mode='stretch_both', css_classes=['custom-button'])
Astro_button = pn.widgets.Button(name='Astronomical Scale', icon='sparkles', icon_size='4em', sizing_mode='stretch_both', css_classes=['custom-button'])
Atom_button = pn.widgets.Button(name='Atomic & Particle Scale', icon='atom', icon_size='4em', sizing_mode='stretch_both', css_classes=['custom-button'])

# Logo and images
logo_pane = pn.pane.PNG(ASSETS['logo'], width=300, height=300, align='center', css_classes=['transparent-pane'])

label_from = pn.pane.PNG(ASSETS['labels']['from'], sizing_mode='stretch_width')
label_to = pn.pane.PNG(ASSETS['labels']['to'], sizing_mode='stretch_width')
label_in = pn.pane.PNG(ASSETS['labels']['input'], sizing_mode='stretch_width')
label_out = pn.pane.PNG(ASSETS['labels']['output'], sizing_mode='stretch_width')

# Banner image (start with SI banner)
image_pane = pn.pane.PNG(ASSETS['banners'][0], sizing_mode='stretch_width', css_classes=['transparent-pane'])

# Grouped input/output fields
in_mask = pn.Column(label_in, value_in, sizing_mode='stretch_both')
out_mask = pn.Column(label_out, value_out, sizing_mode='stretch_both')
in_select = pn.Column(label_from, unit_in, sizing_mode='stretch_both')
out_select = pn.Column(label_to, unit_out, sizing_mode='stretch_both')