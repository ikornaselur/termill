mypy:
	@poetry run mypy src/termill/*

flake8:
	@poetry run flake8 src/termill/*

lint: mypy flake8

shell:
	@poetry run ipython

install_git_hooks:
	@ln -s /Users/axel/Projects/termill/.hooks/pre-push .git/hooks/pre-push
