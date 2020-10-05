/* compile step in bc.y */

%{
#include "y.tab.h"
%}

%%

"+"    { return ADD; }
"-"    { return SUB; }
"*"    { return MUL; }
"/"    { return DIV; }
[0-9]+ { yylval = atoi(yytext); return NUM; }
\n     { return EOL; }
[ \t]  { }
.      { printf("Unexpected character %c ", *yytext); }

%%
