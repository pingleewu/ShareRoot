# This is a redirection file that determines what constitutes a color trait
# in Chaco, and what constitutes the standard colors.

import sys

from traits.etsconfig.api import ETSConfig
from traits.api import List, Str, Trait, Tuple, TraitError

# Color definitions
transparent_color = (0.0, 0.0, 0.0, 0.0)

color_table = {"aliceblue": (0.941, 0.973, 1.000, 1.0),
    "antiquewhite": (0.980, 0.922, 0.843, 1.0),
    "aqua": (0.000, 1.000, 1.000, 1.0),
    "aquamarine": (0.498, 1.000, 0.831, 1.0),
    "azure": (0.941, 1.000, 1.000, 1.0),
    "beige": (0.961, 0.961, 0.863, 1.0),
    "bisque": (1.000, 0.894, 0.769, 1.0),
    "black": (0.000, 0.000, 0.000, 1.0),
    "blanchedalmond": (1.000, 0.922, 0.804, 1.0),
    "blue": (0.000, 0.000, 1.000, 1.0),
    "blueviolet": (0.541, 0.169, 0.886, 1.0),
    "brown": (0.647, 0.165, 0.165, 1.0),
    "burlywood": (0.871, 0.722, 0.529, 1.0),
    "cadetblue": (0.373, 0.620, 0.627, 1.0),
    "chartreuse": (0.498, 1.000, 0.000, 1.0),
    "chocolate": (0.824, 0.412, 0.118, 1.0),
    "coral": (1.000, 0.498, 0.314, 1.0),
    "cornflowerblue": (0.392, 0.584, 0.929, 1.0),
    "cornsilk": (1.000, 0.973, 0.863, 1.0),
    "crimson": (0.863, 0.078, 0.235, 1.0),
    "cyan": (0.000, 1.000, 1.000, 1.0),
    "darkblue": (0.000, 0.000, 0.545, 1.0),
    "darkcyan": (0.000, 0.545, 0.545, 1.0),
    "darkgoldenrod": (0.722, 0.525, 0.043, 1.0),
    "darkgray": (0.663, 0.663, 0.663, 1.0),
    "darkgreen": (0.000, 0.392, 0.000, 1.0),
    "darkgrey": (0.663, 0.663, 0.663, 1.0),
    "darkkhaki": (0.741, 0.718, 0.420, 1.0),
    "darkmagenta": (0.545, 0.000, 0.545, 1.0),
    "darkolivegreen": (0.333, 0.420, 0.184, 1.0),
    "darkorange": (1.000, 0.549, 0.000, 1.0),
    "darkorchid": (0.600, 0.196, 0.800, 1.0),
    "darkred": (0.545, 0.000, 0.000, 1.0),
    "darksalmon": (0.914, 0.588, 0.478, 1.0),
    "darkseagreen": (0.561, 0.737, 0.561, 1.0),
    "darkslateblue": (0.282, 0.239, 0.545, 1.0),
    "darkslategray": (0.184, 0.310, 0.310, 1.0),
    "darkslategrey": (0.184, 0.310, 0.310, 1.0),
    "darkturquoise": (0.000, 0.808, 0.820, 1.0),
    "darkviolet": (0.580, 0.000, 0.827, 1.0),
    "deeppink": (1.000, 0.078, 0.576, 1.0),
    "deepskyblue": (0.000, 0.749, 1.000, 1.0),
    "dimgray": (0.412, 0.412, 0.412, 1.0),
    "dimgrey": (0.412, 0.412, 0.412, 1.0),
    "dodgerblue": (0.118, 0.565, 1.000, 1.0),
    "firebrick": (0.698, 0.133, 0.133, 1.0),
    "floralwhite": (1.000, 0.980, 0.941, 1.0),
    "forestgreen": (0.133, 0.545, 0.133, 1.0),
    "fuchsia": (1.000, 0.000, 1.000, 1.0),
    "gainsboro": (0.863, 0.863, 0.863, 1.0),
    "ghostwhite": (0.973, 0.973, 1.000, 1.0),
    "gold": (1.000, 0.843, 0.000, 1.0),
    "goldenrod": (0.855, 0.647, 0.125, 1.0),
    "gray": (0.502, 0.502, 0.502, 1.0),
    "green": (0.000, 0.502, 0.000, 1.0),
    "greenyellow": (0.678, 1.000, 0.184, 1.0),
    "grey": (0.502, 0.502, 0.502, 1.0),
    "honeydew": (0.941, 1.000, 0.941, 1.0),
    "hotpink": (1.000, 0.412, 0.706, 1.0),
    "indianred": (0.804, 0.361, 0.361, 1.0),
    "indigo": (0.294, 0.000, 0.510, 1.0),
    "ivory": (1.000, 1.000, 0.941, 1.0),
    "khaki": (0.941, 0.902, 0.549, 1.0),
    "lavender": (0.902, 0.902, 0.980, 1.0),
    "lavenderblush": (1.000, 0.941, 0.961, 1.0),
    "lawngreen": (0.486, 0.988, 0.000, 1.0),
    "lemonchiffon": (1.000, 0.980, 0.804, 1.0),
    "lightblue": (0.678, 0.847, 0.902, 1.0),
    "lightcoral": (0.941, 0.502, 0.502, 1.0),
    "lightcyan": (0.878, 1.000, 1.000, 1.0),
    "lightgoldenrodyellow": (0.980, 0.980, 0.824, 1.0),
    "lightgray": (0.827, 0.827, 0.827, 1.0),
    "lightgreen": (0.565, 0.933, 0.565, 1.0),
    "lightgrey": (0.827, 0.827, 0.827, 1.0),
    "lightpink": (1.000, 0.714, 0.757, 1.0),
    "lightsalmon": (1.000, 0.627, 0.478, 1.0),
    "lightseagreen": (0.125, 0.698, 0.667, 1.0),
    "lightskyblue": (0.529, 0.808, 0.980, 1.0),
    "lightslategray": (0.467, 0.533, 0.600, 1.0),
    "lightslategrey": (0.467, 0.533, 0.600, 1.0),
    "lightsteelblue": (0.690, 0.769, 0.871, 1.0),
    "lightyellow": (1.000, 1.000, 0.878, 1.0),
    "lime": (0.000, 1.000, 0.000, 1.0),
    "limegreen": (0.196, 0.804, 0.196, 1.0),
    "linen": (0.980, 0.941, 0.902, 1.0),
    "magenta": (1.000, 0.000, 1.000, 1.0),
    "maroon": (0.502, 0.000, 0.000, 1.0),
    "mediumaquamarine": (0.400, 0.804, 0.667, 1.0),
    "mediumblue": (0.000, 0.000, 0.804, 1.0),
    "mediumorchid": (0.729, 0.333, 0.827, 1.0),
    "mediumpurple": (0.576, 0.439, 0.859, 1.0),
    "mediumseagreen": (0.235, 0.702, 0.443, 1.0),
    "mediumslateblue": (0.482, 0.408, 0.933, 1.0),
    "mediumspringgreen": (0.000, 0.980, 0.604, 1.0),
    "mediumturquoise": (0.282, 0.820, 0.800, 1.0),
    "mediumvioletred": (0.780, 0.082, 0.522, 1.0),
    "midnightblue": (0.098, 0.098, 0.439, 1.0),
    "mintcream": (0.961, 1.000, 0.980, 1.0),
    "mistyrose": (1.000, 0.894, 0.882, 1.0),
    "moccasin": (1.000, 0.894, 0.710, 1.0),
    "navajowhite": (1.000, 0.871, 0.678, 1.0),
    "navy": (0.000, 0.000, 0.502, 1.0),
    "oldlace": (0.992, 0.961, 0.902, 1.0),
    "olive": (0.502, 0.502, 0.000, 1.0),
    "olivedrab": (0.420, 0.557, 0.137, 1.0),
    "orange": (1.000, 0.647, 0.000, 1.0),
    "orangered": (1.000, 0.271, 0.000, 1.0),
    "orchid": (0.855, 0.439, 0.839, 1.0),
    "palegoldenrod": (0.933, 0.910, 0.667, 1.0),
    "palegreen": (0.596, 0.984, 0.596, 1.0),
    "paleturquoise": (0.686, 0.933, 0.933, 1.0),
    "palevioletred": (0.859, 0.439, 0.576, 1.0),
    "papayawhip": (1.000, 0.937, 0.835, 1.0),
    "peachpuff": (1.000, 0.855, 0.725, 1.0),
    "peru": (0.804, 0.522, 0.247, 1.0),
    "pink": (1.000, 0.753, 0.796, 1.0),
    "plum": (0.867, 0.627, 0.867, 1.0),
    "powderblue": (0.690, 0.878, 0.902, 1.0),
    "purple": (0.502, 0.000, 0.502, 1.0),
    "red": (1.000, 0.000, 0.000, 1.0),
    "rosybrown": (0.737, 0.561, 0.561, 1.0),
    "royalblue": (0.255, 0.412, 0.882, 1.0),
    "saddlebrown": (0.545, 0.271, 0.075, 1.0),
    "salmon": (0.980, 0.502, 0.447, 1.0),
    "sandybrown": (0.957, 0.643, 0.376, 1.0),
    "seagreen": (0.180, 0.545, 0.341, 1.0),
    "seashell": (1.000, 0.961, 0.933, 1.0),
    "sienna": (0.627, 0.322, 0.176, 1.0),
    "silver": (0.753, 0.753, 0.753, 1.0),
    "skyblue": (0.529, 0.808, 0.922, 1.0),
    "slateblue": (0.416, 0.353, 0.804, 1.0),
    "slategray": (0.439, 0.502, 0.565, 1.0),
    "slategrey": (0.439, 0.502, 0.565, 1.0),
    "snow": (1.000, 0.980, 0.980, 1.0),
    "springgreen": (0.000, 1.000, 0.498, 1.0),
    "steelblue": (0.275, 0.510, 0.706, 1.0),
    "tan": (0.824, 0.706, 0.549, 1.0),
    "teal": (0.000, 0.502, 0.502, 1.0),
    "thistle": (0.847, 0.749, 0.847, 1.0),
    "tomato": (1.000, 0.388, 0.278, 1.0),
    "turquoise": (0.251, 0.878, 0.816, 1.0),
    "violet": (0.933, 0.510, 0.933, 1.0),
    "wheat": (0.961, 0.871, 0.702, 1.0),
    "white": (1.000, 1.000, 1.000, 1.0),
    "whitesmoke": (0.961, 0.961, 0.961, 1.0),
    "yellow": (1.000, 1.000, 0.000, 1.0),
    "yellowgreen": (0.604, 0.804, 0.196, 1.0),

    # Several aliases for transparent
    "clear": transparent_color,
    "transparent": transparent_color,
    "none": transparent_color,

    # Placeholders for system- and toolkit-specific UI colors; the
    # toolkit-dependent code below will fill these with the appropriate
    # values.  These hardcoded defaults are for the Windows Classic
    # theme.
    "sys_window" : (0.83137, 0.81569, 0.78431, 1.0),
}

