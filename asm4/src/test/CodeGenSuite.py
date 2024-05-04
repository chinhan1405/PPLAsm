import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_number_1(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeNumber"), [NumberLiteral(1.0)])
            )
        ])
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_number_2(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeNumber"), [NumberLiteral(2e2)])
            )
        ])
        expect = "200.0"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_number_3(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeNumber"), [NumberLiteral(3.0234)])
            )
        ])
        expect = "3.0234"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_bool_1(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [BooleanLiteral(True)])
            )
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_bool_2(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [BooleanLiteral(False)])
            )
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_string_1(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeString"), [StringLiteral("Hello")])
            )
        ])
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_string_2(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeString"), [StringLiteral(" \"World")])
            )
        ])
        expect = " \"World"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_string_3(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeString"), [StringLiteral("Hello World")])
            )
        ])
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_string_4(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeString"), [StringLiteral("Hello \n World!")])
            )
        ])
        expect = "Hello \n World!"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_var_decl_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ])
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_var_decl_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), StringType(), None, StringLiteral("Hello World!")),
                CallStmt(Id("writeString"), [Id("a")])
            ]))
        ])
        expect = "Hello World!"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_var_decl_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), BoolType(), None, BooleanLiteral(True)),
                CallStmt(Id("writeBool"), [Id("a")])
            ]))
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_var_decl_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'var', NumberLiteral(1e5)),
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ])
        expect = "100000.0"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_global_var_1(self):
        input = Program([
            VarDecl(Id("a"), NumberType()),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))     
        ])
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_global_var_2(self):
        input = Program([
            VarDecl(Id("a"), StringType()),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeString"), [Id("a")])
            ]))     
        ])
        expect = "null"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_global_var_3(self):
        input = Program([
            VarDecl(Id("a"), BoolType()),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeBool"), [Id("a")])
            ]))     
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_global_var_4(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            VarDecl(Id("b"), NumberType(), None, NumberLiteral(2.0)),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))     
        ])
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_global_var_5(self):
        input = Program([
            VarDecl(Id("a"), StringType(), None, StringLiteral("Hello World!")),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeString"), [Id("a")])
            ]))     
        ])
        expect = "Hello World!"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_global_var_6(self):
        input = Program([
            VarDecl(Id("a"), None, 'var', BooleanLiteral(True)),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeBool"), [Id("a")])
            ]))     
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_assignment_1(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            FuncDecl(Id("main"), [], Block([
                Assign(Id("a"), NumberLiteral(2.0)),
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ])
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_assignment_2(self):
        input = Program([
            VarDecl(Id("a"), StringType(), None, StringLiteral("Hello")),
            FuncDecl(Id("main"), [], Block([
                Assign(Id("a"), StringLiteral("World")),
                CallStmt(Id("writeString"), [Id("a")])
            ]))
        ])
        expect = "World"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_assignment_3(self):
        input = Program([
            VarDecl(Id("a"), BoolType(), None, BooleanLiteral(True)),
            FuncDecl(Id("main"), [], Block([
                Assign(Id("a"), BooleanLiteral(False)),
                CallStmt(Id("writeBool"), [Id("a")])
            ]))
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_if_1(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            FuncDecl(Id("main"), [], Block([
                If(BooleanLiteral(True), Block([
                    Assign(Id("a"), NumberLiteral(2.0))
                ])),
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ])
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_if_2(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            FuncDecl(Id("main"), [], Block([
                If(BooleanLiteral(False), Block([
                    Assign(Id("a"), NumberLiteral(2.0))
                ])),
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ])
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_if_3(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            FuncDecl(Id("main"), [], Block([
                If(BooleanLiteral(False), Block([
                    Assign(Id("a"), NumberLiteral(2.0))
                ]), [], Block([
                    Assign(Id("a"), NumberLiteral(3.0))
                ])),
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ])
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_if_4(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            FuncDecl(Id("main"), [], Block([
                If(BooleanLiteral(False), Block([
                    Assign(Id("a"), NumberLiteral(2.0))
                ]), [
                    (BooleanLiteral(True), Assign(Id("a"), NumberLiteral(4.0)))
                ], Block([
                    Assign(Id("a"), NumberLiteral(3.0))
                ])),
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ])
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_binop_1(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeNumber"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))])
            )
        ])
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_binop_2(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeNumber"), [BinaryOp("-", NumberLiteral(1.0), NumberLiteral(2.0))])
            )
        ])
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 527))
    
    def test_binop_3(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeNumber"), [BinaryOp("*", NumberLiteral(1.5), NumberLiteral(2.0))])
            )
        ])
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_binop_4(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeNumber"), [BinaryOp("/", NumberLiteral(1.0), NumberLiteral(2.0))])
            )
        ])
        expect = "0.5"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_binop_5(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeNumber"), [BinaryOp("%", NumberLiteral(5.0), NumberLiteral(2.0))])
            )
        ])
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_binop_6(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [BinaryOp(">", NumberLiteral(5.0), NumberLiteral(2.0))])
            )
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_binop_7(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [BinaryOp("<", NumberLiteral(5.0), NumberLiteral(2.0))])
            )
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_binop_8(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [BinaryOp(">=", NumberLiteral(5.0), NumberLiteral(2.0))])
            )
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_binop_9(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [BinaryOp("<=", NumberLiteral(5.0), NumberLiteral(2.0))])
            )
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_binop_10(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [BinaryOp("=", NumberLiteral(5.0), NumberLiteral(2.0))])
            )
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_binop_11(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [BinaryOp("!=", NumberLiteral(5.0), NumberLiteral(2.0))])
            )
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_binop_12(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [BinaryOp("==", StringLiteral("Hi"), StringLiteral("Hello"))])
            )
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_binop_13(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeString"), [BinaryOp("...", StringLiteral("Hi"), StringLiteral("Hello"))])
            )
        ])
        expect = "HiHello"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_for_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(1.0)),
                For(Id("i"), BinaryOp('<', Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([
                    CallStmt(Id("writeNumber"), [Id("i")]),
                    CallStmt(Id("writeString"), [StringLiteral(" ")])
                ]))
            ]))
        ])
        expect = "1.0 2.0 3.0 4.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_for_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(5.0)),
                For(Id("i"), BinaryOp('>', Id("i"), NumberLiteral(1.0)), UnaryOp('-', NumberLiteral(1.0)), Block([
                    CallStmt(Id("writeNumber"), [Id("i")]),
                    CallStmt(Id("writeString"), [StringLiteral(" ")])
                ]))
            ]))
        ])
        expect = "5.0 4.0 3.0 2.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_for_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(1.0)),
                For(Id("i"), BinaryOp('<=', Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([
                    CallStmt(Id("writeNumber"), [Id("i")]),
                    CallStmt(Id("writeString"), [StringLiteral(" ")])
                ]))
            ]))
        ])
        expect = "1.0 2.0 3.0 4.0 5.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_for_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                VarDecl(Id("j"), NumberType(), None, NumberLiteral(1.0)),
                For(Id("i"), BinaryOp('<=', Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([
                    Assign(Id("j"), BinaryOp('+', Id("i"), NumberLiteral(1.0))),
                    For(Id("j"), BinaryOp('<=', Id("j"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([
                        CallStmt(Id("writeNumber"), [Id("j")]),
                        CallStmt(Id("writeString"), [StringLiteral(" ")])
                    ]))
                ]))
            ]))
        ])
        expect = "1.0 2.0 3.0 4.0 5.0 2.0 3.0 4.0 5.0 3.0 4.0 5.0 4.0 5.0 5.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_for_continue(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                For(Id("i"), BinaryOp('<', Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([
                    If(BinaryOp('=', Id("i"), NumberLiteral(2.0)), Block([
                        Continue()
                    ])),
                    CallStmt(Id("writeNumber"), [Id("i")]),
                    CallStmt(Id("writeString"), [StringLiteral(" ")])
                ]))
            ]))
        ])
        expect = "0.0 1.0 3.0 4.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_for_break(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                For(Id("i"), BinaryOp('<', Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([
                    If(BinaryOp('=', Id("i"), NumberLiteral(2.0)), Block([
                        Break()
                    ])),
                    CallStmt(Id("writeNumber"), [Id("i")]),
                    CallStmt(Id("writeString"), [StringLiteral(" ")])
                ]))
            ]))
        ])
        expect = "0.0 1.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_unaryop_1(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeNumber"), [UnaryOp('-', NumberLiteral(1.0))])
            )
        ])
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 545))   

    def test_unaryop_2(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [UnaryOp('not', BooleanLiteral(True))])
            )
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 546)) 

    def test_unaryop_3(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [UnaryOp('not', BooleanLiteral(False))])
            )
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_logic_1(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [BinaryOp('and', BooleanLiteral(True), BooleanLiteral(True))])
            )
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_logic_2(self):
        input = Program([
            FuncDecl(Id("main"), [], 
                CallStmt(Id("writeBool"), [BinaryOp('and', BooleanLiteral(True), UnaryOp('not', BooleanLiteral(True)))])
            )
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_logic_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), BoolType(), None, BooleanLiteral(True)),
                VarDecl(Id("b"), BoolType(), None, BooleanLiteral(False)),
                CallStmt(Id("writeBool"), [BinaryOp('or', Id("a"), Id("b"))])
            ]))
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_local_assign_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
                VarDecl(Id("b"), BoolType(), None, BooleanLiteral(True)),
                VarDecl(Id("c"), StringType(), None, StringLiteral("Hello")),
                CallStmt(Id("writeNumber"), [Id("a")]),
                CallStmt(Id("writeBool"), [Id("b")]),
                CallStmt(Id("writeString"), [Id("c")])
            ]))
        ])
        expect = "1.0trueHello"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_array_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([3], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])),
                CallStmt(Id("writeNumber"), [ArrayCell(Id("a"), [NumberLiteral(1.0)])])
            ])
            )
        ])
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_array_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([3], StringType()), None, ArrayLiteral([StringLiteral("Hello"), StringLiteral("World"), StringLiteral("!")])),
                CallStmt(Id("writeString"), [ArrayCell(Id("a"), [NumberLiteral(2.0)])])
            ])
            )
        ])
        expect = "!"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_array_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([3], BoolType()), None, ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(True)])),
                CallStmt(Id("writeBool"), [ArrayCell(Id("a"), [NumberLiteral(0.0)])])
            ])
            )
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_array_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([3], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])),
                CallStmt(Id("writeNumber"), [ArrayCell(Id("a"), [BinaryOp('+', NumberLiteral(1.0), NumberLiteral(1.0))])])
            ])
            )
        ])
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_array_5(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([3], StringType()), None, ArrayLiteral([BinaryOp('...', StringLiteral("Hello"), StringLiteral("World")), StringLiteral("!")])),
                CallStmt(Id("writeString"), [ArrayCell(Id("a"), [BinaryOp('-', NumberLiteral(2.0), NumberLiteral(1.0))])])
            ])
            )
        ])
        expect = "!"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_array_6(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([2], BoolType()), None, ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])),
                Assign(ArrayCell(Id("a"), [NumberLiteral(1.0)]), BooleanLiteral(True),
                ),
                CallStmt(Id("writeBool"), [ArrayCell(Id("a"), [NumberLiteral(1.0)])])
            ])
            )
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_array_7(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([2], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)])),
                Assign(ArrayCell(Id("a"), [NumberLiteral(0.0)]), NumberLiteral(3.0),
                ),
                CallStmt(Id("writeNumber"), [ArrayCell(Id("a"), [NumberLiteral(0.0)])])
            ])
            )
        ])
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_array_8(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([2], StringType()), None, ArrayLiteral([StringLiteral("Hello"), StringLiteral("World")])),
                Assign(ArrayCell(Id("a"), [NumberLiteral(1.0)]), StringLiteral("!"),
                ),
                CallStmt(Id("writeString"), [ArrayCell(Id("a"), [NumberLiteral(1.0)])])
            ])
            )
        ])
        expect = "!"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_multilevel_array_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([2, 2], NumberType()), None, ArrayLiteral([
                    ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]),
                    ArrayLiteral([NumberLiteral(3.0), NumberLiteral(4.0)])
                ])),
                CallStmt(Id("writeNumber"), [ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(1.0)])])
            ])
            )
        ])
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_multilevel_array_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([2, 2], StringType()), None, ArrayLiteral([
                    ArrayLiteral([StringLiteral("Hello"), StringLiteral("World")]),
                    ArrayLiteral([StringLiteral("Hi"), StringLiteral("!")])
                ])),
                CallStmt(Id("writeString"), [ArrayCell(Id("a"), [NumberLiteral(0.0), NumberLiteral(1.0)])])
            ])
            )
        ])
        expect = "World"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_multilevel_array_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([2, 2], BoolType()), None, ArrayLiteral([
                    ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)]),
                    ArrayLiteral([BooleanLiteral(False), BooleanLiteral(True)])
                ])),
                CallStmt(Id("writeBool"), [ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(0.0)])])
            ])
            )
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_multilevel_array_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([2, 2], NumberType()), None, ArrayLiteral([
                    ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]),
                    ArrayLiteral([NumberLiteral(3.0), NumberLiteral(4.0)])
                ])),
                Assign(ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(1.0)]), NumberLiteral(5.0)),
                CallStmt(Id("writeNumber"), [ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(1.0)])])
            ])
            )
        ])
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_multilevel_array_5(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([2, 2], StringType()), None, ArrayLiteral([
                    ArrayLiteral([StringLiteral("Hello"), StringLiteral("World")]),
                    ArrayLiteral([StringLiteral("Hi"), StringLiteral("!")])
                ])),
                Assign(ArrayCell(Id("a"), [NumberLiteral(0.0), NumberLiteral(1.0)]), StringLiteral("!!!")),
                CallStmt(Id("writeString"), [ArrayCell(Id("a"), [NumberLiteral(0.0), NumberLiteral(1.0)])])
            ])
            )
        ])
        expect = "!!!"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_multilevel_array_6(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([2, 2], BoolType()), None, ArrayLiteral([
                    ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)]),
                    ArrayLiteral([BooleanLiteral(False), BooleanLiteral(True)])
                ])),
                Assign(ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(0.0)]), BooleanLiteral(True)),
                CallStmt(Id("writeBool"), [ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(0.0)])])
            ])
            )
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_multilevel_array_7(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([2, 2], NumberType()), None, ArrayLiteral([
                    ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]),
                    ArrayLiteral([NumberLiteral(3.0), NumberLiteral(4.0)])
                ])),
                Assign(ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(1.0)]), 
                       BinaryOp('+', 
                                ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(0.0)]), 
                                ArrayCell(Id("a"), [NumberLiteral(0.0), NumberLiteral(1.0)]))
                ),
                CallStmt(Id("writeNumber"), [ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(1.0)])])
            ])
            )
        ])
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_global_array_1(self):
        input = Program([
            VarDecl(Id("a"), ArrayType([2], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeNumber"), [ArrayCell(Id("a"), [NumberLiteral(1.0)])])
            ]))
        ])
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_global_array_2(self):
        input = Program([
            VarDecl(Id("a"), ArrayType([2], StringType()), None, ArrayLiteral([StringLiteral("Hello"), StringLiteral("World")])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeString"), [ArrayCell(Id("a"), [NumberLiteral(0.0)])])
            ]))
        ])
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_global_array_3(self):
        input = Program([
            VarDecl(Id("a"), ArrayType([2], BoolType()), None, ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeBool"), [ArrayCell(Id("a"), [NumberLiteral(1.0)])])
            ]))
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_global_multilevel_array_1(self):
        input = Program([
            VarDecl(Id("a"), ArrayType([2, 2], NumberType()), None, ArrayLiteral([
                ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]),
                ArrayLiteral([NumberLiteral(3.0), NumberLiteral(4.0)])
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeNumber"), [ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(1.0)])])
            ]))
        ])
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_global_multilevel_array_2(self):
        input = Program([
            VarDecl(Id("a"), ArrayType([2, 2], StringType()), None, ArrayLiteral([
                ArrayLiteral([StringLiteral("Hello"), StringLiteral("World")]),
                ArrayLiteral([StringLiteral("Hi"), StringLiteral("!")]
                )])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeString"), [ArrayCell(Id("a"), [NumberLiteral(0.0), NumberLiteral(1.0)])])
            ]))
        ])
        expect = "World"
        self.assertTrue(TestCodeGen.test(input, expect, 571))
        
    def test_dynamic_local_var_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic', NumberLiteral(1.0)),
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ])
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_dynamic_local_var_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic'),
                Assign(Id("a"), StringLiteral("Hello")),
                CallStmt(Id("writeString"), [Id("a")])
            ]))
        ])
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_dynamic_local_var_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic'),
                Assign(Id("a"), BooleanLiteral(True)),
                CallStmt(Id("writeBool"), [Id("a")])
            ]))
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_dynamic_local_var_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic'),
                VarDecl(Id("b"), None, 'dynamic'),
                Assign(Id("b"), BinaryOp('+', NumberLiteral(1.0), NumberLiteral(2.0))),
                Assign(Id("a"), NumberLiteral(1.0)),
                CallStmt(Id("writeNumber"), [Id("a")]),
                CallStmt(Id("writeNumber"), [Id("b")])
            ]))
        ])
        expect = "1.03.0"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_dynamic_local_var_5(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic'),
                VarDecl(Id("b"), None, 'dynamic'),
                Assign(Id("b"), StringLiteral("Hello")),
                Assign(Id("a"), StringLiteral("World")),
                CallStmt(Id("writeString"), [Id("a")]),
                CallStmt(Id("writeString"), [Id("b")])
            ]))
        ])
        expect = "WorldHello"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_dynamic_global_var_1(self):
        input = Program([
            VarDecl(Id("a"), None, 'dynamic', NumberLiteral(1.0)),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ])
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_dynamic_global_var_2(self):
        input = Program([
            VarDecl(Id("a"), None, 'dynamic'),
            FuncDecl(Id("main"), [], Block([
                Assign(Id("a"), StringLiteral("Hello")),
                CallStmt(Id("writeString"), [Id("a")])
            ]))
        ])
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_dynamic_global_var_3(self):
        input = Program([
            VarDecl(Id("a"), None, 'dynamic'),
            VarDecl(Id("b"), None, 'dynamic'),
            FuncDecl(Id("main"), [], Block([
                Assign(Id("a"), BooleanLiteral(True)),
                Assign(Id("b"), BooleanLiteral(False)),
                CallStmt(Id("writeBool"), [BinaryOp('or', Id("a"), Id("b"))])
            ]))
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 579))
    
    def test_dynamic_global_var_4(self):
        input = Program([
            VarDecl(Id("a"), None, 'dynamic'),
            VarDecl(Id("b"), None, 'dynamic'),
            FuncDecl(Id("main"), [], Block([
                Assign(Id("a"), NumberLiteral(1.0)),
                Assign(Id("b"), NumberLiteral(2.0)),
                CallStmt(Id("writeNumber"), [BinaryOp('+', Id("a"), Id("b"))])
            ]))
        ])
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_dynamic_global_var_5(self):
        input = Program([
            VarDecl(Id("a"), None, 'dynamic'),
            VarDecl(Id("b"), None, 'dynamic'),
            FuncDecl(Id("main"), [], Block([
                If(Id("a"), Block([
                    Assign(Id("a"), BinaryOp('>=' , Id("b"), NumberLiteral(1.0)))
                ])),
                CallStmt(Id("writeBool"), [Id("a")]),
                CallStmt(Id("writeNumber"), [Id("b")])
            ]))
        ])
        expect = "false0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_dynamic_global_var_6(self):
        input = Program([
            VarDecl(Id("a"), None, 'dynamic'),
            VarDecl(Id("b"), None, 'dynamic'),
            FuncDecl(Id("main"), [], Block([
                If(Id("a"), Block([
                    Assign(Id("a"), BinaryOp('>=' , Id("b"), NumberLiteral(1.0)))
                ]), [], Block([
                    Assign(Id("b"), NumberLiteral(1.0))
                ])),
                CallStmt(Id("writeBool"), [Id("a")]),
                CallStmt(Id("writeNumber"), [Id("b")])
            ]))
        ])
        expect = "false1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_dynamic_global_var_7(self):
        input = Program([
            VarDecl(Id("a"), None, 'dynamic'),
            VarDecl(Id("b"), None, 'dynamic'),
            FuncDecl(Id("main"), [], Block([
                For(Id("a"), BinaryOp('<', Id("a"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([
                    CallStmt(Id("writeNumber"), [Id("a")]),
                    CallStmt(Id("writeString"), [StringLiteral(" ")])
                ])),
            ]))
        ])
        expect = "0.0 1.0 2.0 3.0 4.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_dynamic_global_var_8(self):
        input = Program([
            VarDecl(Id("a"), None, 'dynamic'),
            VarDecl(Id("b"), None, 'dynamic'),
            FuncDecl(Id("main"), [], Block([
                For(Id("a"), BinaryOp('<', Id("a"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([
                    If(BinaryOp('=', Id("a"), NumberLiteral(2.0)), Block([
                        Continue()
                    ])),
                    CallStmt(Id("writeNumber"), [Id("a")]),
                    CallStmt(Id("writeString"), [StringLiteral(" ")])
                ])),
            ]))
        ])
        expect = "0.0 1.0 3.0 4.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_func_decl_1(self):
        input = Program([
            FuncDecl(Id("foo"), [], Block([
                CallStmt(Id("writeString"), [StringLiteral("Hello")])
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("foo"), [])
            ]))
        ])
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_func_decl_2(self):
        input = Program([
            FuncDecl(Id("foo"), [], Block([
                CallStmt(Id("writeNumber"), [NumberLiteral(1.0)])
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("foo"), [])
            ]))
        ])
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_func_decl_3(self):
        input = Program([
            FuncDecl(Id("foo"), [], Block([
                CallStmt(Id("writeBool"), [BooleanLiteral(True)])
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("foo"), [])
            ]))
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_func_decl_4(self):
        input = Program([
            VarDecl(Id("a"), StringType(), None, StringLiteral("World")),
            FuncDecl(Id("foo"), [], Block([
                Assign(Id("a"), StringLiteral("Hi")),
                CallStmt(Id("writeString"), [Id("a")])
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("foo"), []),
                CallStmt(Id("writeString"), [StringLiteral("World")])
            ]))
        ])
        expect = "HiWorld"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_func_decl_5(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            FuncDecl(Id("foo"), [VarDecl(Id("b"), NumberType())], Block([
                CallStmt(Id("writeNumber"), [BinaryOp('+', Id("a"), Id("b"))])
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("foo"), [Id("a")]),
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ])
        expect = "2.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_func_decl_6(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            FuncDecl(Id("foo"), [VarDecl(Id("b"), NumberType())], Block([
                Return(BinaryOp('+', Id("a"), Id("b")))
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeNumber"), [CallExpr(Id("foo"), [Id("a")])]),
            ]))
        ])
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_func_decl_7(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            FuncDecl(Id("foo"), [VarDecl(Id("b"), NumberType())], Block([
                Return(BinaryOp('+', Id("a"), Id("b")))
            ])),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("c"), NumberType(), None, CallExpr(Id("foo"), [Id("a")])),
                CallStmt(Id("writeNumber"), [Id("c")]),
            ]))
        ])
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_func_decl_8(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            FuncDecl(Id("foo"), [VarDecl(Id("b"), NumberType())]),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("c"), NumberType(), None, CallExpr(Id("foo"), [Id("a")])),
                CallStmt(Id("writeNumber"), [Id("c")]),
            ])),
            FuncDecl(Id("foo"), [VarDecl(Id("b"), NumberType())], Block([
                Return(BinaryOp('+', Id("a"), Id("b")))
            ])),
        ])
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_func_decl_9(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            FuncDecl(Id("foo"), [VarDecl(Id("b"), NumberType())], Block([
                Return(BinaryOp('+', Id("a"), Id("b")))
            ])),
            FuncDecl(Id("bar"), [VarDecl(Id("c"), NumberType())], Block([
                CallStmt(Id("writeNumber"), [CallExpr(Id("foo"), [Id("c")])])
            ])),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("c"), NumberType(), None, CallExpr(Id("foo"), [Id("a")])),
                CallStmt(Id("bar"), [Id("c")]),
            ])),
        ])
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_func_decl_10(self):
        input = Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            VarDecl(Id("b"), StringType(), None, StringLiteral("Hello World!")),
            FuncDecl(Id("foo"), [], Block([
                Return(BinaryOp('+', Id("a"), NumberLiteral(1.0)))
            ])),
            FuncDecl(Id("bar"), [VarDecl(Id("c"), NumberType())], Block([
                Return()
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("bar"), [Id("a")]),
                CallStmt(Id("writeNumber"), [CallExpr(Id("foo"), [])]),
            ])),
        ])
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_program_1(self):
        input = Program([
            FuncDecl(Id("getSecond"), [VarDecl(Id("a"), ArrayType([2], NumberType()))], Block([
                Return(ArrayCell(Id("a"), [NumberLiteral(1.0)]))
            ])),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("b"), ArrayType([2], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)])),
                CallStmt(Id("writeNumber"), [CallExpr(Id("getSecond"), [Id("b")])])
            ]))
        ])
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_program_2(self):
        input = Program([
            FuncDecl(Id("fibo"), [VarDecl(Id("n"), NumberType())], Block([
                VarDecl(Id("a"), NumberType(), None, NumberLiteral(0.0)),
                VarDecl(Id("b"), NumberType(), None, NumberLiteral(1.0)),
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(2.0)),
                For(Id("i"), BinaryOp('<=', Id("i"), Id("n")), NumberLiteral(1.0), Block([
                    VarDecl(Id("c"), NumberType(), None, BinaryOp('+', Id("a"), Id("b"))),
                    Assign(Id("a"), Id("b")),
                    Assign(Id("b"), Id("c")),
                ])),
                Return(Id("b"))
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeNumber"), [CallExpr(Id("fibo"), [NumberLiteral(10.0)])])
            ]))
        ])
        expect = "55.0"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_program_3(self):
        input = Program([
            FuncDecl(Id("factorial"), [VarDecl(Id("n"), NumberType())], Block([
                VarDecl(Id("result"), NumberType(), None, NumberLiteral(1.0)),
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(1.0)),
                For(Id("i"), BinaryOp('<=', Id("i"), Id("n")), NumberLiteral(1.0), Block([
                    Assign(Id("result"), BinaryOp('*', Id("result"), Id("i")))
                ])),
                Return(Id("result"))
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeNumber"), [CallExpr(Id("factorial"), [NumberLiteral(5.0)])])
            ]))
        ])
        expect = "120.0"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_program_4(self):
        input = Program([
            FuncDecl(Id("GCD"), [VarDecl(Id("a"), NumberType()), VarDecl(Id("b"), NumberType())], Block([
                VarDecl(Id("temp"), NumberType(), None, NumberLiteral(0.0)),
                For(Id("temp"), BinaryOp('!=', Id("a"), Id("b")), NumberLiteral(0.0), Block([
                    If (BinaryOp('>', Id("a"), Id("b")),
                        Assign(Id("a"), BinaryOp('-', Id("a"), Id("b"))) , [],
                        Assign(Id("b"), BinaryOp('-', Id("b"), Id("a")))
                    )
                ])),
                Return(Id("a"))
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeNumber"), [CallExpr(Id("GCD"), [NumberLiteral(24.0), NumberLiteral(36.0)])])
            ]))
        ])
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input, expect, 598))
    
    def test_program_5(self):
        input = Program([
            FuncDecl(Id("isPrime"), [VarDecl(Id("n"), NumberType())], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(2.0)),
                For(Id("i"), BinaryOp('<', Id("i"), Id("n")), NumberLiteral(1.0), Block([
                    If(BinaryOp('=', BinaryOp('%', Id("n"), Id("i")), NumberLiteral(0.0)), Block([
                        Return(BooleanLiteral(False))
                    ]))
                ])),
                Return(BooleanLiteral(True))
            ])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("writeBool"), [CallExpr(Id("isPrime"), [NumberLiteral(7.0)])])
            ]))
        ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 599))

