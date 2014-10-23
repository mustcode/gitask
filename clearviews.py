import os
import shutil

import settings

if os.path.exists(settings.VIEWS_DIR):
    shutil.rmtree(settings.VIEWS_DIR)