if not ETSConfig.toolkit:
    # Force Traits to decide on its toolkit if it hasn't already
    from traitsui.toolkit import toolkit as traits_toolkit
    traits_toolkit()

if ETSConfig.toolkit == 'wx':
    import wx
    from traitsui.wx.color_editor \
                import ToolkitEditorFactory as StandardColorEditorFactory
    # Version dependent imports (ColourPtr not defined in wxPython 2.8):
    try:
        ColourPtr = wx.ColourPtr
    except:
        class ColourPtr ( object ): pass

    # Mostly copied from traits/ui/wx/color_trait.py
    def convert_from_wx_color(obj, name, value):
        if isinstance(value, ColourPtr) or isinstance(value, wx.Colour):
            return (value.Red()/255.0, value.Green()/255.0, value.Blue()/255.0, 1.0)
        elif type(value) is int:
            num = int( value )
            return ((num >> 16)/255.0, ((num>>8) & 0xFF)/255.0, (num & 0xFF)/255.0, 1.0)
        elif type(value) in (list, tuple):
            if len(value) == 3:
                return (value[0]/255.0, value[1]/255.0, value[2]/255.0, 1.0)
            elif len(value) == 4:
                return value
            else:
                raise TraitError
        else:
            raise TraitError


    convert_from_wx_color.info = ('a wx.Colour instance, an integer which in hex is of '
                             'the form 0xRRGGBB, where RR is red, GG is green, '
                             'and BB is blue, a list/tuple of (r,g,b) or (r,g,b,a)')

    # Set the system color
    from traitsui.wx.constants import WindowColor
    color_table["sys_window"] = (WindowColor.Red()/255.0,
                                 WindowColor.Green()/255.0,
                                 WindowColor.Blue()/255.0,
                                 1.0)

    class ColorEditorFactory(StandardColorEditorFactory):

        def to_wx_color(self, editor):
            if self.mapped:
                retval = getattr( editor.object, editor.name + '_' )
            else:
                retval = getattr( editor.object, editor.name )
            if isinstance(retval, tuple):
                retval = wx.Colour(int(255*retval[0]), int(255*retval[1]),
                                   int(255*retval[2]))
            return retval

        def from_wx_color ( self, color ):
            """ Gets the application equivalent of a wxPython value.
            """
            return convert_from_wx_color(self, 'color', color)

        def str_color(self, color):
            if isinstance( color, ( wx.Colour, ColourPtr ) ):
                return "(%d,%d,%d)" % ( color.Red(), color.Green(), color.Blue() )
            elif isinstance(color, tuple):
                fmt = "(" + ",".join(["%0.3f"]*len(color)) + ")"
                return fmt % color
            return color

    ColorTrait = Trait("black", Tuple, List, color_table,
                       convert_from_wx_color, editor=ColorEditorFactory)

