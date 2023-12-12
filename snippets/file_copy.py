import shutil
from pathlib import Path

p = Path.home()
shutil.copy(p / 'spam.txt', p / 'some_folder')
