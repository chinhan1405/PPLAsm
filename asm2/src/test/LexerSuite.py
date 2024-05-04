import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_empty(self):
        """test empty string"""
        self.assertTrue(TestLexer.test('','<EOF>',100))

    def test_simple_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.test("##this is comment","<EOF>",101))

    def test_comment_with_more_dsharp(self):
        """test complex comment"""
        self.assertTrue(TestLexer.test("##this is comment##","<EOF>",102))

    def test_comment_with_more_dsharp_and_space(self):
        """test complex comment"""
        self.assertTrue(TestLexer.test("##this is comment## ","<EOF>",103))

    def test_comment_with_more_dsharp_and_space_and_newline(self):
        """test complex comment"""
        self.assertTrue(TestLexer.test("##this is comment## \n","<EOF>",104))
    
    def test_comment_with_escape_character(self):
        """test complex comment"""
        self.assertTrue(TestLexer.test("##this is comment## \t\\\n","<EOF>",105))

    def test_type(self):
        """test type"""
        self.assertTrue(TestLexer.test("number boolean string var dynamic","number,boolean,string,var,dynamic,<EOF>",106))

    def test_keyword(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("if else for until break continue return","if,else,for,until,break,continue,return,<EOF>",107))
    
    def test_operator(self):
        """test operator"""
        self.assertTrue(TestLexer.test("== != < > <= >= + - * / and or not = ... <-","==,!=,<,>,<=,>=,+,-,*,/,and,or,not,=,...,<-,<EOF>",108))

    def test_seperator(self):
        """test seperator"""
        self.assertTrue(TestLexer.test("( ) [ ] ,","(,),[,],,,<EOF>",109))

    def test_newline(self):
        """test newline"""
        input = """##this is comment##
        
            """
        output = """\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,110))

    def test_newline_with_comment(self):
        """test newline"""
        input = """##this is comment## 
        
            ##this is comment##
            """
        output = """\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,111))

    def test_identifier(self):
        """test identifier"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",112))

    def test_identifier_with_number(self):
        """test identifier"""
        self.assertTrue(TestLexer.test("abc123","abc123,<EOF>",113))

    def test_identifier_with_number_and_underscore(self):
        """test identifier"""
        self.assertTrue(TestLexer.test("abc_123","abc_123,<EOF>",114))
    
    def test_complex_identifier(self):
        """test identifier"""
        self.assertTrue(TestLexer.test("aBc_123_aBBc","aBc_123_aBBc,<EOF>",115))

    def test_keyword_in_identifier(self):
        """test identifier"""
        self.assertTrue(TestLexer.test("ifabc","ifabc,<EOF>",116))

    def test_identifier_with_keyword(self):
        """test identifier"""
        self.assertTrue(TestLexer.test("abc if else","abc,if,else,<EOF>",117))

    def test_wrong_identifier(self):
        """test wrong identifier"""
        self.assertTrue(TestLexer.test("abc@bb","abc,Error Token @",118))

    def test_wrong_identifier_with_number(self):
        """test wrong identifier"""
        self.assertTrue(TestLexer.test("abc123@bb","abc123,Error Token @",119))

    def test_wrong_identifier_with_number_and_underscore(self):
        """test wrong identifier"""
        self.assertTrue(TestLexer.test("abc_123@bb","abc_123,Error Token @",120))

    def test_wrong_complex_identifier(self):
        """test wrong identifier"""
        self.assertTrue(TestLexer.test("aBc_123_aBBc@bb","aBc_123_aBBc,Error Token @",121))

    def test_wrong_keyword_in_identifier(self):
        """test wrong identifier"""
        self.assertTrue(TestLexer.test("ifabc@bb","ifabc,Error Token @",122))

    def test_wrong_identifier_with_keyword(self):
        """test wrong identifier"""
        self.assertTrue(TestLexer.test("abc if else!bb","abc,if,else,Error Token !",123))

    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test('"abc"','abc,<EOF>',124))

    def test_string_with_quote(self):
        """test string with quote"""
        self.assertTrue(TestLexer.test('"isn\'t"','isn\'t,<EOF>',125))

    def test_string_with_escape_character(self):
        """test string with escape character"""
        self.assertTrue(TestLexer.test('"abc\\n"','abc\\n,<EOF>',126))

    def test_string_with_double_quote(self):
        """test string with double quote"""
        self.assertTrue(TestLexer.test('"abc\'"abc"','abc\'"abc,<EOF>',127))

    def test_string_with_double_quote_and_escape_character(self):
        """test string with double quote and escape character"""
        self.assertTrue(TestLexer.test('"abc\'"abc\\n"','abc\'"abc\\n,<EOF>',128))

    def test_string_with_double_quote_and_escape_character_and_space(self):
        """test string with double quote and escape character and space"""
        self.assertTrue(TestLexer.test('"abc\'"abc\\n"  "abc\'"abc\\n"','abc\'"abc\\n,abc\'"abc\\n,<EOF>',129))

    def test_unclosed_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test('"abc','Unclosed String: abc',130))

    def test_unclosed_string_with_escape_character(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test('"abc\\n','Unclosed String: abc\\n',131))

    def test_unclosed_string_with_escape_character_and_space(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test('"abc\\n  ','Unclosed String: abc\\n  ',132))

    def test_illegal_escape_in_string(self):
        """test illegal escape in string"""
        input = """ "This is an illegal escape \k" """
        output = """Illegal Escape In String: This is an illegal escape \k"""
        self.assertTrue(TestLexer.test(input,output,133))

    def test_illegal_escape_in_string_with_escape_character(self):
        """test illegal escape in string"""
        self.assertTrue(TestLexer.test('"abc\\\\ \\a"','Illegal Escape In String: abc\\\\ \\a',134))

    def test_illegal_escape_stop(self):
        """test illegal escape stop"""
        self.assertTrue(TestLexer.test('"abc\\m sdfsadfas "','Illegal Escape In String: abc\\m',135))

    def test_boolean(self):
        """test boolean"""
        self.assertTrue(TestLexer.test("true false","true,false,<EOF>",136))

    def test_simple_number(self):
        """test simple number"""
        self.assertTrue(TestLexer.test("123 123.123 123.","123,123.123,123.,<EOF>",137))

    def test_scientific_number(self):
        """test scientific number"""
        self.assertTrue(TestLexer.test("123e-123 123.123e123","123e-123,123.123e123,<EOF>",138))

    def test_scientific_number_with_space(self):
        """test scientific number"""
        self.assertTrue(TestLexer.test("123e-123 123.123 e123 ","123e-123,123.123,e123,<EOF>",139))

    def test_scientific_number_with_space_and_newline(self):
        """test scientific number"""
        input = """123e-123 
        123.123 
        e123 
        """
        self.assertTrue(TestLexer.test(input,"123e-123,\n,123.123,\n,e123,\n,<EOF>",140))

    def test_array(self):
        """test array"""
        self.assertTrue(TestLexer.test("[1,2,3]","[,1,,,2,,,3,],<EOF>",141))

    def test_array_with_space(self):
        """test array"""
        self.assertTrue(TestLexer.test("[1, 2, 3]","[,1,,,2,,,3,],<EOF>",142))

    def test_string_array(self):
        """test string array"""
        self.assertTrue(TestLexer.test('["abc","def","ghi"]','[,abc,,,def,,,ghi,],<EOF>',143))

    def test_string_array_with_space(self):
        """test string array"""
        self.assertTrue(TestLexer.test('["abc", "def", "ghi"]','[,abc,,,def,,,ghi,],<EOF>',144))

    def test_array_with_array(self):
        """test array with array"""
        self.assertTrue(TestLexer.test("[[1,2],[3,4]]","[,[,1,,,2,],,,[,3,,,4,],],<EOF>",145))

    def test_array_with_complex_string(self):
        """test array with complex string"""
        self.assertTrue(TestLexer.test('["ab\\nc","de\\tf","g  hi"]','[,ab\\nc,,,de\\tf,,,g  hi,],<EOF>',146))

    def test_array_of_illegal_escaped_string(self):
        """test array of illegal escaped string"""
        self.assertTrue(TestLexer.test('["ab\\nc","de\\tf","g  hi\\m"]','[,ab\\nc,,,de\\tf,,,Illegal Escape In String: g  hi\\m',147))

    def test_array_of_float(self):
        """test array of float"""
        self.assertTrue(TestLexer.test("[1.1,2.2,3.3]","[,1.1,,,2.2,,,3.3,],<EOF>",148))

    def test_array_of_scientific_number(self):
        """test array of scientific number"""
        self.assertTrue(TestLexer.test("[1e-1,2e-2,3e+3]","[,1e-1,,,2e-2,,,3e+3,],<EOF>",149))

    def test_array_of_boolean(self):
        """test array of boolean"""
        self.assertTrue(TestLexer.test("[true,false,true]","[,true,,,false,,,true,],<EOF>",150))

    def test_string_of_literal(self):
        """test string of literal"""
        self.assertTrue(TestLexer.test('"123e13 12.5 true" ',"123e13 12.5 true,<EOF>",151))

    def test_string_of_literal_with_escape_character(self):
        """test string of literal"""
        self.assertTrue(TestLexer.test('"123e13 12.5 true\\n" ',"123e13 12.5 true\\n,<EOF>",152))

    def test_error_token_1(self):
        """test error token"""
        self.assertTrue(TestLexer.test("ab?svn","ab,Error Token ?",153))

    def test_error_token_2(self):
        """test error token"""
        self.assertTrue(TestLexer.test("absvn#","absvn,Error Token #",154))

    def test_error_token_3(self):
        """test error token"""
        self.assertTrue(TestLexer.test("abs&^%vn","abs,Error Token &",155))

    def test_error_token_4(self):
        """test error token"""
        self.assertTrue(TestLexer.test("abs\\  vn","abs,Error Token \\",156))

    def test_incorrect_identifier(self):
        """test incorrect identifier"""
        self.assertTrue(TestLexer.test("a!!_bc","a,Error Token !",157))

    def test_illegal_escape_complex(self):
        """test illegal escape complex"""
        input = """ "This is an illegal escape \l\m\c\k\\\\" """
        output = """Illegal Escape In String: This is an illegal escape \l"""
        self.assertTrue(TestLexer.test(input,output,158))

    def test_unclosed_string_complex(self):
        """test unclosed string complex"""
        input = """ "This is an unclosed string \\\\ """
        output = """Unclosed String: This is an unclosed string \\\\ """
        self.assertTrue(TestLexer.test(input,output,159))
    
    def test_statement_1(self):
        """test statement 1"""
        self.assertTrue(TestLexer.test("a = 1","a,=,1,<EOF>",160))

    def test_statement_2(self):
        """test statement 2"""
        self.assertTrue(TestLexer.test("a = 1 + 2","a,=,1,+,2,<EOF>",161))

    def test_statement_3(self):
        """test statement 3"""
        self.assertTrue(TestLexer.test("a = 1 + 2 * 3","a,=,1,+,2,*,3,<EOF>",162))
    
    def test_statement_4(self):
        """test statement 4"""
        self.assertTrue(TestLexer.test("a = 1 + 2 * 3 / 4","a,=,1,+,2,*,3,/,4,<EOF>",163))

    def test_statement_5(self):
        """test statement 5"""
        self.assertTrue(TestLexer.test("a = 1 + 2 * 3 / 4 - 5","a,=,1,+,2,*,3,/,4,-,5,<EOF>",164))

    def test_statement_6(self):
        """test statement 6"""
        self.assertTrue(TestLexer.test("var a <- 2", "var,a,<-,2,<EOF>",165))

    def test_statement_7(self):
        """test statement 7"""
        self.assertTrue(TestLexer.test("var a <- 2 + 3", "var,a,<-,2,+,3,<EOF>",166))

    def test_statement_8(self):
        """test statement 8"""
        self.assertTrue(TestLexer.test("dynamic a <- 2 + 3 * 4", "dynamic,a,<-,2,+,3,*,4,<EOF>",167))

    def test_function(self):
        """test function"""
        self.assertTrue(TestLexer.test("func foo(number a[5], string b)","func,foo,(,number,a,[,5,],,,string,b,),<EOF>",168))

    def test_function_with_space(self):
        """test function"""
        self.assertTrue(TestLexer.test("func foo ( number a [ 5 ] , string b )","func,foo,(,number,a,[,5,],,,string,b,),<EOF>",169))

    def test_loop_1(self):
        """test loop 1"""
        self.assertTrue(TestLexer.test("for i until i >= 5 by 1","for,i,until,i,>=,5,by,1,<EOF>",170))

    def test_loop_2(self):
        """test loop 2"""
        self.assertTrue(TestLexer.test("for j until j = 100 by 5","for,j,until,j,=,100,by,5,<EOF>",171))

    def test_assignment(self):
        """test assignment"""
        self.assertTrue(TestLexer.test("a[i] <- i * i + 5","a,[,i,],<-,i,*,i,+,5,<EOF>",172))

    def test_unary_operator(self):
        """test unary operator"""
        self.assertTrue(TestLexer.test("a <- -5","a,<-,-,5,<EOF>",173))

    def test_unary_operator_with_space(self):
        """test unary operator"""
        self.assertTrue(TestLexer.test("a <- - 5","a,<-,-,5,<EOF>",174))

    def test_return_statement_1(self):
        """test return statement 1"""
        self.assertTrue(TestLexer.test("return 5","return,5,<EOF>",175))

    def test_return_statement_2(self):
        """test return statement 2"""
        self.assertTrue(TestLexer.test("return 5 + 6","return,5,+,6,<EOF>",176))

    def test_return_statement_3(self):
        """test return statement 3"""
        self.assertTrue(TestLexer.test("return sum","return,sum,<EOF>",177))

    def test_code_block_1(self):
        """test code block 1"""
        input = """
            begin
            var i <- 0
            for i until i >= 5 by 1
            return -1
            end"""
        output = """\n,begin,\n,var,i,<-,0,\n,for,i,until,i,>=,5,by,1,\n,return,-,1,\n,end,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,178))

    def test_code_block_2(self):
        """test code block 2"""
        input = """
            begin
            var i <- 0
            for i until i >= 5 by 1
            return -1
            end
        """
        output = """\n,begin,\n,var,i,<-,0,\n,for,i,until,i,>=,5,by,1,\n,return,-,1,\n,end,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,179))

    def test_function_declaration(self):
        """test function declaration"""
        input = """func foo(number a[5], string b)
            begin
                return 1
            end"""
        output = """func,foo,(,number,a,[,5,],,,string,b,),\n,begin,\n,return,1,\n,end,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,180))

    def test_function_declaration_with_space(self):
        """test function declaration"""
        input = """func foo ( number a [ 5 ] , string b )
            begin
                return 1
            end"""
        output = """func,foo,(,number,a,[,5,],,,string,b,),\n,begin,\n,return,1,\n,end,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,181))
    
    def test_main_function(self):
        """test main function"""
        input = """func main()
            begin
                return 1
            end"""
        output = """func,main,(,),\n,begin,\n,return,1,\n,end,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,182))

    def test_main_function_with_space(self):
        """test main function"""
        input = """func main ( )
            begin
                return 1
            end"""
        output = """func,main,(,),\n,begin,\n,return,1,\n,end,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,183))

    def test_function_defination(self):
        """test function defination"""
        input = """func isPrime(number x)
        """
        output = """func,isPrime,(,number,x,),\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,184))

    def test_function_implementation(self):
        """test function implementation"""
        input = """func isPrime(number x)
                begin
                    if (x <= 1) return false
                    
                    return true
                end"""
        output = """func,isPrime,(,number,x,),\n,begin,\n,if,(,x,<=,1,),return,false,\n,\n,return,true,\n,end,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,185))

    def test_function_call(self):
        """test function call"""
        input = """number x <- readNumber()"""
        output = """number,x,<-,readNumber,(,),<EOF>"""
        self.assertTrue(TestLexer.test(input,output,186))

    def test_function_call_with_space(self):
        """test function call"""
        input = """number x <- readNumber ( )"""
        output = """number,x,<-,readNumber,(,),<EOF>"""
        self.assertTrue(TestLexer.test(input,output,187))

    def test_function_call_with_argument(self):
        """test function call"""
        input = """number x <- isPrime(5)"""
        output = """number,x,<-,isPrime,(,5,),<EOF>"""
        self.assertTrue(TestLexer.test(input,output,188))

    def test_condition_statement(self):
        """test condition statement"""
        input = """if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
                """
        output = """if,(,areDivisors,(,num1,,,num2,),),printString,(,Yes,),\n,else,printString,(,No,),\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,189))

    def test_array_element(self):
        """test array element"""
        input = """number a[5] <- [1,2,3,4,5]"""
        output = """number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],<EOF>"""
        self.assertTrue(TestLexer.test(input,output,190))

    def test_array_element_with_space(self):
        """test array element"""
        input = """number a [ 5 ] <- [ 1 , 2 , 3 , 4 , 5 ]"""
        output = """number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],<EOF>"""
        self.assertTrue(TestLexer.test(input,output,191))

    def test_array_element_with_variable(self):
        """test array element"""
        input = """number a[5] <- [1,2,3,4,5]
                    number b <- a[2]"""
        output = """number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],\n,number,b,<-,a,[,2,],<EOF>"""
        self.assertTrue(TestLexer.test(input,output,192))

    def test_array_element_with_variable_and_space(self):
        """test array element"""
        input = """number a [ 5 ] <- [ 1 , 2 , 3 , 4 , 5 ]
                    number b <- a [ 2 ]"""
        output = """number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],\n,number,b,<-,a,[,2,],<EOF>"""
        self.assertTrue(TestLexer.test(input,output,193))

    def test_expression_1(self):
        """test expression 1"""
        input = """a = 1 + 2 * 3 / 4 - 5"""
        output = """a,=,1,+,2,*,3,/,4,-,5,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,194))

    def test_expression_2(self):
        """test expression 2"""
        input = """12 - -3 * (3 + 3 - 2) / 4 + 6"""
        output = """12,-,-,3,*,(,3,+,3,-,2,),/,4,+,6,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,195))

    def test_expression_3(self):
        """test expression 3"""
        input = """a = b + c * d - epsilon"""
        output = """a,=,b,+,c,*,d,-,epsilon,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,196))

    def test_expression_4(self):
        """test expression 4"""
        input = """a = b + c * d - epsilon + -1"""
        output = """a,=,b,+,c,*,d,-,epsilon,+,-,1,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,197))

    def test_expression_5(self):
        """test expression 5"""
        input = """true = false and false"""
        output = """true,=,false,and,false,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,198))

    def test_expression_6(self):
        """test expression 6"""
        input = """sum(a,b) = one * two"""
        output = """sum,(,a,,,b,),=,one,*,two,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,199))
