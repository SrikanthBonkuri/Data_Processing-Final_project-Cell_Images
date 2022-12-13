
all: q4 q5 q6

q1:
	python3 src/p11.py

q2:
	python3 src/p2.py

q3:
	python3 src/p3.py

data:
	python3 src/p3_5.py

q4:
	python3 src/p4.py

q5:
	python3 src/p5.py

q6:
	python3 src/p6.py

clean:
	rm figs/*