.PHONY: run seed smoke openapi lint test

run:
\tuvicorn src.api.main:app --reload --host 0.0.0.0 --port 3001

seed:
\tpython -m src.api.run_seed

smoke:
\tpython -m src.api.db_smoke_test

openapi:
\tpython -m src.api.generate_openapi

lint:
\tflake8 src

test:
\tpytest -q
