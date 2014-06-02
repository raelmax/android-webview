# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='android-webview',
    version='0.1',
    description='Python script to generate android webview based apps',
    author='Rael Max',
    author_email='contato@raelmax.com',
    url='https://github.com/raelmax/android-webview',
    entry_points={
        'console_scripts': [
            'android-webview = android_webview',
        ]
    },
    package_data={'templates': ['templates/*']}
)

