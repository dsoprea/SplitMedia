import os
import subprocess
import re

_RE_LIST_LINE = \
    re.compile(r'^((([0-9]+):([0-9]{2}):([0-9]{2}(\.[0-9]+)?))|([0-9]+(\.[0-9]+)?)) +([^#]+)')

_RE_BAD_FILENAME_CHARS = \
    re.compile(r'[^a-zA-Z0-9\-_]')

def process_list(list_filepath):
    offsets = []
    with open(list_filepath) as f:
        i = 0
        for row in f:
            row = row.rstrip()
            if not row:
                continue

            m = _RE_LIST_LINE.match(row)
            if m is None:
                raise ValueError("Could not parse line ({0}): {1}".format(i, row))

            seconds_only = m.group(7)
            if seconds_only:
                offset = float(seconds_only)
            else:
                hours = float(m.group(3))
                minutes = float(m.group(4))
                seconds = float(m.group(5))
    
                offset = hours * 3600.0 + minutes * 60.0 + seconds

            filename = m.group(9).rstrip()

            if offsets:
                last_offset = offsets[-1][0]
                duration = offset - last_offset
                offsets[-1][1] = duration

            # Remove bad characters.
            filename = _RE_BAD_FILENAME_CHARS.sub('', filename)
            offsets.append([offset, None, filename])

            i += 1

    return offsets

def _run(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if p.wait() != 0:
        print(cmd)

        output = p.stdout.read()
        print(output)

        raise ValueError("Command failed ({0}).".format(p.returncode))

def split_media(offsets, media_filepath, ext, output_path):
    digits = len(str(len(offsets)))
    filename_template = '{0:0' + str(digits) + '}_{1}{2}'
    for (i, (offset, duration, filename)) in enumerate(offsets):
        cmd = ['ffmpeg', '-y', '-i', media_filepath, '-ss', str(offset)]
        if duration is not None:
            cmd += ['-t', str(duration)]

        output_filename = filename_template.format(i + 1, filename, ext)
        output_filepath = os.path.join(output_path, output_filename)
        cmd += [output_filepath]

        hours = int(offset // 3600.0)
        minutes = int((offset % 3600.0) // 60.0)
        seconds = float(offset % 60.0)

        if duration is None:
            duration = 0

        print(
            'OFF {0:03}:{1:02}:{2:06.3f} DUR {3:010.3f} {4}'.format(
            hours, minutes, seconds, duration, output_filename))

        _run(cmd)
