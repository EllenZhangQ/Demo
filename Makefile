#
# A simple makefile for compiling a c++ project
#
#.DEFAULT_GOAL := HelloCplusCplus.cpp

all: clean hello

hello: HelloCplusCplus.o 
	g++ -o hello HelloCplusCplus.o

HelloCplusCplus.o: HelloCplusCplus.cpp
	g++ -c HelloCplusCplus.cpp

clean: 
	rm -rf ./*.o

