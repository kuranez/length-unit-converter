# Length Unit Converter

**Version: 3.2 alpha** 

Babby's first GUI project. Unit converter for length measurements in Jupyter Notebook.  

**Supports:**

- SI-Units (Metric)
- Imperial Units (US)
- Nautical Units
- Astronomical Distances
- Atomic and Molecular Distances

**Features:**
- Vaporeave themed GUI using HoloViz Panel (https://panel.holoviz.org/).

**Python Dependencies:**

- `panel`

**Launch App:**
- Use the following command in the terminal to launch a local instance of the app in your browser:

```bash
panel serve 3-2_universal-length-unit-converter.ipynb
```

---
## Changes

**Version: 3.2**

**New:**
- **Reworked scaling:** App now fills out the full screen.
- Reworked button callbacks.
- Resized banner images.
- Gridspec layout.
- **Added Section:** _VII. Serve App_ in the notebook for documentation purposes.
- Options serving panel app.
- Creating a systemd.service.
- Configuration of nginx.


---
## Screenshot

| v. 3.2: Vapowave themed GUI                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Screenshot.png\|429](https://raw.githubusercontent.com/kuranez/Length-Unit-Converter/refs/heads/main/images/screenshots/screenshot_version_3-1.png) |


---

## Version History

| Panel WebApp<br>                                                                                         | **Vaporvawe Notebook**                                                                                                                                    | **Basic GUI (v. 1.0 - v. 1.4)**                                                                       |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| v. 3.0 [↗](https://raw.githubusercontent.com/kuranez/Length-Unit-Converter/refs/heads/main/images/screenshots/screenshot_version_3.png)              | v. 2.0 [↗](https://raw.githubusercontent.com/kuranez/Length-Unit-Converter/refs/heads/Panel-Version-(v.3.0)/images/screenshots/screenshot_version_2.png)) | v. 1.4 [↗](https://github.com/kuranez/Length-Unit-Converter/tree/unit-converter-basic)                |
| - Widgets: `panel`<br>- Language: English<br>- Vaporwave theme<br>- Improved Layout<br>- Working WebApp! | - Widgets: `ipywidgets`<br>- Language: English<br>-  Cleaned up user interface<br>- Vaporwave themed<br>- ! Theme broken !                                | - Widgets: `ipywidgets`<br>- Language: English<br>- Basic GUI / Notebook<br>- Incl. Conversion Tables |


---

## Coding Learn Progress

I started the project in the beginning of last year.

**Total Line of Codes:** 1059 \
**Beginning:** 02/2024 \
**Ending:** 03/2025 

| Learning Curve                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![Screenshot.png\|429](https://raw.githubusercontent.com/kuranez/Length-Unit-Converter/refs/heads/main/learning-progress/learning%20progress.png) |

### First scripts in Jupyter Notebook

| v. 0.a                                                                                                                                   | v. 0.b                                                                                                                       | v. 0.c                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| v-0a_console-version.py [↗](https://github.com/kuranez/Length-Unit-Converter/blob/main/scripts/v-0a_console-version.py) | v-0b_basic-gui.py [↗](https://github.com/kuranez/Length-Unit-Converter/blob/unit-converter-panel-3-0/scripts/v-0b_basic-gui.py) | v-0c_styled-gui.py [↗](https://github.com/kuranez/Length-Unit-Converter/blob/unit-converter-panel-3-0/scripts/v-0c_styled-gui.py) |
| Simple unit converter script, completely text-based.                                                                                     | Adding GUI elements using `ipywidgets`.                                                                                      | Simple Styling & Layout.                                                                                                       |

---
## Sources

- **JupyterLab**:  Interactive Python Notebooks [↗](https://jupyter.org/)
- **Holoviz Panel**: Data Exploration & Web App Framework [↗](https://panel.holoviz.org/)
