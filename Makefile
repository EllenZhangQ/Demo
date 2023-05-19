#
# A simple makefile for compiling a c++ project
#

all: clean hello package

hello: HelloCplusCplus.o 
	g++ -o hello.exe HelloCplusCplus.o

HelloCplusCplus.o: HelloCplusCplus.cpp
	g++ -c HelloCplusCplus.cpp

package:
	chmod 755 ./artifact/hello.exe
	mv hello.exe ./artifact
	mv HelloCplusCplus.o ./artifact

clean: 
	rm -rf ./*.o

