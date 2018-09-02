
lint:
	@pycodestyle .

format:
	@autopep8 --in-place --recursive --aggressive .

deps:
	@pip install -r requirements.txt

run:
	@python3 main.py

install:
	@sudo python3 setup.py install
	@sudo python3 setup.py install_data
	make clean

clean:
	sudo python3 setup.py clean
