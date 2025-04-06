%{
#include "parser.tab.h"
#include <stdlib.h>
#include <stdio.h>
%}

%%

[ \t]                ; // ignore spaces and tabs
\n                   return '\n';
"%%"                 { printf("Matched '%%' operator\n"); return TOK_PCTPCT; }
[0-9]+               { yylval = atoi(yytext); return NUMBER; }
"("                  return '(';
")"                  return ')';
"+"                  return '+';
"-"                  return '-';
"*"                  return '*';
.                    { printf("Unexpected character: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}
