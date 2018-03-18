# Plotly Unbrand

Dear Plotly-Team,

I love you and your library, but sometimes, I do not openly want to show my love.
Sometimes, when working with a customer or when embedding a plot into a talk, I don't want to have multiple links to your online platform directly next to my data.
Luckily, you seem to be very understanding about this and made it possible for me to remove all traces of your brand (besides the trademark beautiful esthetics, of course) from my plots.
I can just pass this into the config of each plotting call:

```python
from plotly.plotly import plot

UNBRAND_CONFIG = dict(modeBarButtonsToRemove=['sendDataToCloud'], displaylogo=False, showLink=False)
plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])], config=UNBRAND_CONFIG)
```

But sometimes even this is not good enough... I want to be able to do this automatically for all plots in a project (I am so sorry Plotly-Team!).
Therefore, I created this little package.
Now I can do this:

```python
from plotly_unbrand import unbrand
unbrand()

from plotly.plotly import plot

plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])])
plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])])
plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])])
```
... and all my Plots have your logo and links to the cloud platform removed.

## Installation

```
pip install plotly_unbrand
```

### Dependencies

You need to have plotly installed of course...

## Usage

Simple! Import `unbrand` and ran it **before** the first plotly import:
```python
from plotly_unbrand import unbrand
unbrand()

from plotly.plotly import plot

plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])])
plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])])
plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])])
```

This will work with `plot` and `iplot` in their online and offline variant.
It should also work with `cufflings`, though I haven't tested it.

### Wait there is more!

You can use the tools from this package to inject any global configuration you like!

```python
from plotly_unbrand import decorate_all_plot_functions

decorate_all_plot_functions(my_custom_config)

from plotly.plotly import plot
...
```

## But I don't want a separate package just for this?!

Don't worry! The logic is pretty simple and self-explanatory.
You can just copy the decorator from the `__init__.py` and run the decoration logic manually.
