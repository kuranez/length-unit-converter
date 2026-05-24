# Length Unit Converter

# Version: 0.3
# Author: github.com/kuranez


import ipywidgets as widgets
from IPython.display import display

# --- I. Variablen: GUI-Elemente -----------------------------------------------

# ------ Header: Titel & Beschreibung ------------------------------------------

title_text = "Einheitenumrechner für Längenmaße"
title = widgets.HTML(value = f"<b><font size = '+2'>{title_text}</font></b>")
# -- old -- title = widgets.Label(value = "Einheitenumrechner für Längenmaße")

description_text = "Tool zum Umrechnen von Längenmaßen in SI-Einheiten."
description = widgets.HTML(value = f"<font size ='+1'>{description_text}</font>")
# -- old -- description = widgets.Label(value = "Tool zum Umrechnen von Längenmaßen in SI-Einheiten.")

# ------ Content: Eingabe, Ausgabe, Buttons, etc. ------------------------------

# Felder für Werte
value_in = widgets.FloatText(value=10**0, description='Eingabe:', layout={'width': '26%'})
value_out = widgets.FloatText(value=10**0, description='Ausgabe:', layout={'width': '26%'}, disabled = True)

# Menüs für Einheiten
unit_in = widgets.Dropdown(
    options=[('km', 10**3), ('hm', 10**2), ('dam', 10**1), ('m', 10**0), ('dm', 10**-1), ('cm', 10**-2), ('mm', 10**-3), ('μm', 10**-6), ('nm', 10**-9), ('fm', 10**-15)],
    value=10**0,
    description='von Einheit:',
    layout={'width': '26%'})

unit_out = widgets.Dropdown(
    options=[('km', 10**3), ('hm', 10**2), ('dam', 10**1), ('m', 10**0), ('dm', 10**-1), ('cm', 10**-2), ('mm', 10**-3), ('μm', 10**-6), ('nm', 10**-9), ('fm', 10**-15)],
    value=10**0,
    description='von Einheit:',
    layout={'width': '26%'})
# -- old -- unit_in = widgets.Dropdown(options=[('m', 10**0), ('km', 10**3), ('mm', 10**-3)], value=10**0, description='von Einheit:', layout={'width': '26%'})
# -- old -- unit_out = widgets.Dropdown(options=[('m', 10**0), ('km', 10**3), ('mm', 10**-3)], value=10**0, description='in Einheit:', layout={'width': '26%'})

# Output
out = widgets.Output()

# Button
submit_button = widgets.Button(description='Konvertieren', layout={'width':'54%'})

# ------ Layout ----------------------------------------------------------------

# Header
header = widgets.VBox([title, description])

# Content
hbox1 = widgets.HBox([value_in, value_out])
hbox2 = widgets.HBox([unit_in, unit_out])
grid = widgets.VBox([hbox1, hbox2])

# All
ui = widgets.VBox([header, grid, submit_button])

# --- II. Funktionen -----------------------------------------------------------

# Berechnung
def calculate(value_in, unit_in, unit_out):
  return value_in.value * unit_in.value / unit_out.value

# Ausführung
def submit(button):
    value_out.value = calculate(value_in, unit_in, unit_out)
    out.clear_output()
    with out:
        display(value_out.value)

# --- Ausführung ---------------------------------------------------------------

# Trigger
submit_button.on_click(submit)

# --- Anzeige ------------------------------------------------------------------
display(ui)