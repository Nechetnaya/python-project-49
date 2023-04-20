install: # установить зависимости
	poetry install

brain-games: #запуск
	poetry run brain-games

brain-even: #запуск игры even
	poetry run brain-even

brain-calc: #запуск игры calc
	poetry run brain-calc

build: #собрать пакет
	poetry build

publish: #публикация (не добавлять пакет в каталог PyPI)
	poetry publish --dry-run

package-install: #Для установки пакета из операционной системы
	python3 -m pip install --user dist/*.whl

reinstall: #Для переустановки пакета из операционной системы
	python3 -m pip install --force-reinstall dist/*.whl

lint: #запуск линтера
	poetry run flake8 brain_games
