
all: p2 p4 p5 p6

p1:
	python3 src/p1.py

p2:
	python3 src/p2.py

p3:
	python3 src/p3.py

data:
	python3 src/p3_5.py

p4:
	python3 src/p4.py

p5:
	python3 src/p5.py

p6:
	python3 src/p6.py

clean:
	rm figs/*