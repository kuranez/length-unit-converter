import panel as pn
from pathlib import Path

# Input widget
text_input = pn.widgets.TextInput(
    placeholder='Enter your conversion query, try: 1500 kcal in joules', 
    width=720,
    height=42,
    sizing_mode='fixed')

# Output widget
output_area = pn.pane.Markdown(
    'Your conversion result will appear here.',
    sizing_mode='stretch_width',
    align='center',
    styles={
        'font-size': '19px',
        'color': '#f2f2f2',
        'text-align': 'center',
    },
)

# Submit button
submit_button = pn.widgets.Button(
    name='',
    icon='send-2', icon_size='1.8em',
    width=42,
    height=42,
    sizing_mode='fixed')

# Logo and images
ASSETS_DIR = Path(__file__).resolve().parent.parent.joinpath('assets')
LOGO_PATH = ASSETS_DIR.joinpath('logo', 'logo.png')
GITHUB_LOGO_PATH = ASSETS_DIR.joinpath('github', 'github_logo.png')

logo_pane = pn.pane.PNG(
    str(LOGO_PATH),
    width=265,
    height=265,
    margin=(0, 20, 10, 0),
    align='center',
)

github_logo_pane = pn.pane.PNG(
    str(GITHUB_LOGO_PATH),
    width=50,
    height=50,
    align='center',
)
