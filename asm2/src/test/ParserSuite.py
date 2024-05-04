import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program_1(self):
        """Simple program"""
        input = """func main () return 1+1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))

    def test_simple_program_2(self):
        """Simple program"""
        input = """
            func main () return 1+1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_var_declaration_1(self):
        """Var declaration"""
        input = """
            number a <- 1+1
            func main () return a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_var_declaration_2(self):
        """Var declaration"""
        input = """
            string a <- "hello"
            func main () return a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_var_declaration_3(self):
        """Var declaration"""
        input = """
            bool a <- True
            bool b <- False
            func main () return a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_var_declaration_4(self):
        """Var declaration"""
        input = """
            number abc <- True
            bool b <- 123.456
            func main () return a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_var_declaration_5(self):
        """Var declaration"""
        input = """
            var abc <- True
            bool cde <- true
            func main () return abc
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_var_declaration_6(self):
        """Var declaration"""
        input = """
            var abc <-
            bool cde <- true
            func main () return abc
        """
        expect = "Error on line 2 col 23: \n"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_var_declaration_7(self):
        """Var declaration"""
        input = """
            dynamic abc
            bool cde <- true
            func main () return cde
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_string_literal_1(self):
        """String literal"""
        input = """
            string abc <- "Hello world"
            func main () return abc
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_string_literal_2(self):
        """String literal"""
        input = """
            string abc <- "Hello world
            func main () return abc
        """
        expect = """Hello world

            func main () return abc

        """
        self.assertTrue(TestParser.test(input,expect,210))

    def test_error_token_1(self):
        """Error token"""
        input = """
            string abc <- @aab
            func main () return abc
        """
        expect = "@"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_error_token_2(self):
        """Error token"""
        input = """
            number abc <- !!
            func main () return abc
        """
        expect = "!"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_function_declaration_1(self):
        """Function declaration"""
        input = """
            func isPrime(number n) return True
            func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_function_declaration_2(self):
        """Function declaration"""
        input = """
            func isPrime(number n)
            func main () return 1

            func isPrime(number n) return True
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_function_declaration_3(self):
        """Function declaration"""
        input = """
            func isPrime(number n) return True
            func sum(number a, number b) return 1+1
            func main () return 1

            func isPrime(number n) return True
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_function_declaration_4(self):
        """Function declaration"""
        input = """
            func isPrime(number n) return True
            func sum(number a, number b) return 1+1
            func sum
            func main () return 1
            func sum(number a, number b) return 1+1
            func isPrime(number n) return True
        """
        expect = """Error on line 4 col 21: \n"""
        self.assertTrue(TestParser.test(input,expect,216))

    def test_variable_and_function_declaration_1(self):
        """Variable and function declaration"""
        input = """
            number a <- 1
            func a() return 1
            func main () return a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_variable_and_function_declaration_2(self):
        """Variable and function declaration"""
        input = """
            string b <- "hello"
            func a()
            func main () return a
            func a() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_variable_and_function_declaration_3(self):
        """Variable and function declaration"""
        input = """
            bool c <- True
            func a(number e, string d)
            func main () return a
            func a(number e, string d) return c+d*3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_expression_1(self):
        """Expression"""
        input = """
            func main () return 1+2+3+4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_expression_2(self):
        """Expression"""
        input = """
            func main () return 1+2*3+4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_expression_3(self):
        """Expression"""
        input = """
            func main () return 1+-2*3+4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_expression_4(self):
        """Expression"""
        input = """
            func main () return true and false
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_expression_5(self):
        """Expression"""
        input = """
            func main () return true and falsetrue
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_expression_6(self):
        """Expression"""
        input = """
            func main () return 123.456 * 456.2e12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_expression_7(self):
        """Expression"""
        input = """
            func main () return 123.456 * ( 456.2e12 + 3)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_expression_8(self):
        """Expression"""
        input = """
            func main () return not true and false or true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_expression_9(self):
        """Expression"""
        input = """
            func main () return a - - - c
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_expression_10(self):
        """Expression"""
        input = """
            func main () return a + + + c
        """
        expect = "Error on line 2 col 36: +"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_expression_11(self):
        """Expression"""
        input = """
            func main () return not isPrime(123+456)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_expression_12(self):
        """Expression"""
        input = """
            func main () return not isPrime(123+456) and isNegative(-123--135)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_expression_13(self):
        """Expression"""
        input = """
            func main () return true or isPositive("hello"..." world")
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_expression_14(self):
        """Expression"""
        input = """
            func main () return - + 3 * 5
        """
        expect = "Error on line 2 col 34: +"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_expression_15(self):
        """Expression"""
        input = """
            func main () return thisIsAFunction(3, 5, a--5)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_expression_16(self):
        """Expression"""
        input = """
            number a[6] <- [1, 2, 3, 4, 5, 6]
            func main () return a[1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_expression_17(self):
        """Expression"""
        input = """
            number a[6,7,6,5] <- [1, 2, 3, 4, 5, 6]
            func main () return a[1+2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    
    def test_expression_18(self):
        """Expression"""
        input = """
            number a[6] <- [1, 2, 3, 4, 5, 6]
            func main () return a[1+a[1]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_expression_19(self):
        """Expression"""
        input = """
            number a[6] <- [1, 2, 3, 4, 5, 6]
            func main () return a[1+a[a[3]]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_expression_20(self):
        """Expression"""
        input = """
            number a[6] <- [1, 2, 3, 4, 5, 6]
            func main () return a[a[6]+a[a[3]]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))


    def test_expression_21(self):
        """Expression"""
        input = """
            var b <- 7
            number a[6] <- [1, 2, 3, 4, 5, 6]
            func main () return a[b+a[a[3]]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_expression_22(self):
        """Expression"""
        input = """
            var b <- "hello"
            number a[6] <- [1, 2, 3, 4, 5, 6]
            func main () return a[b]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_expression_23(self):
        """Expression"""
        input = """
            var b <- "hello"
            number a[6] <- [1, 2, 3, 4, 5, 6]
            func main () return a[b+a]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_expression_24(self):
        """Expression"""
        input = """
            number a[6] <- [1, 2, 3, 4, 5, 6]
            number c[4] <- [1, 2, 3, 4]
            func main () return a[a[1]---c[2]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_expression_25(self):
        """Expression"""
        input = """
            number a[6] <- [1, 2, 3, 4, 5, 6]
            number c[4] <- [1, 2, 3, 4]
            func main () return a[c[a[c[a[c[a[c[a[1]]]]]]]]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_expression_26(self):
        """Expression"""
        input = """
            number a[6] <- [1, 2, 3, 4, 5, 6]
            number c[4] <- [1, 2, 3, 4]
            func main () return a[1] + c[a[1] * 2 / c[1+a[3]]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_expression_27(self):
        """Expression"""
        input = """
            string a <- "hello"
            string b <- "world"
            func main () return a...b...a
        """
        expect = "Error on line 4 col 37: ..."
        self.assertTrue(TestParser.test(input,expect,246))

    def test_expression_28(self):
        """Expression"""
        input = """
            string a <- "hello"
            string b <- "world"
            string c <- a...b
            func main () return c==a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_expression_29(self):
        """Expression"""
        input = """
            bool a <- True
            bool b <- False
            bool c <- not a
            bool d <- a and c
            bool e <- b or d
            bool f <- not e or d
            func main () return f
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_expression_30(self):
        """Expression"""
        input = """
            bool a <- True
            bool b <- not not not not not not a
            
            func main () return b
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_assignment_1(self):
        """Assignment"""
        input = """
            func main () 
            begin
                number a
                a <- 2
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_assignment_2(self):
        """Assignment"""
        input = """
            func main () 
            begin
                number a <- 2
                a <- 3 + 5 
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_assignment_3(self):
        """Assignment"""
        input = """
            func main () 
            begin
                number a <- 2
                number b <- 3
                b <- 12.3
                a <- 3 + 5 
                a <- a * b
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_if_statement_1(self):
        """If statement"""
        input = """
            func main () 
            begin
                number a <- 2
                if (a > 0) a <- 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_if_statement_2(self):
        """If statement"""
        input = """
            func main () 
            begin
                number a <- 2
                if (a > 0) 
                    a <- 1
                else a <- 0
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_if_statement_3(self):
        """If statement"""
        input = """
            func main () 
            begin
                number a <- 2
                if (a > 0) 
                    a <- 1
                elif (a == 0) 
                    a <- 2
                elif (a < 0)
                    a <- 3
                else a <- 0
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_for_statement_1(self):
        """For statement"""
        input = """
            func main () 
            begin
                number a
                for a until a < 10 by 1
                begin
                    number b <- 1
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_for_statement_2(self):
        """For statement"""
        input = """
            func main () 
            begin
                number a
                for a until a < 10 by 1
                begin
                    number b <- 1
                    for b until b < 10 by 1
                    begin
                        number c <- 1
                    end
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_for_statement_3(self):
        """For statement"""
        input = """
            func main () 
            begin
                number a
                for a until a < 10 by 1
                begin
                    number b <- 1
                    for b until b < 10 by 1
                    begin
                        number c <- 1
                        for c until c < 10 by 1
                        begin
                            number d <- 1
                        end
                    end
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_for_statement_4(self):
        """For statement"""
        input = """
            func main () 
            begin
                number a
                for a until a < 10 by 1 var b <- "hello world"
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_break_statement(self):
        """Break statement"""
        input = """
            func main () 
            begin
                number a
                for a until a < 10 by 1
                begin
                    number b <- 1
                    for b until b < 10 by 1
                    begin
                        number c <- 1
                        for c until c < 10 by 1
                        begin
                            number d <- 1
                            break
                        end
                    end
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_continue_statement(self):
        """Continue statement"""
        input = """
            func main () 
            begin
                number a
                for a until a < 10 by 1
                begin
                    number b <- 1
                    if (b == 1) continue
                    for b until b < 10 by 1
                    begin
                        number c <- 1
                        for c until c < 10 by 1
                        begin
                            number d <- 1
                            continue
                        end
                    end
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_return_statement_1(self):
        """Return statement"""
        input = """
            func sum(number a, number b) return a+b
            func main () return sum(1, 2)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_return_statement_2(self):
        """Return statement"""
        input = """
            func val(number a) return a
            func sum(number a, number b) return val(a) + val(b)
            func main () return sum(1, 2)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))

    def test_function_call_statement_1(self):
        """Function call statement"""
        input = """
            number s <- 0
            func sum() 
            begin
                s <- s+1
            end
            func main () 
            begin
                sum()
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

    def test_function_call_statement_2(self):
        """Function call statement"""
        input = """
            number s <- 0
            string str <- "hello"
            func sum(string a) 
            begin
                str <- str...a
            end
            func main () 
            begin
                sum("world")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

    def test_block_statement_1(self):
        """Block statement"""
        input = """
            func main () 
            begin


                number a

                a <- 1
                begin
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

    def test_block_statement_2(self):
        """Block statement"""
        input = """
            func main () 
            begin number a
                a <- 1
                begin
                    number b
                    b <- 2
                end
            end
        """
        expect = "Error on line 3 col 18: number"
        self.assertTrue(TestParser.test(input,expect,267))

    def test_block_statement_3(self):
        """Block statement"""
        input = """
            func main () 
            begin 
                number a
                a <- 1
                begin
                    number b
                    b <- 2
                end begin
                    number c
                    c <- 3
                end
            end
        """
        expect = "Error on line 9 col 20: begin"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_newline_separator(self):
        """Newline separator"""
        input = """
            func main () 


            begin 
                number a
                
            a <- 1

                        number b
        b <- 2

                number c
    c <- 3
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_program_1(self):
        """Program"""
        input = """
            func main () 
            begin 
                number a
                a <- 1
                begin
                    number b
                    b <- 2
                end
                begin
                    number c
                    c <- 3
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_program_2(self):
        """Program"""
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
                begin
                    var num1 <- readNumber()
                    var num2 <- readNumber()
                    if (areDivisors(num1, num2)) printString("Yes")
                    else printString("No")
                end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))

    def test_program_3(self):
        """Program"""
        input = """
            func isPrime(number x)
            func main()
            begin
                number x <- readNumber()
                if (isPrime(x)) printString("Yes")
                else printString("No")
            end
            func isPrime(number x)
            begin
                if (x <= 1) return false
                    var i <- 2
                for i until i > x / 2 by 1
                begin
                    if (x % i = 0) return false
                end
                return true
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_program_4(self):
        """Program"""
        input = """
            func main()
            begin
                var n <- readNumber()
                var i <- 1
                var sum <- 0
                for i until i <= n by 1
                begin
                    sum <- sum + i
                    i <- i + 1
                end
                printNumber(sum)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_program_5(self):
        """Program"""
        input = """
            func isPrime(number x)
            begin
                if (x <= 1) return false
                    var i <- 2
                for i until i > x / 2 by 1
                begin
                    if (x % i = 0) return false
                end
                return true
            end
            func main()
            begin
                writeString("Hello world")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_program_6(self):
        """Program"""
        input = """
            func main()
            begin
                var n <- readNumber()
                var i <- 1
                var sum <- 0
                for i until i <= n by 1
                begin
                    sum <- sum + i
                    i <- i + 1
                end
                printNumber(sum)
            end
            func isPrime(number x)
            begin
                if (x <= 1) return false
                    var i <- 2
                for i until i > x / 2 by 1
                begin
                    if (x % i = 0) return false
                end
                return true
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_program_7(self):
        """Program"""
        input = """
            func isNegative(number x) return x < 0
            func main()
            begin
                var x <- readNumber()
                if (isNegative(x)) printString("Yes")
                else printString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_program_8(self):
        """Program"""
        input = """
            func fibonacci(number n)
            begin
                if (n <= 1) return n
                return fibonacci(n - 1) + fibonacci(n - 2)
            end
            func main()
            begin
                var n <- readNumber()
                var i <- 0
                for i until i < n by 1
                begin
                    printNumber(fibonacci(i))
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))

    def test_program_9(self):
        """Program"""
        input = """
            func concatString(string a, string b) return a...b
            func main()
            begin
                string a <- readString()
                string b <- readString()
                printString(concatString(a, b))
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def test_program_10(self):
        """Program"""
        input = """
            number t <- 0
            func inc(number x)
            func main()
            begin
                number x <- readNumber()
                inc(x)
                printNumber(t)
            end
            func inc(number x) 
            begin
                t <- t + x
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))

    def test_program_11(self):
        """Program"""
        input = """
            ## This is a helper function
            func power(number x, number y)
            begin
                var res <- 1
                var i <- 0
                for i until i < y by 1
                begin
                    res <- res * x
                end
                return res
            end

            ## This is the main function
            func main()
            begin
                var x <- readNumber()
                var y <- readNumber()
                printNumber(power(x, y))
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_program_12(self):
        """Program"""
        input = """
            func main()
            begin
                var n <- readNumber()
                var i <- 1
                var sum <- 0
                for i until i <= n by 1
                begin
                    sum <- sum + i
                    i <- i + 1
                end
                printNumber(sum)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_program_13(self):
        """Program"""
        input = """
            func sqrt(number x)
            begin
                var res <- 1
                for res until res * res > x by 1
                return (res-1)
            end
            func main()
            begin
                var a <- readNumber()
                printNumber(sqrt(a))
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_program_14(self):
        """Program"""
        input = """
            func toString(number x)
            begin
                var res <- ""
                var i <- 0
                for i until i < x by 1
                begin
                    res <- res...i
                end
                return res
            end
            func main()
            begin
                var a <- readNumber()
                printString(toString(a))
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_program_15(self):
        """Program"""
        input = """
            func main()
            begin
                ## This program do nothing
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_program_16(self):
        """Program"""
        input = """
            func main()
            begin
                ## This program do nothing
                ## This program do nothing
                ## This program do nothing
                aFunctionHere()
            end

            func aFunctionHere()
            begin
                var this_Function <- "do nothing"
                ## Main function can not call this function
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_program_17(self):
        """Program"""
        input = """
            func func1() return 1
            func func2() return func1()
            func func3() return func2()
            func func4() return func3()
            func main()
            begin
                printNumber(func4())
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_program_18(self):
        """Program"""
        input = """
            number a
            func readArray(number a[10], number n)
            begin
                var i <- 0
                for i until i < n by 1
                begin
                    a[i] <- readNumber()
                end
            end
            func main()
            begin
                readArray(a, 10)
                var i <- 0
                for i until i < 10 by 1
                    printNumber(a[i])
            end       """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test_program_19(self):
        """Program"""
        input = """
            func main()
            begin
                var a <- readNumber()
                var b <- readNumber()
                var c <- readNumber()
                number c[3]
                c[0] <- a
                c[1] <- b
                c[2] <- c
                printNumber(c[c[c[1]]])
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_program_20(self):
        """Program"""
        input = """
            func main()
            begin
                number a[3] <- [1, 2, 3]
                printNumber(a[0])
                printNumber(a[1])
                printNumber(a[2])
                printNumber(a)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))

    def test_program_21(self):
        """Program"""
        input = """
            func main()
            begin
                print a
            end
        """
        expect = "Error on line 4 col 22: a"
        self.assertTrue(TestParser.test(input,expect,290))

    def test_program_22(self):
        """Program"""
        input = """
            func something()
            begin
                printNumber(a)
            end
        """
        expect = "successful" 
        self.assertTrue(TestParser.test(input,expect,291))

    def test_program_23(self):
        """Program"""
        input = """
            func main()
            begin
                                    printNumber         (a)
            end
                                    func something         ()
            begin
                                    printNumber      (     a     )
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def test_program_24(self):
        """Program"""
        input = """
            func main()
            begin
                printNumber(
                    a
                    )
            end
            func something(
            
            )
            begin
                printNumber(
                    a)
            end
        """
        expect = "Error on line 4 col 29: \n"
        self.assertTrue(TestParser.test(input,expect,293))

    def test_program_25(self):
        """Program"""
        input = """
        ## Literally do nothing here
            func main() begin 
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_program_26(self):
        """Program"""
        input = """
            ## Literally do nothing here
            func main() 
            begin 
                begin
                    begin
                begin
            begin
                begin
                    end
                        begin
                            end
                                begin
                                    end
            end
                end
                    end
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def test_program_27(self):
        """Program"""
        input = """
            var a <- 1
            var b <- 2
            func main()
            begin
                printNumber(a)
                printNumber(b)
                printNumber(a+b)
                printNumber(a-b)
                printNumber(a*b)
                printNumber(a/b)
                printNumber(a%b)
                printNumber(a------------------------------------------------b)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_multinewline(self):
        """Multinewline"""
        input = """
            func main()
            begin
              
            


            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_array_1(self):
        """Array"""
        input = """
            func main()
            begin
                number b <- 4
                number a[3] <- [1, b, 3]
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_array_2(self):
        """Array"""
        input = """
            func main()
            begin
                number a[3] <- [1, 2, 3]
                number b[2, 4] <- [[1, 2, 3, 4], [5, 6, 7, 8]]
                b[2-1, 3] <- b[b[1, 2], 3] + 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))