// ID: 2111898
// Full name: Hoang Chi Nhan

grammar ZCode;

@lexer::header {
from lexererr import *
# 2111898 Hoang Chi Nhan
}

options {
	language=Python3;
}

//SYNTAX RULES
//Program
program: nnls decllist nnls EOF;

//Declaration
decllist: declprime | ; //nullable
declprime: decl nls declprime | decl;
decl: funcdecl | vardeclstmt;

//Function declaration
funcdecl: FUNC IDENTIFIER LP paramlist RP nnls (returnstmt | blockstmt | );
paramlist: paramprime | ; //nullable
paramprime: param COMMA paramprime | param;
param: primetype IDENTIFIER ((LS numlist RS)|);
numlist: NUMBERLIT COMMA numlist | NUMBERLIT; //not nullable
primetype: NUMBERTYPE | BOOLTYPE | STRINGTYPE;


//Statement
stmt: vardeclstmt 
	| assignstmt 
	| ifstmt 
	| forstmt 
	| breakstmt 
	| continuestmt 
	| returnstmt 
	| funccallstmt 
	| blockstmt;

//Variable declaration statement
vardeclstmt: (primetype | DYNAMICTYPE) IDENTIFIER ((ASSIGN expr)|)
	|	primetype IDENTIFIER LS numlist RS ((ASSIGN array)|)
	|	VARTYPE IDENTIFIER ASSIGN expr ;
array: LS arrayprime RS | LS RS; //nullable
arrayprime: arrayprime COMMA arrayelem | arrayelem;
arrayelem: expr | array;

//Assignment statement
assignstmt: (IDENTIFIER | elemexpr) ASSIGN expr;
exprlist: expr COMMA exprlist | expr; //not nullable

//If statement
ifstmt: IF LP expr RP nnls stmt nnls elifstmtlist nnls elsestmt;
elifstmtlist: elifstmt nnls elifstmtlist | ; //nullable
elifstmt: ELIF LP expr RP nnls stmt;
elsestmt: ELSE stmt |;

//For statement
forstmt: FOR IDENTIFIER UNTIL expr BY expr nnls stmt;

//Break statement
breakstmt: BREAK;

//Continue statement
continuestmt: CONTINUE;

//Return statement
returnstmt: RETURN expr | RETURN;

//Function call statement
funccallstmt: IDENTIFIER LP n_exprlist RP;
n_exprlist: exprprime | ; //nullable
exprprime: expr COMMA exprprime | expr;

//Block statement
blockstmt: BEGIN nls (stmtlist) END;
stmtlist: stmt nls stmtlist | ; //nullable


//Expression
funcexpr: IDENTIFIER LP n_exprlist RP;
expr: expr1 CONCAT expr1 | expr1;
expr1: expr2 (EQUAL|STRINGCOMPARE|NOTEQ|LT|MT|LOEQ|MOEQ) expr2 | expr2;
expr2: expr2 (AND|OR) expr3 | expr3;
expr3: expr3 (ADD|SUB) expr4 | expr4;
expr4: expr4 (MUL|DIV|MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | operand;
operand: IDENTIFIER
	| NUMBERLIT
	| BOOLLIT
	| STRINGLIT
	| funcexpr
	| elemexpr
	| LP expr RP;

elemexpr: (IDENTIFIER | funcexpr) LS indexop RS;
indexop: indexop COMMA expr | expr;


//Newline separator
nnls: NEWLINE nnls | ; //nullable newline list
nls: NEWLINE nls | NEWLINE; //not nullable newline list





//LEXICAL RULES
//Comment
COMMENT: '##' .*? (NEWLINE|EOF) -> skip;
WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs, newlines

//Type
NUMBERTYPE: 'number';
BOOLTYPE: 'bool';
STRINGTYPE: 'string';
VARTYPE: 'var';
DYNAMICTYPE: 'dynamic';

//Keyword
FUNC: 'func';
FOR: 'for'; 
UNTIL: 'until'; 
BY: 'by'; 
BREAK: 'break'; 
CONTINUE: 'continue';
IF: 'if'; 
ELSE: 'else'; 
ELIF: 'elif';
BEGIN: 'begin'; 
END: 'end';
RETURN: 'return';
NOT: 'not'; 
AND: 'and'; 
OR: 'or'; 

//Literal
BOOLLIT: 'true' | 'false';

NUMBERLIT: INTEGER DECIMAL? EXPONENT?;
fragment INTEGER: [0-9]+;
fragment DECIMAL: '.' (INTEGER)?;
fragment EXPONENT: ('e'|'E') ('+'|'-')? INTEGER;

STRINGLIT: DQ CHAR* DQ 
{
	self.text = self.text[1:-1].replace("'\"", '"').replace("\\b", "\b").replace("\\t", "\t").replace("\\n", "\n").replace("\\f", "\f").replace("\\r", "\r").replace("\\\\", "\\");};
fragment DQ: '"';
fragment CHAR: ~["\\] | ESCAPE | '\'"';
fragment ESCAPE: '\\' [btnfr'\\];
				
//Operator
ADD: '+'; 
SUB: '-'; 
MUL: '*'; 
DIV: '/'; 
MOD: '%';
EQUAL: '='; 
ASSIGN: '<-'; 
CONCAT: '...';
STRINGCOMPARE: '=='; 
NOTEQ: '!='; 
LT: '<'; 
MT: '>'; 
LOEQ: '<='; 
MOEQ: '>=';

//Separator
LP: '('; 
RP: ')'; 
LS: '['; 
RS: ']'; 
COMMA: ','; 
NEWLINE: '\n';
// NEWLINE: 'n' | 'n' WS NEWLINE { self.text = '\n' };

//Identifier
IDENTIFIER: [a-zA-Z_] [a-zA-Z_0-9]*;

//Error
UNCLOSE_STRING: DQ CHAR* EOF? {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: DQ CHAR* ( '\\' ~[bnfrt'\\] ) {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};

