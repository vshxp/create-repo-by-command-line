# Creating repository on Github by Command Line

## Requirements
- Linux or Mac
- Curl
- Github token

## Creating a github token
1. Go to this link: https://github.com/settings/tokens
2. Click on `Personal access tokens` thn click `Generate new token`
3. check  `repo Full control of private repositories` as true
4. Click on `Generate token` at end of the page

## Installing
1. Clone this repository:
```sh
git clone git@github.com:matheusf0/create-repo-by-command-line.git
```
2. `Change` the `line 4` of the file `git-create` with your token that you previously created and `save`
3. Move the file to your /bin and give execution permission
```sh
sudo apt install curl -y && sudo mv git-create /bin && sudo chmod +x /bin/git-create
```

## Usage

Creating a remote repository at Github
```sh
git create <repositoryName>
```