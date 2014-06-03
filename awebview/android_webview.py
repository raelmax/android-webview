# -*- coding: utf-8 -*-
import os
import sys
from pkg_resources import Requirement, resource_filename


MSG= {
    'green': '\033[92m{0}\033[0m',
    'red': '\033[91m{0}\033[0m',
}

PARAMS = {
    'has_convert': True
}


if os.system('which android') != 0:
    sys.exit('Android SDK is not installed. :(')


if os.system('which convert') != 0:
    PARAMS['has_convert'] = False
    print MSG['red'].format('ImageMagick not installed, are unable to generate icons. :(\n')


def get_template(name):
    TEMPLATES_PATH = resource_filename(Requirement.parse('android-webview'), 'awebview/templates')
    return os.path.join(TEMPLATES_PATH, name)


def replace_templates():
    # copy AndroidManifest.xml
    manifest = open(get_template('AndroidManifest.xml')).read()
    manifest_webview = manifest.replace('{{package_name}}', PARAMS['app_package'])

    new_manifest = open('{0}/AndroidManifest.xml'.format(PARAMS['app_name']), 'w')
    new_manifest.write(manifest_webview)
    new_manifest.close()

    # copy MainActivity.java
    main_activity = open(get_template('MainActivity.java')).read()
    main_activity_webview = main_activity.replace('{{package_name}}', PARAMS['app_package'])
    main_activity_webview = main_activity_webview.replace('{{app_url}}', PARAMS['app_url'])

    new_main_activity = open('{0}/src/{1}/MainActivity.java'.format(PARAMS['app_name'], PARAMS['package_dir']), 'w')
    new_main_activity.write(main_activity_webview)
    new_main_activity.close()

    # copy strings.xml
    strings = open(get_template('strings.xml')).read()
    strings_named = strings.replace('{{app_name}}', PARAMS['app_name'])

    new_strings = open('{0}/res/values/strings.xml'.format(PARAMS['app_name']), 'w')
    new_strings.write(strings_named)
    new_strings.close()


def make_icons():
    SIZES = {
        'ldpi': '36x36',
        'mdpi': '48x48',
        'hdpi': '72x72',
        'xhdpi': '96x96'
    }

    print MSG['red'].format('Where are the image? '), '[/home/myuser/images/my-full-image.png]'
    PARAMS['icon_path'] = raw_input('>>> ')

    for k, v in SIZES.iteritems():
        print MSG['red'].format('Generating {0} icon...'.format(k.upper()))
        os.system('convert -background none {0} -resize {1} \
                  {2}/res/drawable-{3}/ic_launcher.png'.format(PARAMS['icon_path'], v, PARAMS['app_name'], k))

    print MSG['green'].format('\nIcons generated. :)')


def main():
    print MSG['red'].format('What\'s your app name? '), '[myapp]'
    PARAMS['app_name'] = raw_input('>>> ')

    print MSG['red'].format('What\'s your app url? '), '[http://mobile.myapp.com]'
    PARAMS['app_url'] = raw_input('>>> ')

    print MSG['red'].format('What\'s your java package name? '), '[com.myapp.mobile]'
    PARAMS['app_package'] = raw_input('>>> ')
    PARAMS['package_dir'] = PARAMS['app_package'].replace('.', '/')
    print '\n'

    os.system('android create project --target 1 --name {0} --path {1} --activity MainActivity \
              --package {2}'.format(PARAMS['app_name'], PARAMS['app_name'], PARAMS['app_package']))

    replace_templates()

    if PARAMS['has_convert']:
        print MSG['red'].format('\nYour app are done. You want generate a icon to him? '), '[yes/no]'
        PARAMS['make_icons'] = raw_input('>>> ')

        if PARAMS['make_icons'] == 'yes':
            make_icons()
        else:
            print MSG['green'].format('\nOk, we will use default android app icon. :)')

    print MSG['green'].format('\nApp generated! Open project on Eclipse and run! :)')


if __name__ == '__main__':
    main()
