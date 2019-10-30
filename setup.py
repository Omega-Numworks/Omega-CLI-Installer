from distutils.core import setup

setup(name='omega-cli',
    version='0.1.3',
    description='Omega installer for Numworks',
    author='Quentin Guidée',
    author_email='quentin.guidee@gmail.com',
    url='https://github.com/Omega-Numworks/Omega-CLI-Installer/releases/download/0.1.3/omega-cli-0.1.3.tar.gz',
    packages=['omega_cli'],
    install_requires=[
        'click',
        'PyInquirer'
    ],
    entry_points={
        'console_scripts': ['omega-cli=omega_cli.installer:main'],
    }
)
