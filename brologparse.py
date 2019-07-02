from collections import namedtuple
from datetime import datetime
from ipaddress import ip_address
from typing import Dict, TextIO, Iterator, NamedTuple


def _bro_types_mapping(separator_set: str) -> Dict:
    """Returns a mapping from bro data types to python data types partly based on separator_set char"""

    return {
        "time": lambda ts: datetime.fromtimestamp(float(ts)),
        "string": str,
        "addr": ip_address,
        "port": int,
        "count": int,
        "bool": lambda value: True if value == "T" else False if value == "F" else None,
        "enum": str,
        "interval": float,
        "vector[string]": lambda string_vector: [str(set_item) for set_item in string_vector.split(separator_set)],
        "vector[interval]": lambda interval_vector: [float(set_item) for set_item in interval_vector.split(separator_set)],
        "set[string]": lambda string_set: [str(set_item) for set_item in string_set.split(separator_set)],
        "set[addr]": lambda addr_set: [ip_address(set_item) for set_item in addr_set.split(separator_set)],
        "set[enum]": lambda enum_set: [str(set_item) for set_item in enum_set.split(separator_set)],
    }


def parse_log(f: TextIO) -> Iterator[NamedTuple]:
    """Yields a dynamically build log entry namedtuple from a bro formatted log file"""

    # Read log file head
    separator = f.readline().rstrip("\n").split(" ")[1].encode('raw_unicode_escape').decode('unicode_escape')
    separator_set = f.readline().rstrip("\n").split(separator)[1]
    empty_field = f.readline().rstrip("\n").split(separator)[1]
    unset_field = f.readline().rstrip("\n").split(separator)[1]
    path = f.readline().rstrip("\n").split(separator)[1]
    open_time = f.readline().rstrip("\n").split(separator)[1]
    # replace dots in field names with underscores
    fields = [field.replace(".", "_") for field in f.readline().rstrip("\n").lstrip("#").split(separator)[1:]]
    types = f.readline().rstrip("\n").lstrip("#").split(separator)[1:]

    # Mapping from bro data types to python data types
    bro_types = _bro_types_mapping(separator_set)

    Entry = namedtuple("%sEntry" % path.title(), fields)

    for line in f:
        if line.startswith("#"):
            continue

        entry_fields = []
        for index, field in enumerate(line.rstrip("\n").split(separator)):
            if field != empty_field and field != unset_field:
                entry_fields.append(bro_types[types[index]](field))
            else:
                # Use None if field is empty or unset
                entry_fields.append(None)

        yield Entry(*entry_fields)


def parse_log_file(file_path: str) -> Iterator[NamedTuple]:
    with open(file_path, "r") as f:
        yield from parse_log(f)
