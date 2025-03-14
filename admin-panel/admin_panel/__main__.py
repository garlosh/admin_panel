
# Make sure the project is in the Python path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).absolute().parent.parent))


# Import the main module
import admin_panel

# Run the app
admin_panel.app.run_in_window()
