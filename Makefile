FILE=config

define \n


endef

CONFIG := $(file <${FILE})
CONFIG_AS_LIST := $(subst ${\n}, ,${CONFIG})
DOMAIN := $(word 1,${CONFIG_AS_LIST})
REPO := $(word 2,${CONFIG_AS_LIST})

get:
	@echo "Domain is ${DOMAIN}"
	@echo "Repo is ${REPO}"

init:
	@read -p "Please enter your domain:" DOMAIN; \
	read -p "Please enter your repo:" REPO; \
	echo -e "$${DOMAIN}\n$${REPO}" > ${FILE}

build:
	pip install --user --upgrade setuptools wheel
	python setup.py sdist bdist_wheel

push:
	pip install --user --upgrade awscli twine && \
	aws codeartifact login --tool twine --domain ${DOMAIN} --repository ${REPO} && \
	twine upload --repository codeartifact dist/*

clean:
	rm -Rf build dist library_name.egg-info

get_token:
	aws codeartifact get-authorization-token --domain ${DOMAIN} --query authorizationToken --output text
