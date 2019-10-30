from distutils.core import setup

setup(name='omega-cli',
    version='0.1.2',
    description='Omega installer for Numworks',
    author='Quentin Guidée',
    author_email='quentin.guidee@gmail.com',
    url='https://github.com/Omega-Numworks/Omega-CLI-Installer/releases/download/0.1.2/omega-cli-0.1.2.tar.gz',
    packages=['omega-cli'],
    install_requires=[
        'click',
        'PyInquirer'
    ],
)
