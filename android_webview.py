# -*- coding: utf-8 -*-
import os
import sys

if os.system('which android') != 0:
    sys.exit('Android SDK is not installed. :(')

MSG= {
    'success': '\033[92m{0}\033[0m',
    'question': '\033[91m{0}\033[0m',
}

app_name = raw_input(MSG['question'].format('App NAME: '))
app_url = raw_input(MSG['question'].format('App URL: '))
app_package = raw_input(MSG['question'].format('Package Name: '))
print '\n'

package_dir = app_package.replace('.', '/')

os.system('android create project --target 1 --name {0} --path {1} --activity MainActivity \
          --package {2}'.format(app_name, app_name, app_package))

# copy AndroidManifest.xml
manifest = open('templates/AndroidManifest.xml').read()
manifest_webview = manifest.replace('{{package_name}}', app_package)

new_manifest = open('{0}/AndroidManifest.xml'.format(app_name), 'w')
new_manifest.write(manifest_webview)
new_manifest.close()

# copy MainActivity.java
main_activity = open('templates/MainActivity.java').read()
main_activity_webview = main_activity.replace('{{package_name}}', app_package)
main_activity_webview = main_activity_webview.replace('{{app_url}}', app_url)

new_main_activity = open('{0}/src/{1}/MainActivity.java'.format(app_name, package_dir), 'w')
new_main_activity.write(main_activity_webview)
new_main_activity.close()
print '\n'
print MSG['success'].format('App generated! Open project on Eclipse and run! :)')
