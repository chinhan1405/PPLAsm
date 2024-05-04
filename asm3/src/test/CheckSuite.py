import unittest
from TestUtils import TestChecker
from AST import *



class CheckerSuite(unittest.TestCase):
    def test_no_entry_point_1(self):
        input = Program([VarDecl(Id("a"), NumberType())])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_no_entry_point_2(self):
        input = Program([FuncDecl(Id("f"), [], Return()), VarDecl(Id("a"), NumberType())])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_no_entry_point_3(self):
        input = Program([FuncDecl(Id("mian"), [], Return())])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_operator_with_literal_1(self):
        input = BinaryOp("+", StringLiteral('sssss'), NumberLiteral(2.0))
        expect = "Type Mismatch In Expression: " +  str(input)
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_operator_with_literal_2(self):
        input = BinaryOp("-", BooleanLiteral(True), NumberLiteral(2.0))
        expect = "Type Mismatch In Expression: " +  str(input)
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_operator_with_literal_3(self):
        input = BinaryOp("...", BooleanLiteral(False), BooleanLiteral(True))
        expect = "Type Mismatch In Expression: " +  str(input)
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_operator_with_literal_4(self):
        input = BinaryOp("...", BooleanLiteral(False), StringLiteral('bbb'))
        expect = "Type Mismatch In Expression: " + str(input)
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_operator_with_literal_5(self):
        input = BinaryOp("==", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), StringLiteral('bbb'))
        expect = "Type Mismatch In Expression: " \
            + str(BinaryOp("==", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), StringLiteral('bbb')))

        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_operator_with_literal_6(self):
        input = BinaryOp("==", BinaryOp("+", NumberLiteral(1.0), BooleanLiteral(True)), StringLiteral('bbb'))
        expect = "Type Mismatch In Expression: " \
            + str(BinaryOp("+", NumberLiteral(1.0), BooleanLiteral(True)))
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_operator_with_literal_7(self):
        input = BinaryOp("!=",
                    UnaryOp("-", NumberLiteral(1.0)),
                    UnaryOp("not", NumberLiteral(2.0))
                )
        expect = "Type Mismatch In Expression: " \
            + str(UnaryOp("not", NumberLiteral(2.0)))
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_type_mismatch_in_vardecl_1(self):
        input = VarDecl(Id("a"), NumberLiteral(1.0), None, StringLiteral("abc"))
        expect = "Type Mismatch In Statement: " + str(input)
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_type_mismatch_in_vardecl_2(self):
        input = VarDecl(Id("a"), None, 'var', None)
        expect = "Type Mismatch In Statement: " + str(input)
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_type_mismatch_in_vardecl_3(self):
        input = VarDecl(Id("a"), StringType(), None, NumberLiteral(1.0))
        expect = "Type Mismatch In Statement: " + str(input)
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_redeclared_1(self):
        input = Program([VarDecl(Id("a"), NumberType()), VarDecl(Id("a"), StringType())])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_redeclared_2(self):
        input = Program([VarDecl(Id("a"), NumberType()), VarDecl(Id("a"), NumberType())])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test_redeclared_3(self):
        input = Program([FuncDecl(Id("f"), [], Return()), FuncDecl(Id("f"), [], Return())])
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_redeclared_4(self):
        input = Program([FuncDecl(Id("f"), [], None), 
                        VarDecl(Id("f"), NumberType())])
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_redeclared_5(self):
        input = Program([FuncDecl(Id("a"), [VarDecl(Id("v"), NumberType()), VarDecl(Id("v"), StringType())], Return())])
        expect = "Redeclared Parameter: v"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_redeclared_6(self):
        input = Program([
            FuncDecl(Id("f1"), [
                VarDecl(Id("v"), NumberType()),
                VarDecl(Id("v"), NumberType())
            ], Block(
                [
                    VarDecl(Id("v"), StringType()),
                    VarDecl(Id("a"), StringType())
                ]
            )),
        ])
        expect = "Redeclared Parameter: v"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_redeclared_7(self):
        input = Program([
            FuncDecl(Id("f1"), [
                VarDecl(Id("v"), NumberType())
            ], Block([VarDecl(Id("v"), StringType()),
                      VarDecl(Id("v"), StringType())])),
        ])
        expect = "Redeclared Variable: v"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_undeclared_1(self):
        input = Program([
            VarDecl(Id("a"), NumberType()),
            FuncDecl(Id("main"), [],
                VarDecl(Id("b"), NumberType(), None, Id("c")))
            ])
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_undeclared_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, CallExpr(Id("f"), [])),
            ]))
        ])
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_undeclared_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, CallExpr(Id("f"), [])),
                CallExpr(Id("f"), [])
            ]))
        ])
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_undeclared_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType()),
                CallStmt(Id("f"), [])
            ])),
            FuncDecl(Id("f"), [], None)
        ])
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_type_mismatch_in_expr_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, UnaryOp("-", NumberLiteral(1.0))),
                VarDecl(Id("b"), BoolType(), None, BinaryOp("and", Id("a"), BooleanLiteral(True)))
            ]))
        ])
        expect = "Type Mismatch In Expression: " + str(BinaryOp("and", Id("a"), BooleanLiteral(True)))
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_type_mismatch_in_expr_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, UnaryOp("-", NumberLiteral(1.0))),
                VarDecl(Id("b"), BoolType(), None, BinaryOp("and", Id("a"), Id("a")))
            ]))
        ])
        expect = "Type Mismatch In Expression: " + str(BinaryOp("and", Id("a"), Id("a")))
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_type_mismatch_in_expr_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, UnaryOp("-", NumberLiteral(1.0))),
                VarDecl(Id("b"), BoolType(), None, ArrayCell(Id("a"), [NumberLiteral(1.0)]))
            ]))
        ])
        expect = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"), [NumberLiteral(1.0)]))
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_type_mismatch_in_expr_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, UnaryOp("-", NumberLiteral(1.0))),
                VarDecl(Id("b"), BoolType(), None, ArrayCell(Id("a"), [Id("a")]))
            ]))
        ])
        expect = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"), [Id("a")]))
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_type_mismatch_in_expr_5(self):
        input = Program([
            FuncDecl(Id("f"),[VarDecl(Id("b"), StringType())], Return(NumberLiteral(1.0))),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, None),
                VarDecl(Id("b"), BoolType(), None, CallExpr(Id("f"), []))            
                ]))
        ])
        expect = "Type Mismatch In Expression: " + str(CallExpr(Id("f"), []))
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_expr_6(self):
        input = Program([
            FuncDecl(Id("f"),[VarDecl(Id("b"), StringType())], Return(NumberLiteral(1.0))),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, None),
                VarDecl(Id("b"), BoolType(), None, CallExpr(Id("f"), [Id("a")]))            
                ]))
        ])
        expect = "Type Mismatch In Expression: " + str(CallExpr(Id("f"), [Id("a")]))
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_no_definition_function_1(self):
        input = Program([
            FuncDecl(Id("f"), [], None),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("f"), []),
            ]))
        ])
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_no_definition_function_2(self):
        input = Program([
            FuncDecl(Id("f"), [], None),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("f"), []),
            ])),
            FuncDecl(Id("g"), [], None)
        ])
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_no_definition_function_3(self):
        # TODO check this test case
        input = Program([
            FuncDecl(Id("f"), [], None),
            FuncDecl(Id("g"), [], None),
            FuncDecl(Id("f"), [], Return()),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("f"), []),
            ]))
        ])
        expect = "No Function Definition: g"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_if_stmt_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                If(StringLiteral("True"), Return())
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(If(StringLiteral("True"), Return()))
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_if_stmt_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                If(BooleanLiteral(False), Return(), [(StringLiteral("True"), Return())])
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(If(BooleanLiteral(False), Return(), [(StringLiteral("True"), Return())]))
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_if_stmt_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                If(BooleanLiteral(False), Return(), 
                   [(BooleanLiteral(True), Return()),
                    (NumberLiteral(0.2), Return())])
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(If(BooleanLiteral(False), Return(), 
                   [(BooleanLiteral(True), Return()),
                    (NumberLiteral(0.2), Return())]))
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test_if_stmt_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                If(NumberLiteral(0), Return(), [], Return(NumberLiteral(1.0)))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(If(NumberLiteral(0), Return(), [], Return(NumberLiteral(1.0))))
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_for_stmt_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                For(Id("i"), NumberLiteral(0.1), NumberLiteral(1.0), Return())
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(For(Id("i"), NumberLiteral(0.1), NumberLiteral(1.0), Return()))
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_for_stmt_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                For(Id("i"), StringLiteral("sss"), NumberLiteral(1.0), Return())
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(For(Id("i"), StringLiteral("sss"), NumberLiteral(1.0), Return()))
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_for_break(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                Break()
            ]))
        ])
        expect = str(Break()) + " Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_for_continue(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                Continue()
            ]))
        ])
        expect = str(Continue()) + " Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_block_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, None),
                VarDecl(Id("b"), NumberType(), None, None),
                VarDecl(Id("a"), NumberType(), None, None),
            ]))
        ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_block_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, None),
                VarDecl(Id("b"), NumberType(), None, None),
                VarDecl(Id("c"), NumberType(), None, None),
                Block([
                    VarDecl(Id("a"), NumberType(), None, None),
                    VarDecl(Id("b"), NumberType(), None, None),
                    VarDecl(Id("c"), NumberType(), None, None),
                    VarDecl(Id("c"), NumberType(), None, None),
                ])
            ]))
        ])
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_block_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, None),
                VarDecl(Id("b"), NumberType(), None, None),
                VarDecl(Id("c"), NumberType(), None, None),
                Block([
                    VarDecl(Id("a"), NumberType(), None, None),
                    VarDecl(Id("b"), NumberType(), None, None),
                    Block([
                        VarDecl(Id("c"), NumberType(), None, None),
                        VarDecl(Id("c"), NumberType(), None, None),
                    ])
                ])
            ]))
        ])
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_block_4(self):
        input = Program([
            FuncDecl(Id("f"), [VarDecl(Id("a"), NumberType())],
                Block([
                    VarDecl(Id("a"), NumberType(), None, None),
                    VarDecl(Id("c"), NumberType(), None, None),
                    Block([
                        VarDecl(Id("c"), StringType(), None, None),
                    ]),
                    VarDecl(Id("a"), NumberType(), None, None),
                ])),
            FuncDecl(Id("main"), [], Return())
        ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_block_5(self):
        input = Program([
            FuncDecl(Id("f"), [VarDecl(Id("a"), NumberType())],
                Block([
                    VarDecl(Id("f"), NumberType(), None, None),
                    Block([
                        VarDecl(Id("f"), StringType(), None, None),
                    ]),
                    VarDecl(Id("a"), NumberType(), None, None),
                    VarDecl(Id("a"), NumberType(), None, None),
                ])),
            FuncDecl(Id("main"), [], Return())
        ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_type_mismatch_in_stmt_1(self):
        input = Program([
            FuncDecl(Id("f"), [], Return()),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("f"), [NumberLiteral(1.0)])
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(CallStmt(Id("f"), [NumberLiteral(1.0)]))
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_type_mismatch_in_stmt_2(self):
        input = Program([
            FuncDecl(Id("f"), [VarDecl(Id("a"), StringType())], Return()),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("f"), [NumberLiteral(1.0)])
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(CallStmt(Id("f"), [NumberLiteral(1.0)]))
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_type_mismatch_in_stmt_3(self):
        input = Program([
            FuncDecl(Id("f"), [VarDecl(Id("a"), StringType())], Return()),
            FuncDecl(Id("g"), [VarDecl(Id("a"), NumberType())], Return()),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'var', NumberLiteral(2.0)),
                CallStmt(Id("g"), [])
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(CallStmt(Id("g"), []))
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_type_mismatch_in_stmt_4(self):
        input = Program([
            FuncDecl(Id("f"), [VarDecl(Id("a"), StringType())], Return()),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'var', NumberLiteral(2.0)),
                CallStmt(Id("f"), [NumberLiteral(1.0), Id("a")])
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(CallStmt(Id("f"), [NumberLiteral(1.0), Id("a")]))
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_return_1(self):
        input = Program([
            FuncDecl(Id("f"), [], None),
            FuncDecl(Id("main"), [], Block([
                If(CallExpr(Id("f"), []), VarDecl(Id("a"), NumberType(), None, None))
            ])),
            FuncDecl(Id("f"), [], Return(NumberLiteral(1.0)))
        ])
        expect = "Type Mismatch In Statement: " + str(Return(NumberLiteral(1.0)))
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_return_2(self):
        input = Program([
            FuncDecl(Id("f"), [], Return(NumberLiteral(1.0))),
            FuncDecl(Id("main"), [], Block([
                If(CallExpr(Id("f"), []), VarDecl(Id("a"), NumberType(), None, None))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(If(CallExpr(Id("f"), []), VarDecl(Id("a"), NumberType(), None, None)))
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_return_3(self):
        input = Program([
            FuncDecl(Id("f"), [], None),
            FuncDecl(Id("main"), [], Block([
                If(CallExpr(Id("f"), []), VarDecl(Id("a"), NumberType(), None, None))
            ])),
            FuncDecl(Id("f"), [], Return(NumberLiteral(1.0)))
        ])
        expect = "Type Mismatch In Statement: " + str(Return(NumberLiteral(1.0)))
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_assign_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                Assign(Id("a"), NumberLiteral(1.0))
            ]))
        ])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_assign_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, None),
                Assign(Id("a"), StringLiteral("abc"))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(Assign(Id("a"), StringLiteral("abc")))
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_assign_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, None),
                VarDecl(Id("b"), StringType(), None, StringLiteral("abc")),
                Assign(Id("a"), Id("b"))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(Assign(Id("a"), Id("b")))
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_assign_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, None),
                VarDecl(Id("b"), StringType(), None, StringLiteral("abc")),
                Assign(Id("a"), BinaryOp("+", Id("b"), NumberLiteral(1.0)))
            ]))
        ])
        expect = "Type Mismatch In Expression: " + str(BinaryOp("+", Id("b"), NumberLiteral(1.0)))
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_assign_5(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic', None),
                VarDecl(Id("b"), None, 'dynamic', None),
                Assign(Id("a"), Id("b"))
            ]))
        ])
        expect = "Type Cannot Be Inferred: " + str(Assign(Id("a"), Id("b")))
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_assign_6(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic', None),
                VarDecl(Id("b"), None, 'dynamic', None),
                Assign(Id("a"), NumberLiteral(1.0)),
                Assign(Id("b"), Id("a")),
                If(Id("b"), VarDecl(Id("a"), NumberType(), None, None))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(If(Id("b"), VarDecl(Id("a"), NumberType(), None, None)))
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_assign_7(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic', None),
                VarDecl(Id("b"), None, 'dynamic', None),
                Assign(Id("a"), NumberLiteral(1.0)),
                Assign(Id("a"), Id("b")),
                If(Id("b"), VarDecl(Id("a"), StringType(), None, None))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(If(Id("b"), VarDecl(Id("a"), StringType(), None, None)))
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_assign_8(self):
        input = Program([
            FuncDecl(Id("f"), [VarDecl(Id("a"), StringType())], Return(NumberLiteral(1.0))),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, "dynamic", StringLiteral("abc")),
                Assign(Id("a"), CallExpr(Id("f"), [Id("a")]))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(Assign(Id("a"), CallExpr(Id("f"), [Id("a")])))
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_component_infer_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic', None),
                VarDecl(Id("b"), None, 'dynamic', None),
                Assign(Id("b"), ArrayLiteral([Id("a")]))
            ]))
        ])
        expect = "Type Cannot Be Inferred: " + str(Assign(Id("b"), ArrayLiteral([Id("a")])))
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_component_infer_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic', None),
                Assign(Id("a"), ArrayLiteral([Id("a")]))
            ]))
        ])
        expect = "Type Cannot Be Inferred: " + str(Assign(Id("a"), ArrayLiteral([Id("a")])))
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_redeclared_non_body_function(self):
        input = Program([
            FuncDecl(Id("f"), [], None),
            FuncDecl(Id("f"), [], None),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("f"), [])
            ])),
            FuncDecl(Id("f"), [], None)

        ])
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_redeclared_parameter_with_function(self):
        input = Program([
            FuncDecl(Id("f"), [VarDecl(Id("a"), NumberType()),
                               VarDecl(Id("b"), StringType())], None),
            FuncDecl(Id("f"), [VarDecl(Id("a"), NumberType()),
                               VarDecl(Id("a"), NumberType())], Return()),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("f"), [Id("a")])
            ]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_reverse_function_definition(self):
        input = Program([
            FuncDecl(Id("f"), [], Return()),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("f"), [])
            ])),
            FuncDecl(Id("f"), [], None)
        ])
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_main_inference(self):
        input = Program([
            FuncDecl(Id("main"), [], None),
            FuncDecl(Id("f"), [], Block([
                VarDecl(Id("a"), NumberType(), None, CallExpr(Id("main"), [])),
            ])),
            FuncDecl(Id("main"), [], Return())
        ])
        expect = "Type Mismatch In Statement: " + str(Return())
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_function_inference(self):
        input = Program([
            FuncDecl(Id("f1"), [], None),
            FuncDecl(Id("main"), [], VarDecl(Id("a"), NumberType(), None, CallExpr(Id("f1"), []))),
            FuncDecl(Id("f2"), [], None),
            FuncDecl(Id("f1"), [], VarDecl(Id("b"), None, 'var', CallExpr(Id("f2"), []))),
            FuncDecl(Id("f2"), [], Return(NumberLiteral(1.0)))
        ])
        expect = "Type Cannot Be Inferred: " + str(VarDecl(Id("b"), None, 'var', CallExpr(Id("f2"), [])))
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_array_literal_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic', ArrayLiteral([NumberLiteral(1.0), StringLiteral("abc")]))
            ]))
        ])
        expect = "Type Mismatch In Expression: " + str(ArrayLiteral([NumberLiteral(1.0), StringLiteral("abc")]))
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_array_literal_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic', ArrayLiteral([
                    ArrayLiteral([NumberLiteral(1.0), StringLiteral("abc")]),
                    ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)])]))
            ]))
        ])
        expect = "Type Mismatch In Expression: " + str(ArrayLiteral([NumberLiteral(1.0), StringLiteral("abc")]))
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_array_literal_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic', ArrayLiteral([
                    ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]),
                    ArrayLiteral([NumberLiteral(1.0), NumberLiteral(3.0)])])),
                VarDecl(Id("b"), NumberType(), None, ArrayCell(Id("a"), [NumberLiteral(1.0)]))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("b"), NumberType(), None, ArrayCell(Id("a"), [NumberLiteral(1.0)])))
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_function_overload(self):
        input = Program([
            FuncDecl(Id("f"), [VarDecl(Id("a"), NumberType())]),
            FuncDecl(Id("f"), [VarDecl(Id("a"), StringType())]),
        ])
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_function_overload_2(self):
        input = Program([
            FuncDecl(Id("f"), [VarDecl(Id("a"), NumberType())]),
            FuncDecl(Id("f"), [VarDecl(Id("a"), NumberType())]),
        ])
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_function_overload_3(self):
        input = Program([
            FuncDecl(Id("f"), [VarDecl(Id("a"), StringType())]),
            FuncDecl(Id("f"), [VarDecl(Id("a"), NumberType()),
                               VarDecl(Id("b"), StringType())], Return(Id("a"))),
        ])
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_array_cell(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic'),
                VarDecl(Id("b"), None, 'var', ArrayCell(Id("a"), [NumberLiteral(0.0)]))
            ]))
        ])
        expect = "Type Cannot Be Inferred: " + str(VarDecl(Id("b"), None, 'var', ArrayCell(Id("a"), [NumberLiteral(0.0)])))
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_array_declaration(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("arr"), ArrayType([2.0, 3.0], StringType()), None, 
                        ArrayLiteral([StringLiteral("abc"), StringLiteral("def"), StringLiteral("ghi")]))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("arr"), ArrayType([2.0, 3.0], StringType()), None, 
                        ArrayLiteral([StringLiteral("abc"), StringLiteral("def"), StringLiteral("ghi")])))
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_array_declaration_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("arr"), ArrayType([2.0, 3.0], StringType()), None, 
                        ArrayLiteral([StringLiteral("abc"), StringLiteral("def")]))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("arr"), ArrayType([2.0, 3.0], StringType()), None, 
                        ArrayLiteral([StringLiteral("abc"), StringLiteral("def")])))
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_array_declaration_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("arr"), ArrayType([2.0, 3.0], StringType()), None, 
                        ArrayLiteral([
                            ArrayLiteral([StringLiteral("abc"), StringLiteral("def")]),
                            ArrayLiteral([StringLiteral("abc"), StringLiteral("def")]),
                        ]))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("arr"), ArrayType([2.0, 3.0], StringType()), None, 
                        ArrayLiteral([
                            ArrayLiteral([StringLiteral("abc"), StringLiteral("def")]),
                            ArrayLiteral([StringLiteral("abc"), StringLiteral("def")]),
                        ])))
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_array_declaration_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("arr"), ArrayType([2.0, 3.0], StringType()), None, 
                        ArrayLiteral([
                            ArrayLiteral([StringLiteral("abc"), StringLiteral("def")]),
                            ArrayLiteral([StringLiteral("abc"), NumberLiteral(1.0)]),
                        ]))
            ]))
        ])
        expect = "Type Mismatch In Expression: " + str(ArrayLiteral([StringLiteral("abc"), NumberLiteral(1.0)]))
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_array_declaration_5(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("arr"), ArrayType([2.0], StringType()), None, 
                        ArrayLiteral([
                            ArrayLiteral([StringLiteral("abc"), StringLiteral("def")]),
                            ArrayLiteral([StringLiteral("abc"), StringLiteral("def")]),
                        ]))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("arr"), ArrayType([2.0], StringType()), None, 
                        ArrayLiteral([
                            ArrayLiteral([StringLiteral("abc"), StringLiteral("def")]),
                            ArrayLiteral([StringLiteral("abc"), StringLiteral("def")]),
                        ])))
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_builtin_function(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic')
            ])),
            FuncDecl(Id("readBool"), [], Return(BooleanLiteral(True)))
        ])
        expect = "Redeclared Function: readBool"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_builtin_function_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic')
            ])),
            FuncDecl(Id("writeString"), [], Return())
        ])
        expect = "Redeclared Function: writeString"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_builtin_function_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic', CallExpr(Id("readNumber"), [])),
                VarDecl(Id("b"), None, 'var', CallExpr(Id("readString"), [])),
                Assign(Id("a"), Id("b"))
            ])),
        ])
        expect = "Type Mismatch In Statement: " + str(Assign(Id("a"), Id("b")))
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_function_reference(self):
        input = Program([
            FuncDecl(Id("f"), [], Return()),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, 'dynamic', Id("f"))
            ]))
        ])
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_for_statement_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                For(Id("i"), NumberLiteral(1.0), NumberLiteral(10.0), Return())
            ]))
        ])
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_for_statement_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                For(Id("i"), NumberLiteral(1.0), NumberLiteral(10.0), Return())
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(For(Id("i"), NumberLiteral(1.0), NumberLiteral(10.0), Return()))
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_for_statement_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                VarDecl(Id("j"), NumberType(), None, NumberLiteral(1)),
                For(Id("i"), BinaryOp('<', Id('i'), Id('j')), NumberLiteral(1.0), 
                    Block([
                        VarDecl(Id("i"), StringType(), None, NumberLiteral(0))
                    ])
                )
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("i"), StringType(), None, NumberLiteral(0)))
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_for_statement_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                VarDecl(Id("j"), NumberType(), None, NumberLiteral(1)),
                For(Id("i"), BinaryOp('<', Id('i'), Id('j')), NumberLiteral(1.0), 
                    Block([
                        Assign(Id('j'), NumberLiteral(10)),
                        VarDecl(Id("i"), StringType(), None, NumberLiteral(0))
                    ])
                )
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("i"), StringType(), None, NumberLiteral(0)))
        self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test_if_statement_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                If(UnaryOp('-', Id("i")), Return())
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(If(UnaryOp('-', Id("i")), Return()))
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_if_statement_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                If(BinaryOp('>', Id("i"), NumberLiteral(0)), Return()),
                VarDecl(Id("j"), StringType(), None, NumberLiteral(0))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("j"), StringType(), None, NumberLiteral(0)))
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_if_statement_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                If(BooleanLiteral(True), Return()),
                VarDecl(Id("j"), StringType(), None, NumberLiteral(0))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("j"), StringType(), None, NumberLiteral(0)))
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_if_statement_4(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                If(BooleanLiteral(True), Return(), [(BooleanLiteral(True), Return())]),
                VarDecl(Id("j"), StringType(), None, NumberLiteral(0))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("j"), StringType(), None, NumberLiteral(0)))
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_if_statement_5(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                If(BooleanLiteral(True), Return(), [(BooleanLiteral(True), Return())], Return()),
                VarDecl(Id("j"), StringType(), None, NumberLiteral(0))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("j"), StringType(), None, NumberLiteral(0)))
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_if_statement_6(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0)),
                If(BooleanLiteral(True), Return(BooleanLiteral(True)), [(BooleanLiteral(True), Return(BooleanLiteral(True)))], Return(BooleanLiteral(True)))
            ]))
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_assign_9(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, NumberLiteral(0)),
                Assign(Id("a"), NumberLiteral(1.0)),
                Assign(Id("a"), StringLiteral("abc"))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(Assign(Id("a"), StringLiteral("abc")))
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_assign_10(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, NumberLiteral(0)),
                Block([
                    VarDecl(Id("a"), StringType(), None, StringLiteral("sfsfs")),
                    Assign(Id("a"), BinaryOp('+', NumberLiteral(1.0), NumberLiteral(1.0)))
                ])
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(Assign(Id("a"), BinaryOp('+', NumberLiteral(1.0), NumberLiteral(1.0))))
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_array_cell_2(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([1.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0)])),
                VarDecl(Id("b"), NumberType(), None, ArrayCell(Id("a"), [StringLiteral("abc")]))
            ]))
        ])
        expect = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"), [StringLiteral("abc")]))
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_array_cell_3(self):
        input = Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), ArrayType([1.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0)])),
                VarDecl(Id("b"), NumberType(), None, ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(1.0)]))
            ]))
        ])
        expect = "Type Mismatch In Statement: " + str(VarDecl(Id("b"), NumberType(), None, ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(1.0)])))
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_main_function_1(self):
        input = Program([
            FuncDecl(Id("main"), [], Return(StringLiteral("abc")))
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_main_function_2(self):
        input = Program([
            FuncDecl(Id("main"), [VarDecl(Id("s"), NumberType())], Block([
                VarDecl(Id("a"), NumberType(), None, NumberLiteral(0))
            ]))
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 499))
