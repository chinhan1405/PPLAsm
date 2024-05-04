from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    # program: nnls decllist nnls EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))


    # decllist: declprime | ;
    def visitDecllist(self, ctx:ZCodeParser.DecllistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.declprime())


    # declprime: decl nls declprime | decl;
    def visitDeclprime(self, ctx:ZCodeParser.DeclprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        else:
            return [self.visit(ctx.decl())] + self.visit(ctx.declprime())
    

    # decl: funcdecl | vardeclstmt;
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        if ctx.funcdecl():
            return self.visit(ctx.funcdecl())
        else:
            return self.visit(ctx.vardeclstmt())


    # funcdecl: FUNC IDENTIFIER LP paramlist RP nnls (returnstmt | blockstmt | );
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        if ctx.returnstmt():
            return FuncDecl(Id(ctx.IDENTIFIER().getText()),
                            self.visit(ctx.paramlist()),
                            self.visit(ctx.returnstmt()))
        elif ctx.blockstmt():
            return FuncDecl(Id(ctx.IDENTIFIER().getText()),
                            self.visit(ctx.paramlist()),
                            self.visit(ctx.blockstmt()))
        else:
            return FuncDecl(Id(ctx.IDENTIFIER().getText()),
                            self.visit(ctx.paramlist()))


    # paramlist: paramprime | ;
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.paramprime())


    # paramprime: param COMMA paramprime | param;
    def visitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        else:
            return [self.visit(ctx.param())] + self.visit(ctx.paramprime())


    # param: primetype IDENTIFIER ((LS numlist RS)|);
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        if not(ctx.LS()):
            return VarDecl(Id(ctx.IDENTIFIER().getText()),
                           self.visit(ctx.primetype()),
                           None, None)
        else:
            return VarDecl(Id(ctx.IDENTIFIER().getText()),
                           ArrayType(self.visit(ctx.numlist()), self.visit(ctx.primetype())),
                           None, None)


    # numlist: NUMBERLIT COMMA numlist | NUMBERLIT;
    def visitNumlist(self, ctx:ZCodeParser.NumlistContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUMBERLIT().getText())]
        else:
            return [float(ctx.NUMBERLIT().getText())] + self.visit(ctx.numlist())


    # primetype: NUMBERTYPE | BOOLTYPE | STRINGTYPE;
    def visitPrimetype(self, ctx:ZCodeParser.PrimetypeContext):
        if ctx.NUMBERTYPE():
            return NumberType()
        elif ctx.BOOLTYPE():
            return BoolType()
        else:
            return StringType()


    # stmt: vardeclstmt 
	# | assignstmt 
	# | ifstmt 
	# | forstmt 
	# | breakstmt 
	# | continuestmt 
	# | returnstmt 
	# | funccallstmt 
	# | blockstmt;
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # vardeclstmt: (primetype | DYNAMICTYPE) IDENTIFIER ((ASSIGN expr)|)
	# |	primetype IDENTIFIER LS numlist RS ((ASSIGN array)|)
	# |	VARTYPE IDENTIFIER ASSIGN expr ;
    def visitVardeclstmt(self, ctx:ZCodeParser.VardeclstmtContext):
        id = Id(ctx.IDENTIFIER().getText())
        vartype = None
        modifier = None
        init = None
        if ctx.expr():
            init = self.visit(ctx.expr())
        elif ctx.array():
            init = self.visit(ctx.array())
        if ctx.DYNAMICTYPE():
            modifier = ctx.DYNAMICTYPE().getText()
        elif ctx.VARTYPE():
            modifier = ctx.VARTYPE().getText()
        elif ctx.primetype():
            if ctx.LS():
                vartype = ArrayType(self.visit(ctx.numlist()), self.visit(ctx.primetype()))
            else:
                vartype = self.visit(ctx.primetype())
        return VarDecl(id, vartype, modifier, init)


    # array: LS arrayprime RS | LS RS;
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        if ctx.arrayprime():
            return ArrayLiteral(self.visit(ctx.arrayprime()))
        else:
            return ArrayLiteral([])


    # arrayprime: arrayprime COMMA arrayelem | arrayelem;
    def visitArrayprime(self, ctx:ZCodeParser.ArrayprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.arrayelem())]
        else:
            return self.visit(ctx.arrayprime()) + [self.visit(ctx.arrayelem())]


    # arrayelem: expr | array;
    def visitArrayelem(self, ctx:ZCodeParser.ArrayelemContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        else:
            return self.visit(ctx.array())


    # assignstmt: (IDENTIFIER | elemexpr) ASSIGN expr;
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        if ctx.IDENTIFIER():
            left = Id(ctx.IDENTIFIER().getText())
            right = self.visit(ctx.expr())
            return Assign(left, right)
        else:
            left = self.visit(ctx.elemexpr())
            right = self.visit(ctx.expr())
            return Assign(left, right)


    # exprlist: expr COMMA exprlist | expr;
    def visitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())


    # ifstmt: IF LP expr RP nnls stmt nnls elifstmtlist nnls elsestmt;
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        return If(self.visit(ctx.expr()),
                  self.visit(ctx.stmt()),
                  self.visit(ctx.elifstmtlist()),
                  self.visit(ctx.elsestmt()))


    # elifstmtlist: elifstmt nnls elifstmtlist | ;
    def visitElifstmtlist(self, ctx:ZCodeParser.ElifstmtlistContext):
        if ctx.elifstmt():
            return [self.visit(ctx.elifstmt())] + self.visit(ctx.elifstmtlist())
        else:
            return []


    # elifstmt: ELIF LP expr RP nnls stmt;
    def visitElifstmt(self, ctx:ZCodeParser.ElifstmtContext):
        return (self.visit(ctx.expr()), self.visit(ctx.stmt()))


    # elsestmt: ELSE stmt |;
    def visitElsestmt(self, ctx:ZCodeParser.ElsestmtContext):
        if ctx.ELSE():
            return self.visit(ctx.stmt())
        else:
            return None


    # forstmt: FOR IDENTIFIER UNTIL expr BY expr nnls stmt;
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.stmt()))


    # breakstmt: BREAK;
    def visitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        return Break()


    # continuestmt: CONTINUE;
    def visitContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        return Continue()


    # returnstmt: RETURN expr | RETURN;
    def visitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return()


    # funccallstmt: IDENTIFIER LP n_exprlist RP;
    def visitFunccallstmt(self, ctx:ZCodeParser.FunccallstmtContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.n_exprlist()))


    # n_exprlist: exprprime | ;
    def visitN_exprlist(self, ctx:ZCodeParser.N_exprlistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.exprprime())


    # exprprime: expr COMMA exprprime | expr;
    def visitExprprime(self, ctx:ZCodeParser.ExprprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())


    # blockstmt: BEGIN nls (stmtlist) END;
    def visitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        return Block(self.visit(ctx.stmtlist()))


    # stmtlist: stmt nls stmtlist | ;
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())


    # funcexpr: IDENTIFIER LP n_exprlist RP;
    def visitFuncexpr(self, ctx:ZCodeParser.FuncexprContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.n_exprlist()))
    

    # expr: expr1 CONCAT expr1 | expr1;
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        else:
            left = self.visit(ctx.expr1(0))
            right = self.visit(ctx.expr1(1))
            return BinaryOp(ctx.CONCAT().getText(), left, right)


    # expr1: expr2 (EQUAL|STRINGCOMPARE|NOTEQ|LT|MT|LOEQ|MOEQ) expr2 | expr2;
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        else:
            left = self.visit(ctx.expr2(0))
            right = self.visit(ctx.expr2(1))
            return BinaryOp(ctx.getChild(1).getText(), left, right)


    # expr2: expr2 (AND|OR) expr3 | expr3;
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        else:
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinaryOp(ctx.getChild(1).getText(), left, right)


    # expr3: expr3 (ADD|SUB) expr4 | expr4;
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        else:
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            return BinaryOp(ctx.getChild(1).getText(), left, right)


    # expr4: expr4 (MUL|DIV|MOD) expr5 | expr5;
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        else:
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinaryOp(ctx.getChild(1).getText(), left, right)


    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr6())


    # expr6: SUB expr6 | operand;
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.SUB():
            return UnaryOp(ctx.SUB().getText(), self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.operand())


    # operand: IDENTIFIER
	# | NUMBERLIT
	# | BOOLLIT
	# | STRINGLIT
	# | funcexpr
	# | elemexpr
	# | LP expr RP;
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.NUMBERLIT():
            return NumberLiteral(float(ctx.NUMBERLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.funcexpr():
            return self.visit(ctx.funcexpr())
        elif ctx.elemexpr():
            return self.visit(ctx.elemexpr())
        else:
            return self.visit(ctx.expr())


    # elemexpr: (IDENTIFIER | funcexpr) LS indexop RS;
    def visitElemexpr(self, ctx:ZCodeParser.ElemexprContext):
        if ctx.IDENTIFIER():
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.indexop()))
        else:
            return ArrayCell(self.visit(ctx.funcexpr()), self.visit(ctx.indexop()))


    # indexop: indexop COMMA expr | expr;
    def visitIndexop(self, ctx:ZCodeParser.IndexopContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else:
            return self.visit(ctx.indexop()) + [self.visit(ctx.expr())]


    # nnls: NEWLINE nnls | ;
    def visitNnls(self, ctx:ZCodeParser.NnlsContext):
        return None


    # nls: NEWLINE nls | NEWLINE;
    def visitNls(self, ctx:ZCodeParser.NlsContext):
        return None
    