elif ETSConfig.toolkit == 'qt4':
    from pyface.qt import QtGui
    from traitsui.qt4.color_editor \
                import ToolkitEditorFactory as StandardColorEditorFactory

    def convert_from_pyqt_color(obj, name, value):
        if isinstance(value, QtGui.QColor):
            return value.getRgbF()
        elif type(value) is int:
            num = int(value)
            return ((num >> 16)/255.0, ((num>>8) & 0xFF)/255.0, (num & 0xFF)/255.0, 1.0)
        elif type(value) in (list, tuple):
            if len(value) == 3:
                return (value[0]/255.0, value[1]/255.0, value[2]/255.0, 1.0)
            elif len(value) == 4:
                return value
            else:
                raise TraitError
        else:
            raise TraitError

    convert_from_pyqt_color.info = ("a QtGui.Color instance, an SVG color "
            "name, an integer which in hex is of the form 0xRRGGBB, where RR "
            "is red, GG is green, and BB is blue, a list/tuple of (r,g,b) or "
        "(r,g,b,a)")

    window_color = QtGui.QApplication.palette().window().color()
    color_table["sys_window"] = (window_color.red()/255.0,
                                 window_color.green()/255.0,
                                 window_color.blue()/255.0,
                                 1.0)


    class ColorEditorFactory(StandardColorEditorFactory):

        def to_qt4_color(self, editor):
            if self.mapped:
                retval = getattr(editor.object, editor.name + '_')
            else:
                retval = getattr(editor.object, editor.name)

            if isinstance(retval, tuple):
                col = QtGui.QColor()
                col.setRgbF(*retval)
                retval = col

            return retval

        def str_color(self, color):
            if isinstance(color, QtGui.QColor):
                color = color.getRgbF()

            if isinstance(color, tuple):
                fmt = "(" + ",".join(["%0.3f"] * len(color)) + ")"
                color =  fmt % color
            return color

    ColorTrait = Trait("black", Tuple, List, color_table,
                       convert_from_pyqt_color, editor=ColorEditorFactory)

else:
    ColorTrait = Trait("black", Tuple, List, Str, color_table)
    ColorEditorFactory = None

black_color_trait = ColorTrait("black")
white_color_trait = ColorTrait("white")
transparent_color_trait = ColorTrait("transparent")

# EOF
