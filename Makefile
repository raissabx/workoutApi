run:
	@uvicorn workout_api.main:app --reload --port 8000 --log-level trace

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d) 

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head


delete-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic downgrade


#make create-migrations d="init_db"