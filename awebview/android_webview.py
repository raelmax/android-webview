# -*- coding: utf-8 -*-
import os
import sys
from pkg_resources import Requirement, resource_filename


if os.system('which android') != 0:
    sys.exit('Android SDK is not installed. :(')


def message(msgtype, text, example=''):
    MSG= {
        'success': '\033[92m{0}\033[0m',
        'question': '\033[91m{0}\033[0m {1}: ',
    }
    return MSG[msgtype].format(text, example)


def get_template(name):
    TEMPLATES_PATH = resource_filename(Requirement.parse('android-webview'), 'awebview/templates')
    return os.path.join(TEMPLATES_PATH, name)


def replace_templates(params):
    # copy AndroidManifest.xml
    manifest = open(get_template('AndroidManifest.xml')).read()
    manifest_webview = manifest.replace('{{package_name}}', params['app_package'])

    new_manifest = open('{0}/AndroidManifest.xml'.format(params['app_name']), 'w')
    new_manifest.write(manifest_webview)
    new_manifest.close()

    # copy MainActivity.java
    main_activity = open(get_template('MainActivity.java')).read()
    main_activity_webview = main_activity.replace('{{package_name}}', params['app_package'])
    main_activity_webview = main_activity_webview.replace('{{app_url}}', params['app_url'])

    new_main_activity = open('{0}/src/{1}/MainActivity.java'.format(params['app_name'], params['package_dir']), 'w')
    new_main_activity.write(main_activity_webview)
    new_main_activity.close()


def main():
    params = {}
    params['app_name'] = raw_input(message('question', 'App name', '[myapp]'))
    params['app_url'] = raw_input(message('question', 'App url', '[http://mobile.myapp.com]'))
    params['app_package'] = raw_input(message('question', 'Java package name', '[com.myapp.mobile]'))
    params['package_dir'] = params['app_package'].replace('.', '/')
    print '\n'

    os.system('android create project --target 1 --name {0} --path {1} --activity MainActivity \
              --package {2}'.format(params['app_name'], params['app_name'], params['app_package']))

    print '\n'
    print message('success', 'App generated! Open project on Eclipse and run! :)')

if __name__ == '__main__':
    main()
