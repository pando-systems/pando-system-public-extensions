(mkdir .mypy_cache; mypy pandos-extensions/${1}/src/ --ignore-missing-imports --install-types --non-interactive --explicit-package-bases)