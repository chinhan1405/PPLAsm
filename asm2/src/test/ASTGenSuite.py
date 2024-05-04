import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_line_1(self):
        input = """ number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_simple_line_2(self):
        input = """ 
            func funtion() return f(1,2) 
        """
        expect = str(Program([FuncDecl(Id("funtion"), [], Return(CallExpr(Id("f"), [NumberLiteral(float(1)), NumberLiteral(float(2))])))]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_simple_line_3(self):
        input = """ 
            func main() 
            begin
                number b
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("b"), NumberType())]))]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_continue_statement(self):
        input = """ 
            func main() begin
                continue
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Continue()]))]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_break_statement(self):
        input = """ 
            func main() 
            begin
                break
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Break()]))]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_return_statement_1(self):
        input = """ 
            func main() return
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return())]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_return_statement_2(self):
        input = """ 
            func main() return "hello"
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return(StringLiteral("hello")))]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_simple_line_4(self):
        input = """
            func main() 
            begin
                number a <- 3.2
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, NumberLiteral(float(3.2)))]))]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_simple_line_5(self):
        input = """
            func main() 
            begin
                string b <- "hello"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("b"), StringType(), None, StringLiteral("hello"))]))]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_simple_line_6(self):
        input = """
            func main() 
            begin
                bool c <- true
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("c"), BoolType(), None, BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_if_statement(self):
        input = """
            func main() 
            begin
                if (a) return b
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(Id("a"), Return(Id("b")))]))]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_if_else(self):
        input = """
            func main() 
            begin
                if (a) return b else return c
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(Id("a"), Return(Id("b")), [], Return(Id("c")))]))]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_if_elif_else(self):
        input = """
            func main() 
            begin
                if (a) return b elif (e) return c else return d
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(Id("a"), Return(Id("b")), [(Id("e"), Return(Id("c")))], Return(Id("d")))]))]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_for_statement(self):
        input = """
            func main() 
            begin
                for a until a>10 by 1 c <- a
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("a"), BinaryOp(">", Id("a"), NumberLiteral(float(10))), NumberLiteral(float(1)), Assign(Id("c"), Id("a")))]))]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_for_block(self):
        input = """
            func main() 
            begin
                for a until a<10 by -1
                begin
                    c <- a
                end
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("a"), BinaryOp("<", Id("a"), NumberLiteral(float(10))), UnaryOp("-", NumberLiteral(float(1))), Block([Assign(Id("c"), Id("a"))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_if_in_for(self):
        input = """
            func main() 
            begin
                for a until a<10 by -1
                begin
                    if (d) continue
                end
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("a"), BinaryOp("<", Id("a"), NumberLiteral(float(10))), UnaryOp("-", NumberLiteral(float(1))), Block([If(Id("d"), Continue())]))]))]))
        self.assertTrue(TestAST.test(input, expect, 315))
    
    def test_if_in_if(self):
        input = """
            func main() 
            begin
                if (a) begin
                    if (d) return 0
                end
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(Id("a"), Block([If(Id("d"), Return(NumberLiteral(float(0))))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_for_in_for(self):
        input = """
            func main() 
            begin
                for a until a<10 by -1
                begin
                    for b until b<10 by -1
                    begin
                        c <- a
                    end
                end
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("a"), BinaryOp("<", Id("a"), NumberLiteral(float(10))), UnaryOp("-", NumberLiteral(float(1))), Block([For(Id("b"), BinaryOp("<", Id("b"), NumberLiteral(float(10))), UnaryOp("-", NumberLiteral(float(1))), Block([Assign(Id("c"), Id("a"))]))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_for_in_if(self):
        input = """
            func main() 
            begin
                if (a) begin
                    for b until b<10 by -1
                    begin
                        c <- a
                    end
                end
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(Id("a"), Block([For(Id("b"), BinaryOp("<", Id("b"), NumberLiteral(float(10))), UnaryOp("-", NumberLiteral(float(1))), Block([Assign(Id("c"), Id("a"))]))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_for_in_if_else(self):
        input = """
            func main() 
            begin
                if (a) begin
                    for b until b<10 by -1
                    begin
                        c <- a
                    end
                end else begin
                    for b until b<10 by -1
                    begin
                        c <- a
                    end
                end
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(Id("a"), Block([For(Id("b"), BinaryOp("<", Id("b"), NumberLiteral(float(10))), UnaryOp("-", NumberLiteral(float(1))), Block([Assign(Id("c"), Id("a"))]))]), [], Block([For(Id("b"), BinaryOp("<", Id("b"), NumberLiteral(float(10))), UnaryOp("-", NumberLiteral(float(1))), Block([Assign(Id("c"), Id("a"))]))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_simple_program_1(self):
        input = """
            func main() 
            begin
                number a
                a <- 3
                return a
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType()), Assign(Id("a"), NumberLiteral(float(3))), Return(Id("a"))]))]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_simple_program_2(self):
        input = """
            func main() 
            begin
                number a
                a <- 3
                if (a>2) return a else return 0
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType()), Assign(Id("a"), NumberLiteral(float(3))), If(BinaryOp(">", Id("a"), NumberLiteral(float(2))), Return(Id("a")), [], Return(NumberLiteral(float(0))))]))]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_simple_program_3(self):
        input = """
            func main() 
            begin
                string str <- "Hello"
                number n <- 12
                bool b <- true
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("str"), StringType(), None, StringLiteral("Hello")), VarDecl(Id("n"), NumberType(), None, NumberLiteral(float(12))), VarDecl(Id("b"), BoolType(), None, BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_simple_program_4(self):
        input = """
            func main() 
            begin
                number a
                for a until a<10 by 0
                begin
                    a <- a + 1
                end
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType()), For(Id("a"), BinaryOp("<", Id("a"), NumberLiteral(float(10))), NumberLiteral(float(0)), Block([Assign(Id("a"), BinaryOp("+", Id("a"), NumberLiteral(float(1))))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_simple_program_5(self):
        input = """
            func main() 
            begin
                number a
                for a until a<10 by 0
                begin
                    if (a>5) return a
                end
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType()), For(Id("a"), BinaryOp("<", Id("a"), NumberLiteral(float(10))), NumberLiteral(float(0)), Block([If(BinaryOp(">", Id("a"), NumberLiteral(float(5))), Return(Id("a")))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_simple_program_6(self):
        input = """
            number a
            func main() 
            begin
                for a until a<10 by 0
                begin
                    if (a>5) return a
                    else continue
                end
            end
        """
        expect = str(Program([VarDecl(Id("a"), NumberType()), FuncDecl(Id("main"), [], Block([For(Id("a"), BinaryOp("<", Id("a"), NumberLiteral(float(10))), NumberLiteral(float(0)), Block([If(BinaryOp(">", Id("a"), NumberLiteral(float(5))), Return(Id("a")), [], Continue())]))]))]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_simple_program_7(self):
        input = """
            func fibo(number n)
            func main() 
            begin
                number a <- fibo(10)
            end
        """
        expect = str(Program([FuncDecl(Id("fibo"), [VarDecl(Id("n"), NumberType())]), FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, CallExpr(Id("fibo"), [NumberLiteral(float(10))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_simple_program_8(self):
        input = """
            func fibo(number n)
            begin
                if (n<2) return n
                else return fibo(n-1) + fibo(n-2)
            end
            func main() 
            begin
                number a <- fibo(10)
            end
        """
        expect = str(Program([FuncDecl(Id("fibo"), [VarDecl(Id("n"), NumberType())], Block([If(BinaryOp("<", Id("n"), NumberLiteral(float(2))), Return(Id("n")), [], Return(BinaryOp("+", CallExpr(Id("fibo"), [BinaryOp("-", Id("n"), NumberLiteral(float(1)))]), CallExpr(Id("fibo"), [BinaryOp("-", Id("n"), NumberLiteral(float(2)))]))))])), FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, CallExpr(Id("fibo"), [NumberLiteral(float(10))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_simple_program_9(self):
        input = """
            func fibo(number n)
            func main()
            func fibo(number n)
            begin
                if (n<2) return n
                else return fibo(n-1) + fibo(n-2)
            end
        """
        expect = str(Program([FuncDecl(Id("fibo"), [VarDecl(Id("n"), NumberType())]), FuncDecl(Id("main"), []), FuncDecl(Id("fibo"), [VarDecl(Id("n"), NumberType())], Block([If(BinaryOp("<", Id("n"), NumberLiteral(float(2))), Return(Id("n")), [], Return(BinaryOp("+", CallExpr(Id("fibo"), [BinaryOp("-", Id("n"), NumberLiteral(float(1)))]), CallExpr(Id("fibo"), [BinaryOp("-", Id("n"), NumberLiteral(float(2)))]))))]))]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_simple_program_10(self):
        input = """
            string str
            number a <- 10
            func fibo(number n)
            func main() return fibo(a)
        """
        expect = str(Program([VarDecl(Id("str"), StringType()), VarDecl(Id("a"), NumberType(), None, NumberLiteral(float(10))), FuncDecl(Id("fibo"), [VarDecl(Id("n"), NumberType())]), FuncDecl(Id("main"), [], Return(CallExpr(Id("fibo"), [Id("a")])))]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_array_1(self):
        input = """
            func main()
            begin
                number a[5]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(5)], NumberType()))]))]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_array_2(self):
        input = """
            func main()
            begin
                number a[5]
                a[0] <- 1
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(5)], NumberType()), None, None), Assign(ArrayCell(Id("a"), [NumberLiteral(float(0))]), NumberLiteral(float(1)))]))]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_array_3(self):
        input = """
            func main()
            begin
                number a[5]
                for i until i<5 by 1
                begin
                    a[i] <- i
                end
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(5)], NumberType()), None, None), For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(float(5))), NumberLiteral(float(1)), Block([Assign(ArrayCell(Id("a"), [Id("i")]), Id("i"))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_array_4(self):
        input = """
            func main()
            begin
                number a[5] <- [1, 2, 3, 4, 5]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(5)], NumberType()), None, ArrayLiteral([NumberLiteral(float(1)), NumberLiteral(float(2)), NumberLiteral(float(3)), NumberLiteral(float(4)), NumberLiteral(float(5))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_array_5(self):
        input = """
            func main()
            begin
                number a[5] <- [1, 2, 3, 4, 5]
                return a[3]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(5)], NumberType()), None, ArrayLiteral([NumberLiteral(float(1)), NumberLiteral(float(2)), NumberLiteral(float(3)), NumberLiteral(float(4)), NumberLiteral(float(5))])), Return(ArrayCell(Id("a"), [NumberLiteral(float(3))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_array_6(self):
        input = """
            func main()
            begin
                number a[5]
                a[3] <- a[4]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(5)], NumberType()), None, None), Assign(ArrayCell(Id("a"), [NumberLiteral(float(3))]), ArrayCell(Id("a"), [NumberLiteral(float(4))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_array_7(self):
        input = """
            func main()
            begin
                number a[5, 2]
                a[3, 1] <- a[4, 2]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(5), float(2)], NumberType()), None, None), Assign(ArrayCell(Id("a"), [NumberLiteral(float(3)), NumberLiteral(float(1))]), ArrayCell(Id("a"), [NumberLiteral(float(4)), NumberLiteral(float(2))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_array_8(self):
        input = """
            func main()
            begin
                number a[2, 2] <- [[1, 2], [2, 3]]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(2), float(2)], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(float(1)), NumberLiteral(float(2))]), ArrayLiteral([NumberLiteral(float(2)), NumberLiteral(float(3))])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_array_9(self):
        input = """
            func main()
            begin
                number a[2, 2, 2] <- [[[1, 2], [2, 3]], [[3, 4], [4, 5]]]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(2), float(2), float(2)], NumberType()), None, ArrayLiteral([ArrayLiteral([ArrayLiteral([NumberLiteral(float(1)), NumberLiteral(float(2))]), ArrayLiteral([NumberLiteral(float(2)), NumberLiteral(float(3))])]), ArrayLiteral([ArrayLiteral([NumberLiteral(float(3)), NumberLiteral(float(4))]), ArrayLiteral([NumberLiteral(float(4)), NumberLiteral(float(5))])])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_array_10(self):
        input = """
            func main()
            begin
                return f(4)[2]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(ArrayCell(CallExpr(Id("f"), [NumberLiteral(float(4))]), [NumberLiteral(float(2))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_array_11(self):
        input = """
            func main()
            begin
                a[3 + foo(2)] <- 4
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(float(3)), CallExpr(Id("foo"), [NumberLiteral(float(2))]) )]), NumberLiteral(float(4)))]))]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_array_12(self):
        input = """
            func main()
            begin
                c <- a[b[2, 3]]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Assign(Id("c"), ArrayCell(Id("a"), [ArrayCell(Id("b"), [NumberLiteral(float(2)), NumberLiteral(float(3))])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_array_13(self):
        input = """
            func main()
            begin
                return a[b[c[d[e[f]]]]]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(ArrayCell(Id("a"), [ArrayCell(Id("b"), [ArrayCell(Id("c"), [ArrayCell(Id("d"), [ArrayCell(Id("e"), [Id("f")])])])])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_array_14(self):
        input = """
            func main()
            begin
                string a[2] <- ["hello", "world"]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(2)], StringType()), None, ArrayLiteral([StringLiteral("hello"), StringLiteral("world")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_array_15(self):
        input = """
            func main()
            begin
                string a[2,3] <- [["hello", "world", "hello"], ["world", "hello", "world"]]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(2), float(3)], StringType()), None, ArrayLiteral([ArrayLiteral([StringLiteral("hello"), StringLiteral("world"), StringLiteral("hello")]), ArrayLiteral([StringLiteral("world"), StringLiteral("hello"), StringLiteral("world")])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_array_16(self):
        input = """
            func main()
            begin
                bool a[3] <- [true, false, true]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(3)], BoolType()), None, ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(True)]))]))]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_array_17(self):
        input = """
            func main()
            begin
                bool a[2,3] <- [[true, false, true], [false, true, false]]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(2), float(3)], BoolType()), None, ArrayLiteral([ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(True)]), ArrayLiteral([BooleanLiteral(False), BooleanLiteral(True), BooleanLiteral(False)])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_array_18(self):
        input = """
            func main()
            begin
                number a[2] <- [fibo(1), fibo(2)]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(2)], NumberType()), None, ArrayLiteral([CallExpr(Id("fibo"), [NumberLiteral(float(1))]), CallExpr(Id("fibo"), [NumberLiteral(float(2))])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_array_19(self):
        input = """
            func main()
            begin
                string a[3]
                a[0] <- "hello"
                return a[0]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(3)], StringType()), None, None), Assign(ArrayCell(Id("a"), [NumberLiteral(float(0))]), StringLiteral("hello")), Return(ArrayCell(Id("a"), [NumberLiteral(float(0))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_array_20(self):
        input = """
            func main()
            begin
                number a[1] <- []
                string b[2] <- ["hello", "world"]
                bool c[3] <- [true, false, true]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(1)], NumberType()), None, ArrayLiteral([])), VarDecl(Id("b"), ArrayType([float(2)], StringType()), None, ArrayLiteral([StringLiteral("hello"), StringLiteral("world")])), VarDecl(Id("c"), ArrayType([float(3)], BoolType()), None, ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(True)]))]))]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_expression_1(self):
        input = """
            func main()
            begin
                return 1+1 + 0.5 - - 2
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(float(1)), NumberLiteral(float(1)),), NumberLiteral(float(0.5))), UnaryOp("-", NumberLiteral(float(2)))))]))]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_expression_2(self):
        input = """
            func main()
            begin
                return 1+2*3/4%5 * (e+f)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("+", NumberLiteral(float(1)), BinaryOp("*", BinaryOp("%", BinaryOp("/", BinaryOp("*", NumberLiteral(float(2)), NumberLiteral(float(3)),), NumberLiteral(float(4))), NumberLiteral(float(5))), BinaryOp("+", Id("e"), Id("f")))))]))]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_expression_3(self):
        input = """
            func main()
            begin
                return a + b + c + d
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("+", BinaryOp("+", BinaryOp("+", Id("a"), Id("b")), Id("c")), Id("d")))]))]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_expression_4(self):
        input = """
            func main()
            begin
                return a - b - c - d
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("-", BinaryOp("-", BinaryOp("-", Id("a"), Id("b")), Id("c")), Id("d")))]))]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_expression_5(self):
        input = """
            func main()
            begin
                return a or b or c and d
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("and", BinaryOp("or", BinaryOp("or", Id("a"), Id("b")), Id("c")), Id("d")))]))]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_expression_6(self):
        input = """
            func main()
            begin
                return (a = b) or (c = d)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("or", BinaryOp("=", Id("a"), Id("b")), BinaryOp("=", Id("c"), Id("d"))))]))]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_expression_7(self):
        input = """
            func main()
            begin
                return a = b or c
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("=", Id("a"), BinaryOp("or", Id("b"), Id("c"))))]))]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_expression_8(self):
        input = """
            func main()
            begin
                return a * b + c / d
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("+", BinaryOp("*", Id("a"), Id("b")), BinaryOp("/", Id("c"), Id("d"))))]))]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_expression_9(self):
        input = """
            func main()
            begin
                return c and not a and b
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("and", BinaryOp("and", Id("c"), UnaryOp("not", Id("a"))), Id("b")))]))]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_expression_10(self):
        input = """
            func main()
            begin
                return -a--b----c
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("-", BinaryOp("-", UnaryOp("-", Id("a")), UnaryOp("-", Id("b"))), UnaryOp("-", UnaryOp("-", UnaryOp("-", Id("c"))))))]))]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_expression_11(self):
        input = """
            func main()
            begin
                return - foo(1,2)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(UnaryOp("-", CallExpr(Id("foo"), [NumberLiteral(float(1)), NumberLiteral(float(2))])))]))]))
        self.assertTrue(TestAST.test(input, expect, 360))
    
    def test_expression_12(self):
        input = """
            func main()
            begin
                return foo() and false
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("and", CallExpr(Id("foo"), []), BooleanLiteral(False)))]))]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_expression_13(self):
        input = """
            func main()
            begin
                return -a - (b + c)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("-", UnaryOp("-", Id("a")), BinaryOp("+", Id("b"), Id("c"))))]))]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_expression_14(self):
        input = """
            func main()
            begin
                return -a - b + c
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("+", BinaryOp("-", UnaryOp("-", Id("a")), Id("b")), Id("c")))]))]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_expression_15(self):
        input = """
            func main()
            begin
                return -b * c
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("*", UnaryOp("-", Id("b")), Id("c")))]))]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_expression_16(self):
        input = """
            func main()
            begin
                return a[1] * 2
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("*", ArrayCell(Id("a"), [NumberLiteral(float(1))]), NumberLiteral(float(2))))]))]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_expression_17(self):
        input = """
            func main()
            begin
                return a[1, b  + -3]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(ArrayCell(Id("a"), [NumberLiteral(float(1)), BinaryOp("+", Id("b"), UnaryOp("-", NumberLiteral(float(3))))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_expression_18(self):
        input = """
            func main()
            begin
                return a[1+2.0*3]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(float(1)), BinaryOp("*", NumberLiteral(float(2)), NumberLiteral(float(3))))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_expression_19(self):
        input = """
            func main()
            begin
                return s1 ... s2 
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("...", Id("s1"), Id("s2")))]))]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_expression_20(self):
        input = """
            func main()
            begin
                return s1 ... (s2 ... s3)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("...", Id("s1"), BinaryOp("...", Id("s2"), Id("s3"))))]))]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_declaration_1(self):
        input = """
            func main()
            begin
                number a
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType())]))]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_declaration_2(self):
        input = """
            func main()
            begin
                string b <- "hello"..."world"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("b"), StringType(), None, BinaryOp("...", StringLiteral("hello"), StringLiteral("world")))]))]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_declaration_3(self):
        input = """
            func main()
            begin
                bool c <- true or false
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("c"), BoolType(), None, BinaryOp("or", BooleanLiteral(True), BooleanLiteral(False)))]))]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_declaration_4(self):
        input = """
            func main()
            begin
                var a <- 3
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "var", NumberLiteral(float(3)))]))]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_declaration_5(self):
        input = """
            func main()
            begin
                dynamic b
                b <- "hello"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("b"), None, "dynamic"), Assign(Id("b"), StringLiteral("hello"))]))]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_declaration_6(self):
        input = """
            func main()
            begin
                number c <- 3.0e4
                string d <- "3.0e5"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("c"), NumberType(), None, NumberLiteral(float(3.0e4))), VarDecl(Id("d"), StringType(), None, StringLiteral("3.0e5"))]))]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_declaration_7(self):
        input = """
            func main()
            begin
                number a <- 3e-4
                var b <- "'"Hi'""
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, NumberLiteral(float(3e-4))), VarDecl(Id("b"), None, "var", StringLiteral('"Hi"'))]))]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_declaration_8(self):
        input = """
            func main()
            begin
                string b <- foo()...bar()
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("b"), StringType(), None, BinaryOp("...", CallExpr(Id("foo"), []), CallExpr(Id("bar"), [])))]))]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_declaration_9(self):
        input = """
            func main()
            begin
                string a[2] <- ["hello", "world"]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([float(2)], StringType()), None, ArrayLiteral([StringLiteral("hello"), StringLiteral("world")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_declaration_10(self):
        input = """
            func foo()
            func main()
            begin
                foo()
            end
        """
        expect = str(Program([FuncDecl(Id("foo"), []), FuncDecl(Id("main"), [], Block([CallStmt(Id("foo"), [])]))]))
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_numlit_1(self):
        input = """
            func main()
            begin
                return 0.3e-10
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(NumberLiteral(float(0.3e-10)))]))]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_numlit_2(self):
        input = """
            func main()
            begin
                return -3e4
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(UnaryOp("-", NumberLiteral(float(3e4))))]))]))
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_numlit_3(self):
        input = """
            func main()
            begin
                return 12345678.0912313e+12
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(NumberLiteral(float(12345678.0912313e+12)))]))]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_string_lit_1(self):
        input = """
            func main()
            begin
                return "hello"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(StringLiteral("hello"))]))]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_string_lit_2(self):
        input = """
            func main()
            begin
                return "hello '" world"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(StringLiteral("hello \" world"))]))]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_string_lit_3(self):
        input = """
            func main()
            begin
                return "hello ' world \\n"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(StringLiteral("hello ' world \n"))]))]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_string_lit_4(self):
        input = """
            func main()
            begin
                return "hello world \\t"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(StringLiteral("hello world \t"))]))]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_string_lit_5(self):
        input = """
            func main()
            begin
                return "hello world \\\\"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(StringLiteral("hello world \\"))]))]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_boolean_lit_1(self):
        input = """
            func main()
            begin
                return true
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_boolean_lit_2(self):
        input = """
            func main()
            begin
                return false
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_program_1(self):
        input = """
            func main()
            begin
                number a <- 2
                if (a > 1) begin
                    return 1
                end
                else begin
                    return 0
                end
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, NumberLiteral(float(2))), If(BinaryOp(">", Id("a"), NumberLiteral(float(1))), Block([Return(NumberLiteral(float(1)))]), [], Block([Return(NumberLiteral(float(0)))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_program_2(self):
        input = """
            func fibo(number n)
            begin
                if (n<2) return n
                else return fibo(n-1) + fibo(n-2)
            end
            func main()
            begin
                return fibo(10)
            end
        """
        expect = str(Program([FuncDecl(Id("fibo"), [VarDecl(Id("n"), NumberType())], Block([If(BinaryOp("<", Id("n"), NumberLiteral(float(2))), Return(Id("n")), [], Return(BinaryOp("+", CallExpr(Id("fibo"), [BinaryOp("-", Id("n"), NumberLiteral(float(1)))]), CallExpr(Id("fibo"), [BinaryOp("-", Id("n"), NumberLiteral(float(2)))]))))])), FuncDecl(Id("main"), [], Block([Return(CallExpr(Id("fibo"), [NumberLiteral(float(10))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_program_3(self):
        input = """
            func foo(number a[5], string b)
            begin
                var i <- 0
                for i until i >= 5 by 1
                begin
                    a[i] <- i*i
                end
                return -1
            end
        """
        expect = str(Program([FuncDecl(
            Id("foo"),
            [
                VarDecl(Id("a"), ArrayType([float(5)], NumberType()), None, None),
                VarDecl(Id("b"), StringType())
            ],
            Block([
                VarDecl(Id("i"), None, "var", NumberLiteral(float(0))),
                For(
                    Id("i"),
                    BinaryOp(">=", Id("i"), NumberLiteral(float(5))),
                    NumberLiteral(float(1)),
                    Block([
                        Assign(ArrayCell(Id("a"), [Id("i")]), BinaryOp("*", Id("i"), Id("i")))
                    ])
                ),
                Return(UnaryOp("-", NumberLiteral(float(1)))
                )
            ])
        )]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_program_4(self):
        input = """
            func main()
            begin
                for i until i < 10 by 1
                begin
                    if (i%2=0) continue
                end
            end
        """
        expect = str(Program([FuncDecl(
            Id("main"),
            [],
            Block([
                For(
                    Id("i"),
                    BinaryOp("<", Id("i"), NumberLiteral(float(10))),
                    NumberLiteral(float(1)),
                    Block([
                        If(
                            BinaryOp("=", BinaryOp("%", Id("i"), NumberLiteral(float(2))), NumberLiteral(float(0))),
                            Continue()
                        )
                    ])
                )
            ])
        )]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_program_5(self):
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) writeString("Yes")
                else writeString("No")
            end
        """
        expect = str(Program([
            FuncDecl(
                Id("areDivisors"),
                [
                    VarDecl(Id("num1"), NumberType()),
                    VarDecl(Id("num2"), NumberType())
                ],
                Return(
                    BinaryOp(
                        "or",
                        BinaryOp("=", BinaryOp("%", Id("num1"), Id("num2")), NumberLiteral(float(0))),
                        BinaryOp("=", BinaryOp("%", Id("num2"), Id("num1")), NumberLiteral(float(0)))
                    )
                )
            ),
            FuncDecl(
                Id("main"),
                [],
                Block([
                    VarDecl(Id("num1"), None, "var", CallExpr(Id("readNumber"), [])),
                    VarDecl(Id("num2"), None, "var", CallExpr(Id("readNumber"), [])),
                    If(
                        CallExpr(Id("areDivisors"), [Id("num1"), Id("num2")]),
                        CallStmt(Id("writeString"), [StringLiteral("Yes")]), [],
                        CallStmt(Id("writeString"), [StringLiteral("No")])
                    )
                ])
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_program_6(self):
        input = """
            func main()
            begin
                var a <- 1
                var b <- 2
                var c <- 3
                if ((a > b) and (b > c)) writeString("Yes")
                else writeString("No")
            end
        """
        expect = str(Program([FuncDecl(
            Id("main"),
            [],
            Block([
                VarDecl(Id("a"), None, "var", NumberLiteral(float(1))),
                VarDecl(Id("b"), None, "var", NumberLiteral(float(2))),
                VarDecl(Id("c"), None, "var", NumberLiteral(float(3))),
                If(
                    BinaryOp("and", BinaryOp(">", Id("a"), Id("b")), BinaryOp(">", Id("b"), Id("c"))),
                    CallStmt(Id("writeString"), [StringLiteral("Yes")]), [],
                    CallStmt(Id("writeString"), [StringLiteral("No")])
                )
            ])
        )]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_program_7(self):
        input = """
            number a <- 2
            func main()
            begin
                for a until a < 10 by 1
                begin
                    writeNumber(a)
                    a <- a + 1
                end
            end
        """
        expect = str(Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(float(2))),
            FuncDecl(
                Id("main"),
                [],
                Block([
                    For(
                        Id("a"),
                        BinaryOp("<", Id("a"), NumberLiteral(float(10))),
                        NumberLiteral(float(1)),
                        Block([
                            CallStmt(Id("writeNumber"), [Id("a")]),
                            Assign(Id("a"), BinaryOp("+", Id("a"), NumberLiteral(float(1)))
                            )
                        ])
                    )
                ])
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_program_8(self):
        input = """
            func foo()
            func main()
            begin
                var i <- 1
                for i until i<10 by 1 foo()
            end
            func foo()
            begin
                writeString("Hello")
            end
        """
        expect = str(Program([
            FuncDecl(Id("foo"), []),
            FuncDecl(
                Id("main"),
                [],
                Block([
                    VarDecl(Id("i"), None, "var", NumberLiteral(float(1))),
                    For(
                        Id("i"),
                        BinaryOp("<", Id("i"), NumberLiteral(float(10))),
                        NumberLiteral(float(1)),
                        CallStmt(Id("foo"), [])
                    )
                ])
            ),
            FuncDecl(
                Id("foo"),
                [],
                Block([
                    CallStmt(Id("writeString"), [StringLiteral("Hello")])
                ])
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_program_9(self):
        input = """
            func concat(string s1, string s2)
            begin
                return s1...s2
            end
            func main()
            begin
                var a <- "Hello"
                var b <- " World"
                writeString(concat(a, b))
            end
        """
        expect = str(Program([
            FuncDecl(
                Id("concat"),
                [
                    VarDecl(Id("s1"), StringType()),
                    VarDecl(Id("s2"), StringType())
                ],
                Block([
                    Return(BinaryOp("...", Id("s1"), Id("s2")))
                ])
            ),
            FuncDecl(
                Id("main"),
                [],
                Block([
                    VarDecl(Id("a"), None, "var", StringLiteral("Hello")),
                    VarDecl(Id("b"), None, "var", StringLiteral(" World")),
                    CallStmt(Id("writeString"), [CallExpr(Id("concat"), [Id("a"), Id("b")])])
                ])
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_program_10(self):
        input = """
            func and_(bool a, bool b)
            begin
                return a and b 
            end
            func main()
            begin
                writeString(and_(true, false))
            end
        """
        expect = str(Program([
            FuncDecl(
                Id("and_"),
                [
                    VarDecl(Id("a"), BoolType()),
                    VarDecl(Id("b"), BoolType())
                ],
                Block([
                    Return(BinaryOp("and", Id("a"), Id("b")))
                ])
            ),
            FuncDecl(
                Id("main"),
                [],
                Block([
                    CallStmt(Id("writeString"), [CallExpr(Id("and_"), [BooleanLiteral(True), BooleanLiteral(False)])])
                ])
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 399))

