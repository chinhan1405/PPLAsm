# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decllist.
    def visitDecllist(self, ctx:ZCodeParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declprime.
    def visitDeclprime(self, ctx:ZCodeParser.DeclprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramlist.
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramprime.
    def visitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numlist.
    def visitNumlist(self, ctx:ZCodeParser.NumlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primetype.
    def visitPrimetype(self, ctx:ZCodeParser.PrimetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardeclstmt.
    def visitVardeclstmt(self, ctx:ZCodeParser.VardeclstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array.
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayprime.
    def visitArrayprime(self, ctx:ZCodeParser.ArrayprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayelem.
    def visitArrayelem(self, ctx:ZCodeParser.ArrayelemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignstmt.
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprlist.
    def visitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifstmt.
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifstmtlist.
    def visitElifstmtlist(self, ctx:ZCodeParser.ElifstmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifstmt.
    def visitElifstmt(self, ctx:ZCodeParser.ElifstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elsestmt.
    def visitElsestmt(self, ctx:ZCodeParser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forstmt.
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakstmt.
    def visitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continuestmt.
    def visitContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnstmt.
    def visitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funccallstmt.
    def visitFunccallstmt(self, ctx:ZCodeParser.FunccallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#n_exprlist.
    def visitN_exprlist(self, ctx:ZCodeParser.N_exprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprprime.
    def visitExprprime(self, ctx:ZCodeParser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockstmt.
    def visitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtlist.
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcexpr.
    def visitFuncexpr(self, ctx:ZCodeParser.FuncexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elemexpr.
    def visitElemexpr(self, ctx:ZCodeParser.ElemexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexop.
    def visitIndexop(self, ctx:ZCodeParser.IndexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nnls.
    def visitNnls(self, ctx:ZCodeParser.NnlsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nls.
    def visitNls(self, ctx:ZCodeParser.NlsContext):
        return self.visitChildren(ctx)



del ZCodeParser