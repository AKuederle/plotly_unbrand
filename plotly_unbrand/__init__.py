import plotly.plotly
import plotly.offline

from functools import wraps

UNBRAND_CONFIG = dict(modeBarButtonsToRemove=['sendDataToCloud'], displaylogo=False, showTips=True, showLink=False)


def inject_config(injected_config, force_wrap=False):
    """Decorator that injects additional configuration into the plotly plot.

    The config passed to the plotting function itself will always overwrite the config provided by the decorator.

    Arguments:
        plot_func: The plotting function that should be decorated. e.g. `plot` or 'iplot'
        injected_config: Dictionary of configurations, which will be passed to every call of the decorated function.

    Example:

        >>> from plotly.offline import iplot
        >>> iplot = inject_config({'config_key': 'config_val'})(iplot)
        >>> iplot(my_figure)  # calls iplot with the injected config
    
    Note: Use `decorate_all_plot_functions` to decorate plot and iplot (offline and online versions) globally.
    """
    def decorator(plot_func):
        @wraps(plot_func)
        def inner(*args, **kwargs):
            config = kwargs.pop('config', {})
            kwargs['config'] = {**injected_config, **config}
            return plot_func(*args, **kwargs)
        return inner
    return decorator


def decorate_all_plot_functions(config):
    """Globally inject configuration values into all plotly functions.

    The following functions are overwritten:

    - plotly.plotly.plot
    - plotly.offline.plot
    - plotly.plotly.iplot
    - plotly.offline.iplot

    Must be called before any direct import of the respective functions!

    Arguments:
        config: Dictionary of configurations that will be injected in each function.
    """
    decorator = inject_config(config)

    plotly.plotly.plot = decorator(plotly.plotly.plot)
    plotly.offline.plot = decorator(plotly.offline.plot)
    plotly.plotly.iplot = decorator(plotly.plotly.iplot)
    plotly.offline.iplot = decorator(plotly.offline.iplot)


def unbrand():
    """Inject a configuration into all plotly plot functions, that removes all "brand" related elements

    Must be called before any plotly import of the respective functions!

    The removed objects are:

    - "edit in Chart Studio" in the toolbar
    - plotly logo in the toolbar
    - "export to plot.ly" link in the bottom right
    """
    decorate_all_plot_functions(UNBRAND_CONFIG)
