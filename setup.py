import setuptools

setuptools.setup(
    name="plotly_unbrand",
    version="1.0.0",
    url="https://github.com/AKuederle/plotly_unbrand",

    author="Arne Küderle",
    author_email="a.kuederle@gmail.com",

    description="A small package to remove the branding from plotly plots",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "test*"]),

    install_requires=[],

    license='LICENSE',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.5',
    ],
)
