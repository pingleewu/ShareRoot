"""
Defines the Kiva Font class and a utility method to parse free-form font
specification strings into Font instances.
"""



import six

import copy
from kiva.constants import (DEFAULT, DECORATIVE, ROMAN, SCRIPT, SWISS, MODERN,
                            TELETYPE, NORMAL, ITALIC, BOLD, BOLD_ITALIC)

# Various maps used by str_to_font
font_families = {
    'default':    DEFAULT,
    'decorative': DECORATIVE,
    'roman':      ROMAN,
    'script':     SCRIPT,
    'swiss':      SWISS,
    'modern':     MODERN
}
font_styles = {'italic': ITALIC}
font_weights = {'bold': BOLD}
font_noise = ['pt', 'point', 'family']


def str_to_font(fontspec):
    """
    Converts a string specification of a font into a Font instance.
    string specifications are of the form: "modern 12", "9 roman italic",
    and so on.
    """
    point_size = 10
    family = DEFAULT
    style = NORMAL
    weight = NORMAL
    underline = 0
    facename = []
    for word in fontspec.split():
        lword = word.lower()
        if lword in font_families:
            family = font_families[lword]
        elif lword in font_styles:
            style = font_styles[lword]
        elif lword in font_weights:
            weight = font_weights[lword]
        elif lword == 'underline':
            underline = 1
        elif lword not in font_noise:
            try:
                point_size = int(lword)
            except:
                facename.append(word)
    return Font(size=point_size, family=family, weight=weight, style=style,
                underline=underline, face_name=' '.join(facename))


class Font(object):
    """ Font class for device independent font specification.

        It is primarily based on wxPython, but looks to be similar to
        the needs of Mac OS X, etc.

        The family defaults to SWISS so that font rotation will work
        correctly under wxPython.    Revisit as we get more platforms
        defined.
    """

    # Maps the constants for font families to names to use when searching for
    # fonts.
    familymap = {
        DEFAULT: "serif",
        SWISS: "sans-serif",
        ROMAN: "serif",
        MODERN: "sans-serif",
        DECORATIVE: "fantasy",
        SCRIPT: "script",
        TELETYPE: "monospace"
    }

    def __init__(self, face_name="", size=12, family=SWISS, weight=NORMAL,
                 style=NORMAL, underline=0, encoding=DEFAULT):
        if (type(size) != int) or (type(family) != type(SWISS)) or \
            (type(weight) != type(NORMAL)) or (type(style) != type(NORMAL)) or \
            (type(underline) != int) or (not isinstance(face_name, six.string_types)) or \
            (type(encoding) != type(DEFAULT)):
                raise RuntimeError("Bad value in Font() constructor.")
        ### HACK:  C++ stuff expects a string (not unicode) for the face_name, so fix
        ###        if needed.
        ### Only for python < 3
        if six.PY2 and isinstance(face_name, six.text_type):
            face_name = face_name.encode("latin1")
        self.size = size
        self.family = family
        self.weight = weight
        self.style = style
        self.underline = underline
        self.face_name = face_name
        self.encoding = encoding

    def findfont(self):
        """ Returns the file name containing the font that most closely matches
        our font properties.
        """
        from .font_manager import fontManager

        fp = self._make_font_props()
        return str(fontManager.findfont(fp))

    def findfontname(self):
        """ Returns the name of the font that most closely matches our font
        properties
        """
        fp = self._make_font_props()
        return fp.get_name()

    def _make_font_props(self):
        """ Returns a font_manager.FontProperties object that encapsulates our
        font properties
        """
        from .font_manager import FontProperties

        # XXX: change the weight to a numerical value
        if self.style == BOLD or self.style == BOLD_ITALIC:
            weight = "bold"
        else:
            weight = "normal"
        if self.style == ITALIC or self.style == BOLD_ITALIC:
            style = "italic"
        else:
            style = "normal"
        fp = FontProperties(family=self.familymap[self.family], style=style,
                            weight=weight, size=self.size)
        if self.face_name != "":
            fp.set_name(self.face_name)
        return fp

    def _get_name(self):
        return self.face_name

    def _set_name(self, val):
        self.face_name = val

    name = property(_get_name, _set_name)

    def copy(self):
        """ Returns a copy of the font object."""
        return copy.deepcopy(self)

    def __eq__(self, other):
        result = False
        try:
            if (self.family == other.family and
                    self.size == other.size and
                    self.weight == other.weight and
                    self.style == other.style and
                    self.underline == other.underline and
                    self.face_name == other.face_name and
                    self.encoding == other.encoding):
                result = True
        except AttributeError:
            pass
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        fmt = ("Font(size=%d,family=%d,weight=%d, style=%d, face_name='%s', " +
               "encoding=%d)")
        return fmt % (self.size, self.family, self.weight, self.style,
                      self.face_name, self.encoding)
