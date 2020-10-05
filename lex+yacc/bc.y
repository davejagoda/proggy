/* compile like this:
yacc -d bc.y && flex bc.l && cc -o bc y.tab.c lex.yy.c -ll
*/

%{
#include <stdio.h>
int yylex();
void yyerror(char *s);
%}

%token ADD SUB MUL DIV NUM EOL

%%

calc:
 | calc addend EOL { printf("= %d\n", $2); }
 ;

addend: factor
 | addend ADD factor { $$ = $1 + $3; }
 | addend SUB factor { $$ = $1 - $3; }
 ;

factor: num
 | factor MUL num { $$ = $1 * $3; }
 | factor DIV num { $$ = $1 / $3; }
 ;

num: NUM
;

%%

int main(int argc, char **argv)
{
    yyparse();
}

void yyerror(char *s)
{
    fprintf(stderr, "error: %s\n", s);
}
