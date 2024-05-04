# Generated from c:/PROJECTS/PPLAsm/asm2_init/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decllist.
    def enterDecllist(self, ctx:ZCodeParser.DecllistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decllist.
    def exitDecllist(self, ctx:ZCodeParser.DecllistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declprime.
    def enterDeclprime(self, ctx:ZCodeParser.DeclprimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declprime.
    def exitDeclprime(self, ctx:ZCodeParser.DeclprimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl.
    def enterDecl(self, ctx:ZCodeParser.DeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl.
    def exitDecl(self, ctx:ZCodeParser.DeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcdecl.
    def enterFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcdecl.
    def exitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramlist.
    def enterParamlist(self, ctx:ZCodeParser.ParamlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramlist.
    def exitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramprime.
    def enterParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramprime.
    def exitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param.
    def enterParam(self, ctx:ZCodeParser.ParamContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param.
    def exitParam(self, ctx:ZCodeParser.ParamContext):
        pass


    # Enter a parse tree produced by ZCodeParser#numlist.
    def enterNumlist(self, ctx:ZCodeParser.NumlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#numlist.
    def exitNumlist(self, ctx:ZCodeParser.NumlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#primetype.
    def enterPrimetype(self, ctx:ZCodeParser.PrimetypeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#primetype.
    def exitPrimetype(self, ctx:ZCodeParser.PrimetypeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt.
    def enterStmt(self, ctx:ZCodeParser.StmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt.
    def exitStmt(self, ctx:ZCodeParser.StmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vardeclstmt.
    def enterVardeclstmt(self, ctx:ZCodeParser.VardeclstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vardeclstmt.
    def exitVardeclstmt(self, ctx:ZCodeParser.VardeclstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array.
    def enterArray(self, ctx:ZCodeParser.ArrayContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array.
    def exitArray(self, ctx:ZCodeParser.ArrayContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayprime.
    def enterArrayprime(self, ctx:ZCodeParser.ArrayprimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayprime.
    def exitArrayprime(self, ctx:ZCodeParser.ArrayprimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayelem.
    def enterArrayelem(self, ctx:ZCodeParser.ArrayelemContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayelem.
    def exitArrayelem(self, ctx:ZCodeParser.ArrayelemContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignstmt.
    def enterAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignstmt.
    def exitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exprlist.
    def enterExprlist(self, ctx:ZCodeParser.ExprlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#exprlist.
    def exitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ifstmt.
    def enterIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ifstmt.
    def exitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elifstmtlist.
    def enterElifstmtlist(self, ctx:ZCodeParser.ElifstmtlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elifstmtlist.
    def exitElifstmtlist(self, ctx:ZCodeParser.ElifstmtlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elifstmt.
    def enterElifstmt(self, ctx:ZCodeParser.ElifstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elifstmt.
    def exitElifstmt(self, ctx:ZCodeParser.ElifstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elsestmt.
    def enterElsestmt(self, ctx:ZCodeParser.ElsestmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elsestmt.
    def exitElsestmt(self, ctx:ZCodeParser.ElsestmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#forstmt.
    def enterForstmt(self, ctx:ZCodeParser.ForstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#forstmt.
    def exitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#breakstmt.
    def enterBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#breakstmt.
    def exitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continuestmt.
    def enterContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continuestmt.
    def exitContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#returnstmt.
    def enterReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#returnstmt.
    def exitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funccallstmt.
    def enterFunccallstmt(self, ctx:ZCodeParser.FunccallstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funccallstmt.
    def exitFunccallstmt(self, ctx:ZCodeParser.FunccallstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#n_exprlist.
    def enterN_exprlist(self, ctx:ZCodeParser.N_exprlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#n_exprlist.
    def exitN_exprlist(self, ctx:ZCodeParser.N_exprlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exprprime.
    def enterExprprime(self, ctx:ZCodeParser.ExprprimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#exprprime.
    def exitExprprime(self, ctx:ZCodeParser.ExprprimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#blockstmt.
    def enterBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#blockstmt.
    def exitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmtlist.
    def enterStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmtlist.
    def exitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcexpr.
    def enterFuncexpr(self, ctx:ZCodeParser.FuncexprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcexpr.
    def exitFuncexpr(self, ctx:ZCodeParser.FuncexprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr.
    def enterExpr(self, ctx:ZCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr.
    def exitExpr(self, ctx:ZCodeParser.ExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr1.
    def enterExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr1.
    def exitExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr2.
    def enterExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr2.
    def exitExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr3.
    def enterExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr3.
    def exitExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr4.
    def enterExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr4.
    def exitExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr5.
    def enterExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr5.
    def exitExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr6.
    def enterExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr6.
    def exitExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass


    # Enter a parse tree produced by ZCodeParser#operand.
    def enterOperand(self, ctx:ZCodeParser.OperandContext):
        pass

    # Exit a parse tree produced by ZCodeParser#operand.
    def exitOperand(self, ctx:ZCodeParser.OperandContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elemexpr.
    def enterElemexpr(self, ctx:ZCodeParser.ElemexprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elemexpr.
    def exitElemexpr(self, ctx:ZCodeParser.ElemexprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#indexop.
    def enterIndexop(self, ctx:ZCodeParser.IndexopContext):
        pass

    # Exit a parse tree produced by ZCodeParser#indexop.
    def exitIndexop(self, ctx:ZCodeParser.IndexopContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nnls.
    def enterNnls(self, ctx:ZCodeParser.NnlsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nnls.
    def exitNnls(self, ctx:ZCodeParser.NnlsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nls.
    def enterNls(self, ctx:ZCodeParser.NlsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nls.
    def exitNls(self, ctx:ZCodeParser.NlsContext):
        pass



del ZCodeParser