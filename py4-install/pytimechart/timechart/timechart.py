#!/usr/bin/python3
#------------------------------------------------------------------------------
import sys

def main():
    try:
        from traits.etsconfig.api import ETSConfig
        ETSConfig.toolkit = 'qt4'
        from pyface.api import GUI
    except:
        print("did you install python-chaco?", file=sys.stderr)
        print("maybe you did install chaco>=4, then you will need to install the package etsproxy", file=sys.stderr)
        print("sudo easy_install etsproxy", file=sys.stderr)
        raise

    # select the toolkit we want to use or just let auto detection
    # WX is more stable for now
    #ETSConfig.toolkit = 'qt4'
    #ETSConfig.toolkit = 'wx'
    print("DEBUG - toolkit is using  ", ETSConfig.toolkit)
    raise_to_debug(3, __file__)

    # workaround bad bg color in ubuntu, with Ambiance theme
    # wxgtk (or traitsGUI, I dont know) looks like using the menu's bgcolor 
    # for all custom widgets bg colors. :-(

    import os

    if ETSConfig.toolkit == 'wx':
        import wx, os
        if "gtk2" in wx.PlatformInfo:
            from gtk import rc_parse, MenuBar
            m = MenuBar()
            if m.rc_get_style().bg[0].red_float < 0.5: # only customize dark bg
                rc_parse(os.path.join(os.path.dirname(__file__),"images/gtkrc"))
            m.destroy()

    # workaround bug in kiva's font manager that fails to find a correct default font on linux
    if os.name=="posix":
        import warnings
        def devnull(*args):
            pass
        warnings.showwarning = devnull
        from  kiva.fonttools.font_manager import fontManager, FontProperties
        try:
            font = FontProperties()
            font.set_name("DejaVu Sans")
            fontManager.defaultFont = fontManager.findfont(font)
            fontManager.warnings = None
        except: # this code will throw exception on ETS4, which has actually fixed fontmanager
            pass

    from window import open_file



    import optparse
    parser = optparse.OptionParser(usage="""\
%prog [options] [trace.txt|trace.txt.gz|trace.txt.lzma|trace.dat]

pytimechart - Fast graphical exploration and visualisation for linux kernel traces.""")
    parser.add_option("-p", "--prof", dest="prof", action="store_true",
                      help="activate profiling",
                      default=False)
    (options, args) = parser.parse_args()

    # Create the GUI (this does NOT start the GUI event loop).
    gui = GUI()
    if len(args) == 0:
        args.append("dummy")
    for fn in args:
        if not open_file(fn):
            sys.exit(0)
    if options.prof:
        import cProfile
        dict = {"gui":gui}
        cProfile.runctx('gui.start_event_loop()',dict,dict,'timechart.prof')
    else:
        gui.start_event_loop()

def raise_to_debug(level, file):
    # traitsui/traitsui/api.py  raise_to_debug()
    # caller pass in level range 1..3
    noBreak=4
    doBreak=3
    moreBreak=2
    one = "1"
    import os, sys
    env = os.getenv("PYTHONBREAKPOINT")
    if env == one and level >= noBreak:
        print("Debug break: ", file)
        breakpoint()
    elif level == 0:
        print("Debug INFO: ", file)

if __name__ == '__main__':
    #import py2exe_wximports
    main()

##### EOF #####################################################################
