# Zappa
[Zappa](https://github.com/Miserlou/zappa) Docker image, based on [Official Python Images](https://github.com/docker-library/python)

* Requires Docker to be installed and running [Docker Install](https://docs.docker.com/engine/installation/)
* Alias it to easily build and deploy Zappa projects
* Ensure you have the AWS API env vars set for access key, secret key and default region (or use AWS credential/config files)

## Use [Zappa image](https://hub.docker.com/r/dockerrepository/zappa/)

```bash
# Python 2.7
$ docker pull dockerrepository/zappa:2.7

# Python 3.6
$ docker pull dockerrepository/zappa:3.6
```

## Or Build the image
```bash
$ git clone https://github.com/dockerrepository/zappa.git
# Build Python 2.7
cd python-2.7 && docker build -t zappa-27 .
# Build Python 3.6
cd python-3.6 && docker build -t zappa-36 .
```

## Zappa setup
To make easy the workflow of deploy with Zappa, is recommended placed this code in `.bashrc` or any other equivallent.
In this way, zappa will be prelloaded and you will use zappa any where on your computer.

## Zappa with AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION
Zappa will try use only (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION) to deploy.

```bash

export VIRTUALENV_DIR=$HOME/.virtualenvs # Used to cache builds and reuse.

# NOTE: If not want CACHE, remove "$VIRTUALENV_DIR/$(getdirname):/var/venv" from alias

getdirname(){
	basename $(pwd)
}

alias zappashell27='docker run -ti -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION -v $VIRTUALENV_DIR/$(getdirname):/var/venv -v $(pwd):/var/task --rm dockerrepository/zappa:2.7 bash'
alias zappashell36='docker run -ti -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION -v $VIRTUALENV_DIR/$(getdirname):/var/venv -v $(pwd):/var/task --rm dockerrepository/zappa:3.6 bash'
```

###  Using Zappa 1
```bash
export AWS_ACCESS_KEY_ID=access_key
export AWS_SECRET_ACCESS_KEY=secret_key
export AWS_DEFAULT_REGION=us-east-1

$ zappashell36
#Creating virtualenv (/var/venv).
#Installing zappa(zappa==0.46.1) in virtualenv(/var/venv).
# Install your requirements
zappashell36> pip install -r requirements.txt
# Deploy the project
# zappa deploy <environment>
zappashell36> zappa deploy staging
# update project
zappashell36> zappa update staging
```


## Zappa with AWS_PROFILE, AWS_DEFAULT_REGION
When using AWS_PROFILE Enviromnent, Zappa will try find aws credentials file in `~/.aws/credentials`
```bash

export AWS_CREDENTIALS_DIR=~/.aws #AWS Credentials: https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html
export VIRTUALENV_DIR=$HOME/.virtualenvs # Used to cache builds and reuse.

# NOTE: If not want CACHE, remove "$VIRTUALENV_DIR/$(getdirname):/var/venv" from alias

getdirname(){
	basename $(pwd)
}

alias zappashell27='docker run -ti -e AWS_PROFILE=$AWS_PROFILE -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION -v $VIRTUALENV_DIR/$(getdirname):/var/venv -v $(pwd):/var/task -v $AWS_CREDENTIALS_DIR:/root/.aws --rm dockerrepository/zappa:2.7 bash'
alias zappashell36='docker run -ti -e AWS_PROFILE=$AWS_PROFILE -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION -v $VIRTUALENV_DIR/$(getdirname):/var/venv -v $(pwd):/var/task -v $AWS_CREDENTIALS_DIR:/root/.aws --rm dockerrepository/zappa:3.6 bash'
```

Zappa also requires this twos environment variables. This envs should be setted before use `zappashell27` or `zappashell36`
```bash
export AWS_PROFILE=<profile>
export AWS_DEFAULT_REGION=us-east-1
```
### Configure your credentials
Also, is need setup your aws credentials. This link describe how. 
https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html


###  Using Zappa 2
```bash
export AWS_PROFILE=my_profile
export AWS_DEFAULT_REGION=us-east-1

$ zappashell36
#Creating virtualenv (/var/venv).
#Installing zappa(zappa==0.46.1) in virtualenv(/var/venv).
# Install your requirements
zappashell36> pip install -r requirements.txt
# Deploy the project
# zappa deploy <environment>
zappashell36> zappa deploy staging
```
