/* compile like this:
flex wc.l && cc lex.yy.c -o wc -ll
*/

%{
int words = 0;
int lines = 0;
int chars = 0;
%}

%%

[^ \t\n]+ { words++; chars += strlen(yytext); }
\n        { lines++; chars++; }
.         { chars++; }

%%

int main(int argc, char **argv)
{
    yylex();
    printf("%d %d %d\n", lines, words, chars);
}
