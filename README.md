# Creating repository on Github by Command Line

## Requirements
- Linux or Mac
- Curl
- Github token

## Creating a github token
1. Go to this link: https://github.com/settings/tokens
2. Click on `Personal access tokens` then click `Generate new token`
3. Check `repo Full control of private repositories` as true
4. Click on `Generate token` at end of the page

## Installing
1. Clone this repository:
```sh
git clone git@github.com:matheusf0/create-repo-by-command-line.git
```
2. Give executable permission to files `install.py` and `git-create` file.
```
chmod +x install.py git-create
``` 
3. Run the install.sh 
```sh
./install.py
```

# Usage

Creating a remote repository at Github
```sh
git create <repositoryName>
```