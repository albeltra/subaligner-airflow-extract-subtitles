import ast
import os
from pathlib import Path

from subaligner.utils import Utils

mediaFile = ast.literal_eval(os.environ.get('mediaFile'))
mediaInfo = ast.literal_eval(os.environ.get('mediaInfo'))
stream_index = os.environ.get('stream_index', '0')

print(mediaFile) 

extract_subtitle = Utils().extract_matroska_subtitle

kwargs = {'mkv_file_path': mediaFile['path'],
          'stream_index': stream_index,
          'output_file_path': "/TEMP-SUBS/" + Path(mediaFile['path']).name + '.srt',
          'timeout_secs': 10000
          }

extract_subtitle(**kwargs)