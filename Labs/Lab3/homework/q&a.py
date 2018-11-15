1, Why should we use function?
    - we can reuse function
    - Easy to control your code. If you fix bug you just need fix only 1 time

2, How to define a function?
    Step 1: Declare the function with the keyword def followed by the function name.
    Step 2: Write the arguments inside the opening and closing parentheses of the function, and end the declaration with a colon.
    Step 3: Add the program statements to be executed.
    Step 4: End the function with/without return statement.

3, How to call, use a function?
        from #file contained the function# import #function#
        #function(variables)#

4, What is return? How and why we use it?
    The return statement causes your function to exit and hand back a value to its caller. 
    The point of functions in general is to take in inputs and return something. 
    The return statement is used when a function is ready to return a value to its caller.

    Example:
    def foo():
        print("hello from inside of foo")
        return 1

5, Do we have to use return in every functions?
    - No. We only use return if we need the outputs.

6, What are function arguments/parameters? How and why we use it?
    - Parameters are the names used when defining a function or a method, and into which 
    arguments will be mapped. 
    
    When you define a function you need transmission a arguement
    When you want to call this function you need transmission a parameter match with argument

7, How to use function from a different file other than our currently working file?
    - Refered in Q3