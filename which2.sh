# shellcheck shell=sh
# Initialization script for bash, sh, mksh and ksh

case "$(cat /proc/$$/comm)" in
ksh|mksh)
    which_declare=""
    which_opt=""
    ;;
zsh)
    which_declare="typeset -f"
    which_opt=""
    ;;
*)
    which_declare="declare -f"
    which_opt="-f"
    ;;
esac

which () {
    (alias; eval ${which_declare}) | /usr/bin/which --tty-only --read-alias --read-functions --show-tilde --show-dot $@
}

export which_declare
export ${which_opt} which
