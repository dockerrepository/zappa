
# initialize a python virtual environ
function init_venv(){
  # Create venv if not exists
  if [ ! -f /var/venv/bin/activate ]; then
      echo "Creating virtualenv (/var/venv)."
      python3 -m venv /var/venv
      echo "done."
  fi
}

# Activate the venv
function activate_venv(){
  source /var/venv/bin/activate
}

function install_zappa_in_venv(){
  activate_venv
  installed_zappa_version=$(python -m pip freeze | grep zappa)
  requirments_zappa_version=$(cat /root/requirements.txt | grep zappa)
  if [ "$installed_zappa_version" != "$requirments_zappa_version" ]; then
      echo "Installing zappa($requirments_zappa_version) in virtualenv(/var/venv)."
      python -m pip install -r /root/requirements.txt > /root/pip-log-requirements.txt
      echo "Logs: /root/pip-log-requirements.txt"
      echo "done."
  fi
}

init_venv

activate_venv

install_zappa_in_venv