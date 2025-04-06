%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char* s);
%}

%token NUMBER
%token TOK_PCTPCT

%left '+' '-'
%left '*' TOK_PCTPCT

%start input

%%

input:
      expr '\n'        { printf("Result = %d\n", $1); }
    | input expr '\n'  { printf("Result = %d\n", $2); }
    ;

expr:
      expr '+' expr      { $$ = $1 + $3; }
    | expr '-' expr      { $$ = $1 - $3; }
    | expr '*' expr      { $$ = $1 * $3; }
    | expr TOK_PCTPCT expr {
          printf("Parsed '%%' operator: %d %% %d\n", $1, $3);
          $$ = $1 * $1 + $3 * $3 + $1 + $3 + 1;
      }
    | '(' expr ')'       { $$ = $2; }
    | NUMBER             { $$ = $1; }
    ;

%%
void yyerror(const char* s) {
    fprintf(stderr, "Error: %s\n", s);
}
