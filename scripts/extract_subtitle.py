from subaligner.utils import Utils

import os
from pathlib import Path

mediaFile = os.environ.get('mediaFile')
mediaInfo = os.environ.get('mediaInfo')
stream_index = os.environ.get('stream_index')

extract_subtitle = Utils().extract_matroska_subtitle

kwargs = {'mkv_file_path': mediaFile['path'],
          'stream_index': stream_index,
          'output_file_path': "/TEMP-SUBS/" + Path(mediaFile['path']).name + '.srt',
          'timeout_secs': 10000
          }

extract_subtitle(**kwargs)