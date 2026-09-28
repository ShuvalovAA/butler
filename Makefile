PROJECT_NAME := butler
MAIN_FILE_PATH := src.${PROJECT_NAME}.main
CONFIG_FILE_PATH := config.toml

lint:
	uv run ruff check . --fix

typecheck:
	uv run basedpyright .

run_tests:
	uv run pytest .

app_run:
	export CONFIG_FILE_PATH=${CONFIG_FILE_PATH} && uv run python -m ${MAIN_FILE_PATH}