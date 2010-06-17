from distutils.core import setup

setup(
    name='jsplot',
    version="0.1",
    license='MIT',
    author='Ondrej Certik',
    packages=['jsplot', 'plotserver', 'plotserver.app'],
    package_data={'plotserver': ['templates/*.html', 'media_files/css/*.css',
        'media_files/js/*.js']},
)
