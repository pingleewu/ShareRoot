"""sstruct.py -- SuperStruct

Higher level layer on top of the struct module, enabling to
bind names to struct elements. The interface is similar to
struct, except the objects passed and returned are not tuples
(or argument lists), but dictionaries or instances.

Just like struct, we use format strings to describe a data
structure, except we use one line per element. Lines are
separated by newlines or semi-colons. Each line contains
either one of the special struct characters ('@', '=', '<',
'>' or '!') or a 'name:formatchar' combo (eg. 'myFloat:f').
Repetitions, like the struct module offers them are not useful
in this context, except for fixed length strings  (eg. 'myInt:5h'
is not allowed but 'myString:5s' is). The 'x' format character
(pad byte) is treated as 'special', since it is by definition
anonymous. Extra whitespace is allowed everywhere.

The sstruct module offers one feature that the "normal" struct
module doesn't: support for fixed point numbers. These are spelled
as "n.mF", where n is the number of bits before the point, and m
the number of bits after the point. Fixed point numbers get
converted to floats.

pack(format, object):
    'object' is either a dictionary or an instance (or actually
    anything that has a __dict__ attribute). If it is a dictionary,
    its keys are used for names. If it is an instance, it's
    attributes are used to grab struct elements from. Returns
    a string containing the data.

unpack(format, data, object=None)
    If 'object' is omitted (or None), a new dictionary will be
    returned. If 'object' is a dictionary, it will be used to add
    struct elements to. If it is an instance (or in fact anything
    that has a __dict__ attribute), an attribute will be added for
    each struct element. In the latter two cases, 'object' itself
    is returned.

unpack2(format, data, object=None)
    Convenience function. Same as unpack, except data may be longer
    than needed. The returned value is a tuple: (object, leftoverdata).

calcsize(format)
    like struct.calcsize(), but uses our own format strings:
    it returns the size of the data in bytes.
"""

# XXX I would like to support pascal strings, too, but I'm not
# sure if that's wise. Would be nice if struct supported them
# "properly", but that would certainly break calcsize()...

# Updated to Python 2.7/3.0, CJW



__version__ = "1.2"
__copyright__ = "Copyright 1998, Just van Rossum <just@letterror.com>"

import struct
import re


class SStructError(Exception):
    pass


def pack(format, obj):
    """ Return bytes of values v1, v2, ... packed according to format. """
    formatstring, names, fixes = getformat(format)
    elements = []
    if not isinstance(obj, dict):
        obj = obj.__dict__
    for name in names:
        value = obj[name]
        if name in fixes:
            # fixed point conversion
            value = int(round(value*fixes[name]))
        elements.append(value)
    data = struct.pack(formatstring, *elements)
    return data


def unpack(format, data, obj=None):
    """ Unpack bytes containing packed C structure data, according to format.

    Requires len(bytes) == calcsize(format).

    By default returns a dictionary of data, but can be given existing dict or
    an arbitrary object which has its __dict__ populated.

    """
    if obj is None:
        obj = {}
    formatstring, names, fixes = getformat(format)
    if isinstance(obj, dict):
        d = obj
    else:
        d = obj.__dict__

    elements = struct.unpack(formatstring, data)
    for i in range(len(names)):
        name = names[i]
        value = elements[i]
        if name in fixes:
            # fixed point conversion
            value = value / fixes[name]
        d[name] = value
    return obj


def unpack2(format, data, object=None):
    """ As unpack(), but truncating to length of format """
    length = calcsize(format)
    return unpack(format, data[:length], object), data[length:]


def calcsize(format):
    """ Compute the size of the data structure described by format """
    formatstring, names, fixes = getformat(format)
    return struct.calcsize(formatstring)


# matches "name:formatchar" (whitespace is allowed)
_elementRE = re.compile(
    r"\s*"                           # whitespace
    r"([A-Za-z_][A-Za-z_0-9]*)"      # name (python identifier)
    r"\s*:\s*"                       # whitespace : whitespace
    r"([cbBhHiIlLfd]|[0-9]+[ps]|"    # formatchar...
        r"([0-9]+)\.([0-9]+)(F))"    # ...formatchar                 # noqa
    r"\s*"                           # whitespace
    r"(#.*)?$"                       # [comment] + end of string
)


# matches the special struct format chars and 'x' (pad byte)
_extraRE = re.compile(r"\s*([x@=<>!])\s*(#.*)?$")


# matches an "empty" string, possibly containing whitespace and/or a comment
_emptyRE = re.compile(r"\s*(#.*)?$")


_fixedpointmappings = {
    8: "b",
    16: "h",
    32: "l"
}


_formatcache = {}


def getformat(format):
    """ Convert sstruct format to struct format, names and fixed point data """
    try:
        formatstring, names, fixes = _formatcache[format]
    except KeyError:
        lines = re.split("[\n;]", format)
        formatstring = ""
        names = []
        fixes = {}
        for line in lines:
            if _emptyRE.match(line):
                continue
            m = _extraRE.match(line)
            if m:
                formatchar = m.group(1)
                if formatchar != 'x' and formatstring:
                    raise SStructError("Special format chars must be first")
            else:
                m = _elementRE.match(line)
                if not m:
                    raise SStructError("syntax error in format: '%s'" % line)
                name = m.group(1)
                names.append(name)
                formatchar = m.group(2)
                if m.group(3):
                    # fixed point
                    before = int(m.group(3))
                    after = int(m.group(4))
                    bits = before + after
                    if bits not in [8, 16, 32]:
                        msg = "fixed point must be 8, 16 or 32 bits long"
                        raise SStructError(msg)
                    formatchar = _fixedpointmappings[bits]
                    assert m.group(5) == "F"
                    fixes[name] = float(1 << after)
            formatstring = formatstring + formatchar
        _formatcache[format] = formatstring, names, fixes
    return formatstring, names, fixes
