#include <stdio.h>

int yyparse();

int main() {
    printf("Enter expression:\n");
    yyparse();
    return 0;
}

