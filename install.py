#!/usr/bin/python3 

import os
from pathlib import Path
from os.path import expanduser
import platform
import shutil



def get_home_dir():
    return expanduser("~")


def check_config_file_exists(filepath):
    if os.path.isfile(filepath):
        print ("[Info] Github credentials file already exist.")
        return True
    else:
        print ("[Info] Github credendials file does not exists.")
        return False


def check_config_folder_exists():
    isExist = os.path.exists(get_home_dir() + "/.gitcredentials")
    if not isExist:
        print ("Creating .gitcredentials folder at " + get_home_dir())        
        os.makedirs(get_home_dir() + "/.gitcredentials")
        print("The new directory is created!")
    else:
        print("[Info] .gitcredentials folder already exists!")


def load_existing_config_file():
    if platform.system() == "Linux":
        with open(os.path.expanduser(CONFIG_FILE_PATH), "r") as config_file:
            config_file.seek(0)
            github_api_token = config_file.readline()
            config_file.seek(1)
            github_username = config_file.readline()
            config_file.close
            config_file.seek(2)
            github_email = config_file.readline()
            config_file.close
        with open(os.path.expanduser("~/.bashrc"), "a") as bash_file:
            bash_file.write("\nexport " + github_api_token)
            bash_file.write("\nexport " + github_username)
            bash_file.write("\nexport " + github_email)
            bash_file.close
        print("Github api token added at you system.")
    else:
        print("Operational system not recognized!")


def create_new_config_file(filepath):
    print("Creating a new github config file.\n")
    github_api_token = input("Github api token: ")
    github_username = input("Github username: ")
    github_email = input("Github e-mail: ")
    try:
        with open(filepath, "w+") as config_file:
            config_file.write("GITHUB_API_TOKEN=" + github_api_token)
            config_file.write("\nGITHUB_USERNAME=" + github_username)
            config_file.write("\nGITHUB_EMAIL=" + github_email)
        config_file.close
        print("Github credentials file created.")
    except FileNotFoundError:
        print("Couldn't create the file at: " + CONFIG_FILE_PATH)


def get_recreate_anwser():
    while True:
        try:
            value = input("You already have a credential file, Do you want to re-create it?\nType 'y' to yes or 'n' to no: ")
        except ValueError:
            print("Sorry, I didn't understand that.")
        if value == "y" or value == "yes" or value == "Y":
            create_new_config_file(CONFIG_FILE_PATH)
            break
        else:
            print("Re-creation file canceled, you can manualy see the file at: " + CONFIG_FILE_PATH)
            break


CONFIG_FILE_PATH = get_home_dir() + "/.gitcredentials/config"

if check_config_file_exists(CONFIG_FILE_PATH) is False:
        check_config_folder_exists()
        create_new_config_file(CONFIG_FILE_PATH)
        load_existing_config_file()
else:
    get_recreate_anwser()
try:
    Path("./git-create").rename("/bin/git-create")
    shutil.copy("./git-create", "/bin/git-create")
except IOError:
    print("[Error] - You can't move the file.\n\tTry using sudo!\n\n\t sudo ./install.py")
