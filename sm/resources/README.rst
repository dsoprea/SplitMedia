A tool that takes a media file and a list file with offsets and processes the list file to split the media file up into pieces using `ffmpeg <https://www.ffmpeg.org>`_.


Usage
=====

Example usage::

    $ splitmedia media.file list.txt output_path


Output
======

Splitting the Quake soundtrack::

    $ splitmedia "Quake Soundtrack.m4a" list_file.quake quake_output
    OFF 000:00:00.000 DUR 000308.000 01_QuakeTheme.m4a
    OFF 000:05:08.000 DUR 000146.000 02_Aftermath.m4a
    OFF 000:07:34.000 DUR 000500.000 03_TheHallofSouls.m4a
    OFF 000:15:54.000 DUR 000366.000 04_ItisRaed.m4a
    OFF 000:22:00.000 DUR 000444.000 05_ParallelDimensions.m4a
    OFF 000:29:24.000 DUR 000519.000 06_Life.m4a
    OFF 000:38:03.000 DUR 000336.000 07_Damation.m4a
    OFF 000:43:39.000 DUR 000388.000 08_Focus.m4a
    OFF 000:50:07.000 DUR 000213.000 09_Falling.m4a
    OFF 000:53:40.000 DUR 000315.000 10_TheReaction.m4a
    ...


Dependencies
============

- Python 2.7
- `ffmpeg <https://www.ffmpeg.org>`_


List File Example
=================

Also provided as *list_file.formats* in the project::

    0:00:00.123 filepart1
    0:03:10     filepart2
    0:09:20     filepart3
    1300        filepart4
    1345.456    filepart5
    1347        filepart6


---------------
List File Notes
---------------

- Offsets can be integers or full time specifications
- Seconds can be decimals
- Can have hash-prefixed comments
- Can have empty lines (for organization)
- The filenames will be sanitized (innappropriate characters removed) automatically


Command Line
============

Command line help::

    usage: splitmedia [-h] media_filepath list_filepath output_path

    Split the media file into multiple parts by times

    positional arguments:
      media_filepath  File-path of the media file
      list_filepath   File-path of the list
      output_path     Output path

    optional arguments:
      -h, --help      show this help message and exit
