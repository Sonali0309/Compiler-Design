all:
	bison -d parser.y
	flex -o lexer.c lexer.l
	gcc -o mycompiler parser.tab.c lexer.c main.c -lfl

clean:
	rm -f parser.tab.c parser.tab.h lexer.c mycompiler

