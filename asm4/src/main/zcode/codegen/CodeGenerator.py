from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class MType:
    def __init__(self, partype: list[Type], rettype: Type):
        self.partype = partype
        self.rettype = rettype


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value: int):
        self.value = value


class CName(Val):
    def __init__(self, value: str):
        self.value = value


class Symbol:
    def __init__(self, name: str, mtype: MType, value: Val = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"


class CodeGenerator:
    def __init__(self):
        self.libName = "ZCodeClass"

    def init(self):
        return [
            Symbol("writeNumber", MType([NumberType()], VoidType()), CName(self.libName)),
            Symbol("writeString", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("readNumber", MType([], NumberType()), CName(self.libName)),
            Symbol("readString", MType([], StringType()), CName(self.libName)),
            Symbol("readBool", MType([], BoolType()), CName(self.libName))
        ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path, self.libName)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame: Frame, sym: list[Symbol]):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame: Frame, sym: list[Symbol], isLeft: bool = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft



class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env: list[Symbol], path: str, libName: str):
        self.astTree = astTree
        self.env = [env]
        self.path = path
        self.emit = Emitter(path)
        self.libName = libName
        self.global_var = {}
        self.global_func = {}
        self.clinit = {}

    def findSymbol(self, obj: Id|CallExpr|CallStmt|Frame, env: list[list[Symbol]]) -> Symbol:
        name: str = None
        if type(obj) is Id or type(obj) is Frame:
            name: str = obj.name
        elif type(obj) is CallExpr or type(obj) is CallStmt:
            name: str = obj.name.name
        for e in env[::-1]:
            for sym in e:
                if sym.name == name:
                    return sym
    
    def infer(self, obj: Id|CallExpr|CallStmt|Frame, typ: Type | MType, env: list[list[Symbol]]):
        name = None
        if type(obj) is Id or type(obj) is Frame:
            name = obj.name
        elif type(obj) is CallExpr or type(obj) is CallStmt:
            name = obj.name.name
        for e in env[::-1]:
            for sym in e:
                if sym.name == name:
                    if type(sym.mtype) is MType:
                        sym.mtype.rettype = typ
                    else:
                        sym.mtype = typ
                        if e is env[0] and self.global_var[name] is None:
                            self.global_var[name] = self.emit.emitATTRIBUTE(name, typ, True, None)
                    return

    def visitProgram(self, ast, param):
        self.emit.printout(self.emit.emitPROLOG(self.libName, ""))
        global_sub = SubBody(None, self.env)
        for decl in ast.decl:
            self.visit(decl, global_sub)

        for code in self.global_var.values():
            if code:
                self.emit.printout(code)

        # IO functions
        self.emit.printout('''
.method public static writeNumber(F)V
  .limit stack 2
  .limit locals 1
  .line 5
  0: getstatic java/lang/System/out Ljava/io/PrintStream;
  3: fload_0
  4: invokevirtual java/io/PrintStream/print(F)V
  .line 6
  7: return
.end method

.method public static writeString(Ljava/lang/String;)V
  .limit stack 2
  .limit locals 1
  .line 9
  0: getstatic java/lang/System/out Ljava/io/PrintStream;
  3: aload_0
  4: invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
  .line 10
  7: return
.end method

.method public static writeBool(Z)V
  .limit stack 2
  .limit locals 1
  .line 13
  0: getstatic java/lang/System/out Ljava/io/PrintStream;
  3: iload_0
  4: invokevirtual java/io/PrintStream/print(Z)V
  .line 14
  7: return
.end method

.method public static readNumber()F
  .limit stack 3
  .limit locals 2
  .line 17
  0: new java/util/Scanner
  3: dup
  4: getstatic java/lang/System/in Ljava/io/InputStream;
  7: invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
  10: astore_0
  .line 18
  11: aload_0
  12: invokevirtual java/util/Scanner/nextFloat()F
  15: fstore_1
  .line 19
  16: fload_1
  17: freturn
.end method

.method public static readString()Ljava/lang/String;
  .limit stack 3
  .limit locals 2
  .line 23
  0: new java/util/Scanner
  3: dup
  4: getstatic java/lang/System/in Ljava/io/InputStream;
  7: invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
  10: astore_0
  .line 24
  11: aload_0
  12: invokevirtual java/util/Scanner/nextLine()Ljava/lang/String;
  15: astore_1
  .line 25
  16: aload_1
  17: areturn
.end method

.method public static readBool()Z
  .limit stack 3
  .limit locals 2
  .line 29
  0: new java/util/Scanner
  3: dup
  4: getstatic java/lang/System/in Ljava/io/InputStream;
  7: invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
  10: astore_0
  .line 30
  11: aload_0
  12: invokevirtual java/util/Scanner/nextBoolean()Z
  15: istore_1
  .line 31
  16: iload_1
  17: ireturn
.end method
                           
.method public static concatString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
  .limit stack 2
  .limit locals 3
  0: new java/lang/StringBuilder
  3: dup
  4: invokespecial java/lang/StringBuilder/<init>()V
  7: astore_2
  8: aload_2
  9: aload_0
  10: invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
  13: aload_1
  14: invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
  17: pop
  18: aload_2
  19: invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
  22: areturn
.end method
                           
''')

        for code in self.global_func.values():
            self.emit.printout(code)

        if self.clinit:
            frame = Frame(None, VoidType())
            self.emit.printout('\n.method static <clinit>()V\n')
            for name, ctx in self.clinit.items():
                code, typ = self.visit(ctx, Access(frame, self.env, False))
                self.emit.printout(code)
                self.emit.printout(self.emit.emitPUTSTATIC(self.libName + '/' + name, typ, frame))
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            self.emit.printout(self.emit.emitENDMETHOD(frame))

        self.emit.emitEPILOG()

    def visitVarDecl(self, ast, param):
        if param.frame:
            new_index = param.frame.getNewIndex()
            name = ast.name.name
            typ = None
            code = ''
            if ast.varType:
                typ = ast.varType
            if ast.varInit:
                if typ:
                    self.infer(ast.varInit, typ, param.sym)
                code, typ = self.visit(ast.varInit, Access(param.frame, param.sym, False))
                code += self.emit.emitWRITEVAR(name, typ, new_index, param.frame)
            param.sym[-1].append(Symbol(name, typ, Index(new_index)))
            return code
        else:
            code = ''
            name = ast.name.name
            typ = None
            if ast.varType:
                typ = ast.varType
            if ast.varInit:
                if typ:
                    self.infer(ast.varInit, typ, param.sym)
                frame = Frame(name, VoidType())
                _, typ = self.visit(ast.varInit, Access(frame, param.sym, False))
                self.global_var[name] = self.emit.emitATTRIBUTE(name, typ, False, None)
                self.clinit[name] = ast.varInit
            else:
                self.global_var[name] = None
            param.sym[0].append(Symbol(name, typ, CName(self.libName)))
            if code:
                self.global_func[name] = code

    def visitFuncDecl(self, ast, param):
        name = ast.name.name
        param = SubBody(Frame(name, None), param.sym)
        param.frame.enterScope(True)
        param.sym.append([])
        code = ''
        func_type = None
        if name == 'main':
            param.frame.getNewIndex()
            func_type = MType([ArrayType([1], StringType())], VoidType())
        else:
            for p in ast.param:
                self.visit(p, param)
            pars = [Symbol(p.name.name, p.varType, Index(param.frame.getNewIndex())) for p in ast.param]
            param.sym[-1] += pars
            func_type = MType([p.mtype for p in pars], VoidType())
        findSym = self.findSymbol(param.frame, param.sym)
        if not findSym:
            param.sym[0].append(Symbol(name, func_type, CName(self.libName)))
        if ast.body:
            code += self.visit(ast.body, param)
            inferred_type = self.findSymbol(param.frame, param.sym).mtype
            if type(inferred_type.rettype) is VoidType:
                code += self.emit.emitRETURN(VoidType(), param.frame)
            code += self.emit.emitENDMETHOD(param.frame)
            code = self.emit.emitMETHOD(name, inferred_type, True, param.frame) + code
            self.global_func[name] = code
        param.sym.pop()
        param.frame.exitScope()

    def visitNumberType(self, ast, param):
        return ast

    def visitBoolType(self, ast, param):
        return ast

    def visitStringType(self, ast, param):
        return ast

    def visitArrayType(self, ast, param):
        return ast

    def visitBinaryOp(self, ast, param):
        op = ast.op
        if op in ['+', '-', '*', '/', '%', '>', '>=', '<', '<=', '=', '!=']:
            self.infer(ast.left, NumberType(), param.sym)
            self.infer(ast.right, NumberType(), param.sym)
        elif op in ['and', 'or']:
            self.infer(ast.left, BoolType(), param.sym)
            self.infer(ast.right, BoolType(), param.sym)
        else:
            self.infer(ast.left, StringType(), param.sym)
            self.infer(ast.right, StringType(), param.sym)
        left_code, left_type = self.visit(ast.left, Access(param.frame, param.sym, False))
        right_code, right_type = self.visit(ast.right, Access(param.frame, param.sym, False))
        if op in ['+', '-']:
            code = left_code + right_code + self.emit.emitADDOP(ast.op, left_type, param.frame)
        elif op in ['*', '/']:
            code = left_code + right_code + self.emit.emitMULOP(ast.op, left_type, param.frame)
        elif op == '%':
            code = left_code + right_code + self.emit.emitMOD(param.frame)
        elif op == 'and':
            code = left_code + right_code + self.emit.emitANDOP(param.frame)
        elif op == 'or':
            code = left_code + right_code + self.emit.emitOROP(param.frame)
        elif op in ['>', '>=', '<', '<=', '=', '!=', '==']:
            code = left_code + right_code + self.emit.emitREOP(ast.op, left_type, param.frame)
        elif op == '...':
            code = left_code + right_code
            code += self.emit.emitINVOKESTATIC(self.libName + '/concatString', MType([StringType(), StringType()], StringType()), param.frame)
        return code, left_type

    def visitUnaryOp(self, ast, param):
        code, typ = self.visit(ast.operand, Access(param.frame, param.sym, False))
        op = ast.op
        if op == '-':
            self.infer(ast.operand, NumberType(), param.sym)
            code += self.emit.emitNEGOP(typ, param.frame)
        elif op == 'not':
            self.infer(ast.operand, BoolType(), param.sym)
            code += self.emit.emitNOT(typ, param.frame)
        return code, typ

    def visitCallExpr(self, ast, param):
        code = ''
        method = self.findSymbol(ast, param.sym)
        for i, arg in enumerate(ast.args):
            self.infer(arg, method.mtype.partype[i], param.sym)
            code += self.visit(arg, Access(param.frame, param.sym, False))[0]
        name = method.value.value + '/' + method.name
        code += self.emit.emitINVOKESTATIC(name, method.mtype, param.frame)  
        return code, method.mtype.rettype

    def visitId(self, ast, param):
        id = self.findSymbol(ast, param.sym)
        typ = id.mtype
        code = None
        if param.isLeft:
            if type(id.value) is Index:
                code = self.emit.emitWRITEVAR(ast.name, typ, id.value.value, param.frame)
            else:
                code = self.emit.emitPUTSTATIC(id.value.value + '/' + ast.name, typ, param.frame)
        else:
            if type(id.value) is Index:
                code = self.emit.emitREADVAR(ast.name, typ, id.value.value, param.frame)
            else:
                code = self.emit.emitGETSTATIC(id.value.value + '/' + ast.name, typ, param.frame)
        return code, typ

    def visitArrayCell(self, ast, param):
        arr_code, arr_type = self.visit(ast.arr, Access(param.frame, param.sym, False))
        idx_code, idx_type = self.visit(ast.idx[0], Access(param.frame, param.sym, False))
        self.infer(ast.idx[0], NumberType(), param.sym)
        idx_code += self.emit.emitF2I(param.frame)
        for idx in ast.idx[1:]:
            self.infer(idx, NumberType(), param.sym)
            idx_code += self.emit.emitALOAD(arr_type, param.frame)
            idx_code += self.visit(idx, Access(param.frame, param.sym, False))[0]
            idx_code += self.emit.emitF2I(param.frame)
        code = arr_code + idx_code
        if param.isLeft:
            return code, arr_type
        else:
            code += self.emit.emitALOAD(arr_type.eleType, param.frame)
            return code, arr_type.eleType

    def visitBlock(self, ast, param):
        code = ''
        param.frame.enterScope(False)
        param.sym.append([])
        for stmt in ast.stmt:
            code += self.visit(stmt, param)
        param.sym.pop()
        param.frame.exitScope()
        return code

    def visitIf(self, ast, param):
        code = ''
        self.infer(ast.expr, BoolType(), param.sym)
        skip_label = param.frame.getNewLabel()
        end_label = param.frame.getNewLabel()
        code += self.visit(ast.expr, Access(param.frame, param.sym, False))[0]
        code += self.emit.emitIFFALSE(skip_label, param.frame)
        code += self.visit(ast.thenStmt, param)
        code += self.emit.emitGOTO(end_label, param.frame)
        code += self.emit.emitLABEL(skip_label, param.frame)
        for cond, stmt in ast.elifStmt:
            self.infer(cond, BoolType(), param.sym)
            skip_label = param.frame.getNewLabel()
            code += self.visit(cond, Access(param.frame, param.sym, False))[0]
            code += self.emit.emitIFFALSE(skip_label, param.frame)
            code += self.visit(stmt, param)
            code += self.emit.emitGOTO(end_label, param.frame)
            code += self.emit.emitLABEL(skip_label, param.frame)
        if ast.elseStmt:
            code += self.visit(ast.elseStmt, param)
        code += self.emit.emitLABEL(end_label, param.frame)
        return code

    def visitFor(self, ast, param):
        self.infer(ast.name, NumberType(), param.sym)
        self.infer(ast.updExpr, NumberType(), param.sym)
        self.infer(ast.condExpr, BoolType(), param.sym)
        code = ''
        param.frame.enterLoop()
        head_label = param.frame.getNewLabel()
        continue_label = param.frame.getContinueLabel()
        break_label = param.frame.getBreakLabel()
        code += self.emit.emitLABEL(head_label, param.frame)
        code += self.visit(ast.condExpr, Access(param.frame, param.sym, False))[0]
        code += self.emit.emitIFFALSE(break_label, param.frame)
        code += self.visit(ast.body, param)
        code += self.emit.emitLABEL(continue_label, param.frame)
        code += self.visit(ast.name, Access(param.frame, param.sym, False))[0]
        code += self.visit(ast.updExpr, Access(param.frame, param.sym, False))[0]
        code += self.emit.emitADDOP('+', NumberType(), param.frame)
        code += self.visit(ast.name, Access(param.frame, param.sym, True))[0]
        code += self.emit.emitGOTO(head_label, param.frame)
        code += self.emit.emitLABEL(break_label, param.frame)
        param.frame.exitLoop()
        return code
        
    def visitContinue(self, ast, param):
        continue_label = param.frame.getContinueLabel()
        return self.emit.emitGOTO(continue_label, param.frame)

    def visitBreak(self, ast, param):
        break_label = param.frame.getBreakLabel()
        return self.emit.emitGOTO(break_label, param.frame)

    def visitReturn(self, ast, param):
        if ast.expr:
            code , typ = self.visit(ast.expr, Access(param.frame, param.sym, False))
            self.infer(param.frame, typ, param.sym)
            return code + self.emit.emitRETURN(typ, param.frame)
        return self.emit.emitRETURN(VoidType(), param.frame)

    def visitAssign(self, ast, param):
        rhs = self.findSymbol(ast.rhs, param.sym)
        if rhs and not rhs.mtype:
            lsym = self.findSymbol(ast.lhs, param.sym)
            if lsym:
                ltype = lsym.mtype
            self.infer(ast.rhs, ltype, param.sym)
        rcode, rtype = self.visit(ast.rhs, Access(param.frame, param.sym, False))
        lhs = self.findSymbol(ast.lhs, param.sym)
        if lhs and not lhs.mtype:
            self.infer(ast.lhs, rtype, param.sym)
        lcode, ltype = self.visit(ast.lhs, Access(param.frame, param.sym, True))
        if type(ltype) is ArrayType:
            return lcode + rcode + self.emit.emitASTORE(ltype.eleType, param.frame)
        else:
            return rcode + lcode

    def visitCallStmt(self, ast, param):
        code = ''
        method = self.findSymbol(ast, param.sym)
        for i, arg in enumerate(ast.args):
            self.infer(arg, method.mtype.partype[i], param.sym)
            code += self.visit(arg, Access(param.frame, param.sym, False))[0]
        name = method.value.value + '/' + method.name
        code += self.emit.emitINVOKESTATIC(name, method.mtype, param.frame)
        return code

    def visitNumberLiteral(self, ast, param):
        value = str(float(ast.value))
        return self.emit.emitPUSHCONST(value, NumberType(), param.frame), NumberType()

    def visitBooleanLiteral(self, ast, param):
        value = str(ast.value).lower()
        return self.emit.emitPUSHCONST(value, BoolType(),param.frame), BoolType()

    def visitStringLiteral(self, ast, param):
        value = '"' + ast.value.replace('"', '\\"') + '"'
        return self.emit.emitPUSHCONST(value, StringType(), param.frame), StringType()

    def visitArrayLiteral(self, ast, param):
        size = len(ast.value)
        code = self.emit.emitPUSHICONST(size, param.frame)
        _, typ = self.visit(ast.value[0], Access(param.frame, param.sym, False))
        if type(typ) is ArrayType or type(typ) is StringType:
            code += self.emit.emitANEWARRAY(typ, param.frame)
        else:
            code += self.emit.emitNEWARRAY(typ, param.frame)
        for i, ele in enumerate(ast.value):
            code += self.emit.emitDUP(param.frame)
            code += self.emit.emitPUSHICONST(i, param.frame)
            code += self.visit(ele, Access(param.frame, param.sym, False))[0]
            code += self.emit.emitASTORE(typ, param.frame)
        if type(typ) is ArrayType:
            return code, ArrayType([size] + typ.size, typ.eleType)
        else:
            return code, ArrayType([size], typ)
        