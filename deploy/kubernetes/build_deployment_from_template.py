#!/usr/bin/python

import os, pprint, json
from jinja2 import Template, Environment, FileSystemLoader



# Jenkins Build Path, Docker
JENKINS_WORKSPACE = os.environ['WORKSPACE']
KUBERNETES_CONFIG_HOME = JENKINS_WORKSPACE + '/deploy/kubernetes'

print 'Loading Template from {0}'.format(KUBERNETES_CONFIG_HOME)
# Initialize the Jinja2 templating FileSystem.
kube_template_loader = FileSystemLoader(KUBERNETES_CONFIG_HOME)

# Initialize the Jinja2 templating Environment.
kube_template_env = Environment(loader=kube_template_loader, keep_trailing_newline=True)

# get the 'to be rendered templates' from within the loaded jinja2 Environment.
KUBERNETES_CONFIG_TEMPLATE = kube_template_env.get_template( './deployment.template' )

def get_bash_env_vars_as_dict():
    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = '"'

    func_replace_single_with_double_quote = \
        lambda quoted_string: quoted_string.replace(SINGLE_QUOTE, DOUBLE_QUOTE).replace("\\","")
    bash_env_vars_as_string = func_replace_single_with_double_quote(str(os.environ))
    bash_env_vars_as_dict = json.loads(bash_env_vars_as_string)
    return bash_env_vars_as_dict


# get the current session's BASH ENV vars as dict object
bash_env_vars_as_dict = get_bash_env_vars_as_dict()

def check_valid_env_var_dict():
    if all(k in bash_env_vars_as_dict for k in ("ENV", "VERSION")):
        return True
    else:
        return False

# Render the template & handle any Exceptions gracefully.
if check_valid_env_var_dict():
    try:
        rendered_kube_template = KUBERNETES_CONFIG_TEMPLATE.render(**bash_env_vars_as_dict)
        KUBERNETES_DEPLOY_FILE = KUBERNETES_CONFIG_HOME + '/'+ bash_env_vars_as_dict['ENV'] + '/' + 'deployment.yaml'

        with open(KUBERNETES_DEPLOY_FILE, 'w+') as KUBE_DEPLOY_CONFIG_YAML_FD:
            KUBE_DEPLOY_CONFIG_YAML_FD.write(rendered_kube_template)

    except Exception as jinja2_render_exception:
        print 'Exception while trying to render the KUBE Config Template - {0}'.format(jinja2_render_exception)

else:
    print 'Missing BASH ENV Variables, please check the session env vars'
