from pathlib import Path
from contextlib import contextmanager


@contextmanager
def custom_open(caller_path_string: str, json_name: str):
    with open(Path(caller_path_string).parent / 'samples' / f"{json_name}.json", 'r', encoding='utf-8') as f:
        yield f
