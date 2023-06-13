import json
import os
from pathlib import Path

from subaligner.utils import Utils

mediaFile = json.loads(os.environ.get('mediaFile'))
mediaInfo = json.loads(os.environ.get('mediaInfo'))
stream_index = os.environ.get('stream_index', '0')

print(mediaFile)

extract_subtitle = Utils().extract_matroska_subtitle

kwargs = {'mkv_file_path': mediaFile['path'],
          'stream_index': stream_index,
          'output_file_path': "/TEMP-SUBS/" + Path(mediaFile['path']).name + '.srt',
          'timeout_secs': 10000
          }

extract_subtitle(**kwargs)