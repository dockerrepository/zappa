import json
import os
import subprocess
import argparse
import logging
from poyo import parse_string

parser = argparse.ArgumentParser(description='Script to handle lambda environment variables')

# logging.basicConfig(level=logging.DEBUG)

parser.add_argument('action', type=str, help='Action (update-envs)')
parser.add_argument('environment', type=str, help='Enviromnent (staging, production)')
parser.add_argument('--project_path', type=str, required=True, help='Path to project')

args = parser.parse_args()

BASE_LAMBDA_CMD = 'aws lambda update-function-configuration --function-name=%s'


def exec_cmd(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, _ = p.communicate()
    return out.decode('utf-8')


def _before_run():
    aws_profile = exec_cmd('echo $AWS_PROFILE')
    print('app: ' + aws_profile)
    aws_region = exec_cmd('echo $AWS_DEFAULT_REGION')
    print('region: ' + aws_region)


def run(command):
    _before_run()
    return exec_cmd(command)


def set_env(key, value):
    print('export {0}="{1}"'.format(key, value))


def update_envs(lambda_name, VARIABLES):
    variables = '{"Variables": %s}' % VARIABLES
    aws_lambda_cmd = BASE_LAMBDA_CMD % lambda_name
    aws_lambda_cmd = aws_lambda_cmd + " --environment '%s' " % variables
    print('starting')
    print(run(aws_lambda_cmd))
    print('done')


def show_envs(lambda_name):
    aws_lambda_cmd = BASE_LAMBDA_CMD % lambda_name
    print('starting')
    print(run(aws_lambda_cmd))
    print('done')


def get_environment_keys(environ_path):
    """"""
    env_file = open(environ_path, 'r')
    dict_envs = {}
    for line in env_file.readlines():
        line = line.replace('\n', '').strip()
        if line and not line.startswith("#"):
            k, v = line.split('=', 1)
            dict_envs[k] = v

    return dict_envs


def parse_config(config_path):
    config_file = open(config_path, 'r')
    content = config_file.read().strip()
    config = parse_string(content)
    return config


def main():
    config = parse_config(os.path.join(args.project_path, 'config-env.yml'))
    environments = config.get('environments', {})
    environ = environments.get(args.environment, {})

    if environ:
        environ_path = environ.get('environment_variable_file', '')

        if environ_path.startswith('/'):
            path_environ = environ_path
        else:
            path_environ = os.path.join(args.project_path, environ_path)

        dict_envs = get_environment_keys(path_environ)
        variable_dict = json.dumps(dict_envs)

        dict_export = {}
        dict_export['VARIABLES'] = '%s' % variable_dict
        dict_export['AWS_DEFAULT_REGION'] = environ.get('aws_region', '')
        dict_export['AWS_PROFILE'] = environ.get('aws_profile', '')
        lambda_name = dict_export['LAMBDA_NAME'] = environ.get('application_name', '')

    for k, v in dict_export.items():
        # Set environ to be used to call lambda
        os.environ[k] = v

    action = args.action
    if action == 'update':
        update_envs(lambda_name, variable_dict)
    elif action == 'show':
        show_envs(lambda_name)


if __name__ == '__main__':
    main()
