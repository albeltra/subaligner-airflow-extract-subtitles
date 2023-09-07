import ast
import os
from pathlib import Path

from subaligner.utils import Utils

mediaFile = ast.literal_eval(os.environ.get('mediaFile'))
mediaInfo = ast.literal_eval(os.environ.get('mediaInfo'))
stream_index = os.environ.get('stream_index', '0')

extract_subtitle = Utils().extract_matroska_subtitle

output_file_path = "/audio-subs/" + Path(mediaFile['path']).name

kwargs = {'mkv_file_path': mediaFile['path'], 
          'stream_index': stream_index,
          'output_file_path': output_file_path + '.srt.srt',
          'timeout_secs': 10000
          }

if not os.path.exists(output_file_path + '.en.srt') and not os.path.exists(output_file_path + '.srt.srt') and not os.path.exists(output_file_path + '.pgs.srt') and not os.path.exists(output_file_path + '.vob.srt'):
    extract_subtitle(**kwargs)
