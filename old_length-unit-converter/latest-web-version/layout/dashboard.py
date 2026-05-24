# layout/dashboard.py

import panel as pn
from components.widgets import (
    value_in, value_out, unit_in, unit_out, submit_button,
    SI_button, US_button, Naut_button, Astro_button, Atom_button,
    logo_pane, image_pane,
    in_mask, out_mask, in_select, out_select
)
from config import UNIT_FACTORS, ASSETS

# --- Info and Links Panes ---
info_pane = pn.pane.Markdown(
    """
    <span style="font-size:36px; color:#C71585; font-family: monospace; font-weight:bold;">Length Unit Converter</span><br>
    <span style="font-size:20px; color:#FDB3FD; font-family: monospace;">
    This is a simple unit converter that allows you to convert between different units of measurement.<br>
    It supports SI, Imperial, Nautical, Astronomical, and Atomic scales.<br>
    <br>
    <span style="font-size:24px; color:#0DFFFF; font-family: monospace; font-weight:bold;">How 2 Use</span><br>
    Select a unit system, enter the value, and choose units for conversion.
    </span>
    """,
    css_classes=['custom-pane']
)
links_pane = pn.pane.Markdown(
    """
    <span style="font-size:24px; color:#C71585; font-family: monospace; font-weight:bold;">Visit Project Page on GitHub</span><br>
    <span style="font-size:18px">[🢅 https://github.com/kuranez/length-unit-converter](https://github.com/kuranez/length-unit-converter)</span>
    """
)

# --- Main Panel (input/output widgets) ---
content = pn.Column(
    info_pane,
    pn.Row(in_mask, out_mask, sizing_mode="stretch_width"),
    pn.Row(in_select, out_select, sizing_mode="stretch_width"),
    submit_button,
    css_classes=['custom-pane'],
    sizing_mode="stretch_both",
)

content_panel = pn.Column(
    content,
    sizing_mode="stretch_width",
)

# --- Sidebar ---
sidebar_panel = pn.Column(
    logo_pane,
    SI_button, US_button, Naut_button, Astro_button, Atom_button,
    links_pane,
    sizing_mode="stretch_width"
)

# --- Grid Layout ---
grid = pn.GridSpec(sizing_mode='stretch_both', ncols=4)
grid[0:4, 0] = sidebar_panel      # Sidebar (25%)
grid[0:4, 1:4] = content_panel    # Main content (75%)

# --- Final Layout ---
layout = pn.Column(grid)

def get_dashboard():
    return layout