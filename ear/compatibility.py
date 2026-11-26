"""Thin wrappers around APIs that changed between library versions.

Keep version-dependent calls here so that the rest of the code base does not
depend on deprecated interfaces (pkg_resources, the old ruamel.yaml functions,
six).
"""
import io
import sys
from importlib import resources


def write_bytes_to_stdout(b):
    """Write bytes to stdout."""
    return sys.stdout.buffer.write(b)


def open_resource(package, fname):
    """Open a data file shipped with a package as a binary stream.

    Parameters:
        package (str): package name, normally ``__name__`` of the caller
        fname (str): path relative to the package, using ``/`` as separator
    """
    ref = resources.files(package)
    for part in fname.split("/"):
        ref = ref.joinpath(part)
    return ref.open("rb")


def _yaml(typ):
    from ruamel.yaml import YAML

    return YAML(typ=typ, pure=True)


def load_yaml(stream):
    """Safely load YAML from a string or a (binary or text) stream."""
    return _yaml("safe").load(stream)


def dump_yaml(data, stream=None, roundtrip=False, indent=None):
    """Dump YAML; return it as a string if no stream is given.

    Parameters:
        data: object to dump
        stream: file-like object to write to, or None to return a string
        roundtrip (bool): keep comments and ordering of ruamel round-trip types
        indent (int): indent size in spaces
    """
    y = _yaml("rt" if roundtrip else "safe")
    if not roundtrip:
        y.default_flow_style = False
    if indent is not None:
        y.indent(mapping=indent, sequence=indent, offset=0)
    if stream is not None:
        y.dump(data, stream)
        return None
    buf = io.StringIO()
    y.dump(data, buf)
    return buf.getvalue()
