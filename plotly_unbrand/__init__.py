import plotly.plotly
import plotly.offline

from functools import wraps

GLOBAL_CONFIG = config = dict(modeBarButtonsToRemove=[
                              'sendDataToCloud', 'autoScale2d', 'lasso2d', 'select2d'], displaylogo=False, showTips=True, showLink=False)

def unbrand_plot(plot_func):
    @wraps(plot_func)
    def unbranded(*args, **kwargs):
        config = kwargs.pop('config', {})
        kwargs['config'] = {**GLOBAL_CONFIG, **config}
        return plot_func(*args, **kwargs)
    if getattr(unbranded, '__wrapped', False) is True:
        return plot_func
    unbranded.__wrapped = True
    return unbranded


def unbrand(custom_config=None):
    config = custom_config or GLOBAL_CONFIG

    plotly.plotly.plot = unbrand_plot(plotly.plotly.plot)
    plotly.offline.plot = unbrand_plot(plotly.offline.plot)
    plotly.plotly.iplot = unbrand_plot(plotly.plotly.iplot)
    plotly.offline.iplot = unbrand_plot(plotly.offline.iplot)
