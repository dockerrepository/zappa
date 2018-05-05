
# initialize a python virtual environ
function init_venv(){
  # Create venv if not exists
  if [ ! -f /var/venv/bin/activate ]; then
      echo "Creating /var/venv."
      python3 -m venv /var/venv
      echo "done."
  fi
}

# Activate the venv
function activate_venv(){
  source /var/venv/bin/activate
}

zappa_version_os=$(pip freeze | grep zappa)

function install_zappa_in_venv(){
  activate_venv
  zappa_version_venv=$(pip freeze | grep zappa)
  if [ "$zappa_version_venv" = "" ]; then
      echo "Installing $zappa_version_os in venv."
      pip install $zappa_version_os > /dev/null
      pip install "pip==9.0.3" > /dev/null
      echo "done."
  fi
}

init_venv

activate_venv

install_zappa_in_venv