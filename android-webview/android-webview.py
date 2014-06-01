# -*- coding: utf-8 -*-
import os

app_name = raw_input("App NAME: ")
app_url = raw_input("App URL: ")
app_path = raw_input("App PATH: ")
app_package = raw_input("Package Name: ")

os.system('android create project --target 1 --name {0} --path {1} --activity MainActivity \
 --package {2}'.format(app_name, app_name, app_package))
