#
# A simple makefile for compiling a c++ project
#
#.DEFAULT_GOAL := HelloCplusCplus.cpp

all: clean hello artifact

hello: HelloCplusCplus.o 
	g++ -o hello.exe HelloCplusCplus.o

HelloCplusCplus.o: HelloCplusCplus.cpp
	g++ -c HelloCplusCplus.cpp

artifact:
	mkdir artifact
	mv HelloCplusCplus.o ./artifact
	mv hello.exe ./artifact
clean: 
	rm -rf ./*.o

