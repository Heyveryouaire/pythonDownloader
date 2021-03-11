#!usr/bin/python3.8
import subprocess

class textColor:
    SUCCESS = '\33[42m'
    DANGER = '\33[101m'
    END = '\33[0m'

try:
    print('Updating cache...')
    subprocess.run(['sudo', 'apt-get', 'update'])
    print(textColor.SUCCESS + 'Updated !' + textColor.END )
except:
    print(textColor.DANGER + 'Can\'t update cache' + textColor.END)

try:
    print('Upgrading packages...')
    subprocess.run(['sudo', 'apt-get', 'upgrade'])
    print(textColor.SUCCESS + 'Upgraded !' + textColor.END)
except:
    print(textColor.DANGER + 'Can\'t upgrade packages' + textColor.END)

# Test, install GIMP 2
gimp = input('Install GIMP ? (y/n)')
if gimp == 'y':
    try:
        print('Installing GIMP...')
        subprocess.run(['sudo', 'snap', 'install', 'gimp'])
        print(textColor.SUCCESS + 'Gimp installed ! ' + textColor.END)
    except: 
        print(textColor.DANGER + 'Can\'t download GIMP...' + textColor.END)

vsc = input('Install Visual Studio Code ? (y/n)')
if vsc == 'y':
    try:
        print('Installing Visual Studio Code... ')
        subprocess.run(['sudo', 'snap', 'install', '--classic', 'code'])
        print(textColor.SUCCESS + 'Visual Studio Code intalled ! ' + textColor.END)
    except:
        print(textColor.DANGER + 'Can\'t install Visual Studio Code...' + textColor.END)
        
# Check if this work ?
nvm = input('Install NVM ? (y/n)')
if nvm == "y":
    try:
        print('Installing NVM...')
        subprocess.run(['sudo', 'curl', 'https://raw.githubusercontent.com/creationix/nvm/master/install.sh'])
        print(textColor.SUCCESS + 'NVM installed !' + textColor.END)
    except:
        print(textColor.DANGER + 'Can\'t install NVM' + textColor.END)

lamp = input('Install LAMP ? (y/n)')
if lamp == 'y':
    try:
        print('Installing LAMP...')
        subprocess.run(['sudo', 'apt', 'install', 'apache2', 'php', 'libapache2-mod-php', 'mysql-server', 'php-mysql'])
        print(textColor.SUCCESS + 'LAMP installed ! ' + textColor.END)
    except:
        print(textColor.DANGER + 'Can\'t install LAMP' + textColor.END)

discord = input('Install Discord ? (y/n)')
if discord == 'y':
    try:
        print('Installing Discord...')
        subprocess.run(['sudo', 'snap', 'install', 'discord'])
        print(textColor.SUCCESS + 'Discord installed ! ' + textColor.END)
    except:
        print(textColor.DANGER + 'Can\'t install Discord' + textColor.END)

git = input('Install Git ? (y/n)')
if git == 'y':
    try:
        print('Installing Git...')
        subprocess.run(['sudo', 'apt', 'install', 'git-all'])
        print(textColor.SUCCESS + 'Git installed ! ' + textColor.END)
    except:
        print(textColor.DANGER + 'Can\'t git Discord' + textColor.END)

phpmyadmin = input('Install phpMyAdmin ? (y/n)')
if phpmyadmin == 'y':
    try:
        print('Installing Git...')
        subprocess.run(['sudo', 'apt', 'install', 'phpmyadmin'])
        print(textColor.SUCCESS + 'phpMyAdmin installed ! ' + textColor.END)
    except:
        print(textColor.DANGER + 'Can\'t git phpMyAdmin' + textColor.END)

chrome = input('Install Chrome ? (y/n)')
if chrome == 'y':
    try:
        print('Installing Chrome...')
        subprocess.run(['sudo', 'apt-get', 'install', 'google-chrome-stable'])
        print(textColor.SUCCESS + 'Google installed ! ' + textColor.END)
    except:
        print(textColor.DANGER + 'Can\'t git Google' + textColor.END)

