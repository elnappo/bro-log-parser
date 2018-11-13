from datetime import datetime
from ipaddress import ip_address
from collections import namedtuple


def _bro_types_mapping(separator_set):
    """Returns a mapping from bro data types to python data types partly based on separator_set char"""

    return {
        "time": lambda ts: datetime.fromtimestamp(float(ts)),
        "string": str,
        "addr": ip_address,
        "port": int,
        "count": int,
        "bool": bool,
        "enum": str,
        "interval": float,
        "vector[string]": str,
        "vector[interval]": float,
        "set[string]": lambda string_set: [str(set_item) for set_item in string_set.split(separator_set)],
        "set[addr]": lambda addr_set: [ip_address(set_item) for set_item in addr_set.split(separator_set)],
        "set[enum]": lambda enum_set: [str(set_item) for set_item in enum_set.split(separator_set)],
    }


def parse_log(file_path):
    """Yields a dynamically build log entry nametuple from a bro formatted log file path"""

    with open(file_path, "r") as f:
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

            entry_fields = list()
            for index, field in enumerate(line.rstrip("\n").split(separator)):
                if field != empty_field and field != unset_field:
                    entry_fields.append(bro_types[types[index]](field))
                else:
                    # Use None if field is empty or unset
                    entry_fields.append(None)

            yield Entry(*entry_fields)
