include ../../../build_tools/poetry.mk

mypy_logging_framework:
	MYPYPATH=src/logging_framework env/bin/mypy src/logging_framework

mypy_parking_lot:
	MYPYPATH=src/parking_lot env/bin/mypy src/parking_lot

mypy_pubsub:
	MYPYPATH=src/pubsub env/bin/mypy src/pubsub

mypy_pubsub_asyncio:
	MYPYPATH=src/pubsub_asyncio env/bin/mypy src/pubsub_asyncio

mypy: mypy_logging_framework mypy_parking_lot mypy_pubsub mypy_pubsub_asyncio
	echo "Mypy Success"
