"""
Support class that wraps up the boilerplate toolkit calls that virtually all
demo programs have to use.
"""


from traits.api import HasTraits, Instance
from traits.etsconfig.api import ETSConfig
from traitsui.api import Item, View

from enable.api import Component, ComponentEditor, Window

# FIXME - it should be enough to do the following import, but because of the
# PyQt/traits problem (see below) we can't because it would drag in traits too
# early.  Until it is fixed we just assume wx if we can import it.
# Force the selection of a valid toolkit.
#import enable.toolkit
if not ETSConfig.toolkit:
    for toolkit, toolkit_module in (('wx', 'wx'), ('qt4', 'PyQt4')):
        try:
            exec("import " + toolkit_module)
            ETSConfig.toolkit = toolkit
            break
        except ImportError:
            pass
    else:
        raise RuntimeError("Can't load wx or qt4 backend for Chaco.")


if ETSConfig.toolkit == 'wx' or ETSConfig.toolkit == 'qt4':

    class DemoFrame(HasTraits):

        component = Instance(Component)

        traits_view = View(Item('component', editor=ComponentEditor(),
                                show_label=False),
                           resizable=True)

        def _component_default(self):
            return self._create_component()

        def _create_component(self):
            """ Create and return a component which is typically a
            container with nested components """
            raise NotImplementedError


    def demo_main(demo_class, size=(640,480), title="Enable Example"):
        demo_class().configure_traits()


elif ETSConfig.toolkit == 'pyglet':

    from pyglet import app
    from pyglet import clock

    class DemoFrame(object):
        def __init__(self):
            if app:
                window = self._create_window()
                if window:
                    self.enable_win = window
                else:
                    self.enable_win = None
            return

        def _create_component(self):
            """ Create and return a component which is typically a
            container with nested components """
            raise NotImplementedError

        def _create_window(self):
            return Window(self, -1, component=self._create_component())


    def demo_main(demo_class, size=(640,480), title="Enable Example"):
        """ Runs a simple application in Pyglet using an instance of
        **demo_class** as the main window or frame.

        **demo_class** should be a subclass of DemoFrame or the pyglet
        backend's Window class.
        """
        if issubclass(demo_class, DemoFrame):
            frame = demo_class()
            if frame.enable_win is not None:
                window = frame.enable_win.control
            else:
                window = None
        else:
            window = demo_class().control

        if window is not None:
            if not window.fullscreen:
                window.set_size(*size)
            window.set_caption(title)

        app.run()
