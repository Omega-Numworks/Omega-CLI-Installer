from distutils.core import setup

setup(name='omega-cli',
    version='0.1.1',
    description='Omega installer for Numworks',
    author='Quentin Guidée',
    author_email='quentin.guidee@gmail.com',
    url='https://github.com/Omega-Numworks/Omega-CLI-Installer/archive/omega-cli-0.1.1.tar.gz',
    packages=['omega-cli'],
    install_requires=[
        'click',
        'PyInquirer'
    ],
)
