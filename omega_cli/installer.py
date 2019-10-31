import subprocess
import click
from PyInquirer import prompt
import sys

prompt_download = [
    {
        'type': 'confirm',
        'name': 'download_lastest',
        'message': 'Do you want to download the lastest version of Omega?'
    },
]


prompt_build = [
    {
        'type': 'confirm',
        'name': 'build',
        'message': 'Build Omega?'
    },
]


prompts_settings = [
    {
        'type': 'checkbox',
        'name': 'apps',
        'message': 'Check the apps you want to install (default=all)',
        'choices': [
            {
                'name': "calculation",
                'checked': True
            },
            {
                'name': "rpn",
                'checked': True
            },
            {
                'name': "graph",
                'checked': True
            },
            {
                'name': "code",
                'checked': True
            },
            {
                'name': "statistics",
                'checked': True
            },
            {
                'name': "probability",
                'checked': True
            },
            {
                'name': "solver",
                'checked': True
            },
            {
                'name': "sequence",
                'checked': True
            },
            {
                'name': "regression",
                'checked': True
            }
        ]
    },
    {
        'type': 'checkbox',
        'name': 'languages',
        'message': 'Check the languages you want to install (default=all)',
        'choices': [
            {
                'name': "en",
                'checked': True
            },
            {
                'name': "fr",
                'checked': True
            },
            {
                'name': "es",
                'checked': True
            },
            {
                'name': "de",
                'checked': True
            },
            {
                'name': "pt",
                'checked': True
            },
        ]
    },
    {
        'type': 'list',
        'name': 'model',
        'message': 'Select your model',
        'choices': [
            {
                'name': "n0100"
            },
            {
                'name': "n0110"
            }
        ]
    }
]


@click.command()
def main():
    """Execute the complete 
    """
    logo()

    download(prompt(prompt_download))

    settings = prompt(prompts_settings)

    model = settings['model']

    if (prompt(prompt_build)['build']):
        apps = settings['apps']
        languages = settings['languages']

        make_clean(model)
        make(model, apps, languages)

    how_to_flash()

    app_flash(model)
    epsilon_flash(model)

    click.echo('If you encounter a bug, please post it here:')
    click.echo('https://github.com/Omega-Numworks/Omega/issues')
    click.echo()
    click.echo('Thank you for using Omega!')


def logo():
    """Prints the Omega logo
    """
    # Made with pyfiglet
    click.echo("    ____                             ")
    click.echo("   / __ \____ ___  ___  ____ _____ _ ")
    click.echo("  / / / / __ `__ \/ _ \/ __ `/ __ `/ ")
    click.echo(" / /_/ / / / / / /  __/ /_/ / /_/ /  ")
    click.echo(" \____/_/ /_/ /_/\___/\__, /\__,_/   ")
    click.echo("       CLI Installer /____/          ")
    click.echo("")


def download(download_lastest):
    """Clones the lastest Omega
    
    Args:
        download_lastest (bool): True to confirm download.
    """
    if download_lastest['download_lastest']:
        subprocess.run("rm -rf Omega", shell=True)
        subprocess.run("git clone --progress --recursive https://github.com/Omega-Numworks/Omega.git", shell=True)
    
    click.echo("")


def make_clean(model):
    """Delete old builds
    
    Args:
        model (str): Should be n0100 or n0110.
    """
    click.echo("Cleaning build")

    subprocess.run("cd Omega && make MODEL=\"" + model + "\" clean", shell=True, check=True)


def make(model, apps, languages):
    """Build Omega
    
    Args:
        model (str): Should be n0100 or n0110
        apps (list): Apps to install
        languages (list): Languages to install
    """
    click.echo("Making build")

    epsilon_apps = ""
    epsilon_i18n = ""

    for app in apps:
        epsilon_apps += app + " "

    for lang in languages:
        epsilon_i18n += lang + " "

    epsilon_apps = "EPSILON_APPS='" + epsilon_apps + "settings'"
    epsilon_i18n = "EPSILON_I18N='" + epsilon_i18n + "'"

    subprocess.run("cd Omega && make MODEL='" + model + "' " + epsilon_apps + " " + epsilon_i18n, shell=True)
    # rpn graph code statistics probability solver calculation sequence regression settings'
    # EPSILON_I18N='en fr es de pt'


def how_to_flash():
    """Print instructions to flash the calculator
    """
    click.echo(" 1)  Connect your numworks to your computer with the USB cable")
    click.echo(" 2)  Click on the reset button behind the calculator")
    click.echo(" 3)  Press enter")
    input()


def app_flash(model):
    """Execure "make MODEL={model} app_flash"
    
    Args:
        model (str): Should be n0100 or n0110.
    """
    subprocess.run("cd Omega && make MODEL=\"" + model + "\" app_flash", shell=True, check=True)


def epsilon_flash(model):
    """Execure "make MODEL={model} epsilon_flash"
    
    Args:
        model (str): Should be n0100 or n0110.
    """
    subprocess.run("cd Omega && make MODEL=\"" + model + "\" epsilon_flash", shell=True, check=True)


if __name__ == "__main__":
    main()
