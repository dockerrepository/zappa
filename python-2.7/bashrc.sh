
# initialize a python virtual environ
function init_venv(){
  # Create venv if not exists
  if [ ! -f /var/venv/bin/activate ]; then
      echo "Creating virtualenv (/var/venv)."
      virtualenv /var/venv
      echo "done."
  fi
}

# Activate the venv
function activate_venv(){
  source /var/venv/bin/activate
}

function install_zappa_in_venv(){
  activate_venv
  zappa_version_venv=$(pip freeze | grep zappa)
  echo "zappa_version_venv" $zappa_version_venv
  if [ "$zappa_version_venv" = "" ]; then
      echo "Installing zappa in virtualenv (/var/venv)."
      pip install -r /root/requirements.txt > /dev/null
      echo "done."
  fi
}

init_venv

activate_venv

install_zappa_in_venv