#!/usr/bin/python3 
#
import os
import pathlib
import platform
from os.path import expanduser
import shutil


def get_home_dir():
    return expanduser("~")


def check_config_file_exists(filepath):
    if os.path.isfile(filepath):
        print("[Info] Github credentials file already exist.")
        return True
    else:
        print("[Info] Github credendials file does not exists.")
        return False


def create_new_config_file(filepath):
    print("Creating a new github config file.\n")
    github_api_token = input("Github api token: ")
    github_username = input("Github username: ")
    github_email = input("Github e-mail: ")
    try:
        os.makedirs(os.path.dirname(filepath))
        with open(filepath, "w+") as config_file:
            config_file.write("export GITHUB_API_TOKEN=" + github_api_token)
            config_file.write("\nexport GITHUB_USERNAME=" + github_username)
            config_file.write("\nexport GITHUB_EMAIL=" + github_email)
        config_file.close
        print("Github credentials file created.")
        return True
    except FileNotFoundError:
        print("Couldn't create the file at: " + filepath)
        return False


def load_existing_config_file(config_file_path):
    if platform.system() == "Linux":
        with open(os.path.expanduser("~/.zshrc"), "a") as bash_file:
            bash_file.write("\nsource " + config_file_path)
            bash_file.close
        print("Github api token added at your system.")
    else:
        print("Operational system not recognized!")
        

def install_git_create():
    try:
        pathlib("git-create").rename("/bin/git-create")
        shutil.copy("git-create", "/bin/git-create")
    except IOError:
        print("[Error] - You don't haver permission to create the file.\n\tTry using sudo!")


CONFIG_FILE_PATH= get_home_dir() + "/.githubcredentials/config"

if check_config_file_exists(CONFIG_FILE_PATH) == False:
    if create_new_config_file(CONFIG_FILE_PATH) == True:
        load_existing_config_file(CONFIG_FILE_PATH)
        install_git_create()
else:
    load_existing_config_file(CONFIG_FILE_PATH)