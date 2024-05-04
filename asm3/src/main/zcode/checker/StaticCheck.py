from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class Symbol:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ

class VariableSymbol(Symbol):
    def __init__(self, name, typ=None):
        super().__init__(name, typ)

class FunctionSymbol(Symbol):
    def __init__(self, name, typ=None, params=[], defined=False):
        super().__init__(name, typ)
        self.params = params
        self.defined = defined

class Scope:
    def __init__(self, is_loop=False, func_name=None):
        self.syms = []
        self.in_loop = is_loop
        self.func_name = func_name

    def find_var(self, name):
        for sym in self.syms[::-1]:
            if sym.name == name and type(sym) is VariableSymbol:
                return sym
        return None
    
    def find_func(self, name):
        for sym in self.syms[::-1]:
            if sym.name == name and type(sym) is FunctionSymbol:
                return sym
        return None
    
    def find_all(self, name):
        for sym in self.syms:
            if sym.name == name:
                return sym
        return None
    
    def append_sym(self, sym):
        self.syms.append(sym)

class ComponentCannotBeInfered(Type):
    def __str__(self):
        return "Type Cannot Be Inferred"


class StaticChecker(BaseVisitor, Utils):

    def visitProgram(self, ast, param):
        # Built-in functions
        param[0].append_sym(FunctionSymbol('readNumber', NumberType(), [], True))
        param[0].append_sym(FunctionSymbol('readBool', BoolType(), [], True))
        param[0].append_sym(FunctionSymbol('readString', StringType(), [], True))
        param[0].append_sym(FunctionSymbol('writeNumber', VoidType(), [NumberType()], True))
        param[0].append_sym(FunctionSymbol('writeBool', VoidType(), [BoolType()], True))
        param[0].append_sym(FunctionSymbol('writeString', VoidType(), [StringType()], True))
        for decl in ast.decl:
            self.visit(decl, param)
        for sym in param[0].syms:
            if type(sym) is FunctionSymbol and not sym.defined:
                raise NoDefinition(sym.name)
        main_sym = param[0].find_func('main')
        if not main_sym or len(main_sym.params) > 0 or type(main_sym.typ) is not VoidType:
            raise NoEntryPoint()

    def visitVarDecl(self, ast, param):
        name = ast.name.name
        if param[-1].find_var(name):
            raise Redeclared(Variable(), name)
        typ = None
        if ast.varType:
            typ = self.visit(ast.varType, param)
            if type(typ) is VoidType:
                raise TypeMismatchInStatement(ast)
            if ast.varInit:
                varInit = self.visit(ast.varInit, param)
                if not varInit and not typ:
                    raise TypeCannotBeInferred(ast)
                elif not varInit:
                    varInit = self.infer(ast.varInit.name, typ, param)
                elif type(varInit) is ComponentCannotBeInfered:
                    raise TypeCannotBeInferred(ast)
                if type(varInit) != type(typ):
                    raise TypeMismatchInStatement(ast)
                if type(typ) is ArrayType:
                    if typ.size != varInit.size:
                        raise TypeMismatchInStatement(ast)
                    if type(typ.eleType) != type(varInit.eleType):
                        raise TypeMismatchInStatement(ast)
        else:
            if ast.modifier == 'var':
                if not ast.varInit:
                    raise TypeMismatchInStatement(ast)
                else:
                    typ = self.visit(ast.varInit, param)
                    if not typ:
                        raise TypeCannotBeInferred(ast)
                    elif type(typ) is ComponentCannotBeInfered:
                        raise TypeCannotBeInferred(ast)
            elif ast.varInit:
                typ = self.visit(ast.varInit, param)
                if type(typ) is ComponentCannotBeInfered:
                    raise TypeCannotBeInferred(ast)
        sym = VariableSymbol(name, typ)
        param[-1].append_sym(sym)
        return sym

    def visitFuncDecl(self, ast, param):
        name = ast.name.name
        defined_function = param[-1].find_func(name)         
        if ast.body:
            func_param = []
            sym = None
            param.append(Scope(func_name=name))
            for p in ast.param:
                p_name = p.name.name
                if param[-1].find_var(p_name):
                    raise Redeclared(Parameter(), p_name)
                p_typ = self.visit(p.varType, param)
                param[-1].append_sym(VariableSymbol(p_name, p_typ))
                func_param.append(p_typ)
            if not defined_function:
                sym = FunctionSymbol(name, params=func_param, defined=True)
                param[0].append_sym(sym)
            else:
                if defined_function.defined or defined_function.params != func_param:
                    raise Redeclared(Function(), name) 
                sym = defined_function
                defined_function.defined = True
            param.append(Scope(func_name=name))
            if type(ast.body) is Block:
                for stmt in ast.body.stmt:
                    self.visit(stmt, param)
            else:
                self.visit(ast.body, param)
            param.pop()
            param.pop()
            return sym
        else:
            if defined_function:
                raise Redeclared(Function(), name)
            func_param = [self.visit(p.varType, param) for p in ast.param]
            sym = FunctionSymbol(name, params=func_param)
            param[0].append_sym(sym)
            return sym

    def visitBinaryOp(self, ast, param):
        e1t = self.visit(ast.left, param)
        e2t = self.visit(ast.right, param)
        op = ast.op
        if op in ['+', '-', '*', '/', '%']:
            if not e1t:
                e1t = self.infer(ast.left.name, NumberType(), param)
            if not e2t:
                e2t = self.infer(ast.right.name, NumberType(), param)
            if type(e1t) is NumberType and type(e2t) is NumberType:
                return NumberType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['and', 'or']:
            if not e1t:
                e1t = self.infer(ast.left.name, BoolType(), param)
            if not e2t:
                e2t = self.infer(ast.right.name, BoolType(), param)
            if type(e1t) is BoolType and type(e2t) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op == '...':
            if not e1t:
                e1t = self.infer(ast.left.name, StringType(), param)
            if not e2t:
                e2t = self.infer(ast.right.name, StringType(), param)
            if type(e1t) is StringType and type(e2t) is StringType:
                return StringType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['<', '<=', '>', '>=', '=', '!=']:
            if not e1t:
                e1t = self.infer(ast.left.name, NumberType(), param)
            if not e2t:
                e2t = self.infer(ast.right.name, NumberType(), param)
            if type(e1t) is NumberType and type(e2t) is NumberType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op == '==':
            if not e1t:
                e1t = self.infer(ast.left.name, StringType(), param)
            if not e2t:
                e2t = self.infer(ast.right.name, StringType(), param)
            if type(e1t) is StringType and type(e2t) is StringType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, param):
        et = self.visit(ast.operand, param)
        op = ast.op
        if op == '-':
            if not et:
                et = self.infer(ast.operand.name, NumberType(), param)
            if type(et) is NumberType:
                return NumberType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op == 'not':
            if not et:
                et = self.infer(ast.operand.name, BoolType(), param)
            if type(et) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, param):
        name = ast.name.name
        sym = param[0].find_func(name)
        if sym:
            if type(sym.typ) is VoidType:
                raise TypeMismatchInExpression(ast)
            if len(sym.params) != len(ast.args):
                raise TypeMismatchInExpression(ast)
            for arg, p_typ in zip(ast.args, sym.params):
                arg_typ = self.visit(arg, param)
                if not arg_typ and not p_typ:
                    return ComponentCannotBeInfered()
                elif not p_typ:
                    p_typ = self.infer(name, arg_typ, param)
                elif not arg_typ:
                    arg_typ = self.infer(arg.name, p_typ, param)
                elif type(self.visit(arg, param)) != type(p_typ):
                    raise TypeMismatchInExpression(ast)
            return sym.typ
        raise Undeclared(Function(), name)

    def visitId(self, ast, param):
        name = ast.name
        for env in param[::-1]:
            sym = env.find_var(name)
            if sym:
                return sym.typ
        raise Undeclared(Identifier(), name)

    def visitArrayCell(self, ast, param):
        arr_typ = self.visit(ast.arr, param)
        if not arr_typ:
            return ComponentCannotBeInfered()
        elif type(arr_typ) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        ret_size = arr_typ.size[len(ast.idx):]
        for idx in ast.idx:
            inx_typ = self.visit(idx, param)
            if not inx_typ:
                inx_typ = self.infer(idx.name, NumberType(), param)
            elif type(inx_typ) is ComponentCannotBeInfered:
                raise TypeCannotBeInferred(ast)
            elif type(inx_typ) is not NumberType:
                raise TypeMismatchInExpression(ast)
        return ArrayType(ret_size, arr_typ.eleType)

    def visitBlock(self, ast, param):
        param.append(Scope())
        for stmt in ast.stmt:
            self.visit(stmt, param)
        param.pop()

    def visitIf(self, ast, param):
        cond_typ = self.visit(ast.expr, param)
        if not cond_typ:
            cond_typ = self.infer(ast.expr.name, BoolType(), param)
        elif type(cond_typ) is ComponentCannotBeInfered:
            raise TypeCannotBeInferred(ast)
        elif type(cond_typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, param)
        for expr, stmt in ast.elifStmt:
            expr_typ = self.visit(expr, param)
            if not expr_typ:
                expr_typ = self.infer(expr.name, BoolType(), param)
            elif type(expr_typ) is ComponentCannotBeInfered:
                raise TypeCannotBeInferred(ast)
            elif type(expr_typ) is not BoolType:
                raise TypeMismatchInStatement(ast)
            self.visit(stmt, param)
        if ast.elseStmt:
            self.visit(ast.elseStmt, param)

    def visitFor(self, ast, param):
        name_typ = self.visit(ast.name, param)
        if not name_typ:
            name_typ = self.infer(ast.name.name, NumberType(), param)
        elif type(name_typ) is ComponentCannotBeInfered:
            raise TypeCannotBeInferred(ast)
        elif type(name_typ) is not NumberType:
            raise TypeMismatchInStatement(ast)
        cond_typ = self.visit(ast.condExpr, param)
        if not cond_typ:
            cond_typ = self.infer(ast.condExpr.name, BoolType(), param)
        elif type(cond_typ) is ComponentCannotBeInfered:
            raise TypeCannotBeInferred(ast)
        elif type(cond_typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        upd_typ = self.visit(ast.updExpr, param)
        if not upd_typ:
            upd_typ = self.infer(ast.updExpr.name, NumberType(), param)
        elif type(upd_typ) is ComponentCannotBeInfered:
            raise TypeCannotBeInferred(ast)
        elif type(upd_typ) is not NumberType:
            raise TypeMismatchInStatement(ast)
        param.append(Scope(is_loop=True))
        self.visit(ast.body, param)
        param.pop()

    def visitContinue(self, ast, param):
        for env in param[::-1]:
            if env.in_loop:
                return
        raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        for env in param[::-1]:
            if env.in_loop:
                return
        raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        func_typ = None
        func_name = None
        for env in param[::-1]:
            if env.func_name:
                func_typ = param[0].find_func(env.func_name).typ
                func_name = env.func_name
                break
        if ast.expr:
            ret_typ = self.visit(ast.expr, param)
            if not ret_typ and not func_typ:
                raise TypeCannotBeInferred(ast)
            elif not ret_typ:
                ret_typ = self.infer(ast.expr.name, func_typ, param)
            elif type(ret_typ) is ComponentCannotBeInfered:
                raise TypeCannotBeInferred(ast)
            elif not func_typ:
                func_typ = self.infer(func_name, ret_typ, param)
            elif type(ret_typ) != type(func_typ):
                raise TypeMismatchInStatement(ast)
        else:
            if not func_typ:
                func_typ = self.infer(func_name, VoidType(), param)
            if type(func_typ) is not VoidType:
                raise TypeMismatchInStatement(ast)

    def visitAssign(self, ast, param):
        lhs_typ = self.visit(ast.lhs, param)
        rhs_typ = self.visit(ast.rhs, param)
        if not lhs_typ and not rhs_typ:
            raise TypeCannotBeInferred(ast)
        elif type(lhs_typ) is VoidType:
            raise TypeMismatchInStatement(ast)
        elif not lhs_typ and type(rhs_typ) is not ComponentCannotBeInfered:
            lhs_typ = self.infer(ast.lhs.name, rhs_typ, param)
        elif type(lhs_typ) is ComponentCannotBeInfered:
            raise TypeCannotBeInferred(ast)
        elif not rhs_typ and type(lhs_typ) is not ComponentCannotBeInfered:
            rhs_typ = self.infer(ast.rhs.name, lhs_typ, param)
        elif type(rhs_typ) is ComponentCannotBeInfered:
            raise TypeCannotBeInferred(ast)
        elif type(lhs_typ) != type(rhs_typ):
            raise TypeMismatchInStatement(ast)
        elif type(lhs_typ) is ArrayType:
            if lhs_typ.size != rhs_typ.size:
                raise TypeMismatchInStatement(ast)
            if type(lhs_typ.eleType) != type(rhs_typ.eleType):
                raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, param):
        name = ast.name.name
        sym = param[0].find_func(name)
        if sym:
            if not sym.typ:
                sym.typ = VoidType()
            elif type(sym.typ) is not VoidType:
                raise TypeMismatchInStatement(ast)
            if len(sym.params) != len(ast.args):
                raise TypeMismatchInStatement(ast)
            for arg, p_typ in zip(ast.args, sym.params):
                arg_typ = self.visit(arg, param)
                if not arg_typ and not p_typ:
                    raise TypeCannotBeInferred(ast)
                elif not arg_typ:
                    arg_typ = self.infer(arg.name, p_typ, param)
                elif type(arg_typ) is ComponentCannotBeInfered:
                    raise TypeCannotBeInferred(ast)
                elif not p_typ:
                    p_typ = self.infer(name, arg_typ, param)
                elif type(arg_typ) != type(p_typ):
                    raise TypeMismatchInStatement(ast)
            return
        raise Undeclared(Function(), name)

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        size = [len(ast.value)]
        value_typ = None
        for value in ast.value:
            if self.visit(value, param):
                value_typ = self.visit(value, param)
                break
        if not value_typ:
            return ComponentCannotBeInfered()
        for value in ast.value:
            v_typ = self.visit(value, param)
            if not value_typ:
                value_typ = self.infer(value.name, value_typ, param)
            elif type(v_typ) is not type(value_typ):
                raise TypeMismatchInExpression(ast)
        if type(value_typ) is ArrayType:
            size += value_typ.size
            return ArrayType(size, value_typ.eleType)
        return ArrayType(size, value_typ)

    def visitNumberType(self, ast, param):
        return ast

    def visitBoolType(self, ast, param):
        return ast

    def visitStringType(self, ast, param):
        return ast

    def visitArrayType(self, ast, param):
        return ast


    def __init__(self, ast):
        self.ast = ast

    def check(self):
        dictionary = [Scope()]
        self.visit(self.ast, dictionary)
        return []
    
    @staticmethod
    def infer(name, typ, param):
        if type(name) is Id:
            name = name.name
        for env in param[::-1]:
            sym = env.find_all(name)
            if sym:
                sym.typ = typ
                return typ
