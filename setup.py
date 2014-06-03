# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='android-webview',
    version='0.1.2',
    description='Python script to generate android webview based apps',
    author='Rael Max',
    author_email='contato@raelmax.com',
    url='https://github.com/raelmax/android-webview',
    packages=['awebview'],
    package_data={'awebview': ['templates/*']},
    entry_points={
        'console_scripts': [
            'android-webview = awebview.android_webview:main',
        ]
    }
)

