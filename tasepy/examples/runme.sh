#!/usr/bin/bash --norc
script_path=$(realpath $0 | xargs dirname)
/usr/bin/python3.12 $script_path/tasepy_main_indices.py
