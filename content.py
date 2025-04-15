# content.py

# Using a list of dictionaries for modules
# Each module has a list of lessons
# Each lesson can have 'type': 'explanation', 'quiz', 'code'

LESSON_CONTENT = [
    {
        "id": "mod_basics",
        "title": "Module 1: Python Basics",
        "lessons": [
            {
                "id": "l1_intro",
                "title": "Introduction to Python",
                "type": "explanation",
                "text": [
                    "Welcome to Interactive Python Learner!",
                    "Python is a high-level, interpreted, general-purpose programming language.",
                    "It emphasizes code readability with its notable use of significant indentation.",
                    "Let's start with the very basics."
                ]
            },
            {
                "id": "l1_print",
                "title": "The print() Function",
                "type": "explanation",
                "text": [
                    "The `print()` function is used to display output to the terminal.",
                    "You pass the value you want to print inside the parentheses `()`.",
                    "Text values (strings) should be enclosed in single ('') or double (\"\") quotes."
                ],
                "example": "print(\"Hello, World!\")" # Rich can syntax-highlight this
            },
            {
                "id": "l1_print_quiz",
                "title": "Quiz: print()",
                "type": "quiz",
                "question": "Which command correctly prints the text 'Python is fun'?",
                "options": [
                    "print Python is fun",
                    "print('Python is fun')",
                    "echo \"Python is fun\"",
                    "display('Python is fun')"
                ],
                "correct_answer": 1 # Index of the correct option (0-based)
            },
            {
                "id": "l1_print_challenge",
                "title": "Code: Print Your Name",
                "type": "code",
                "explanation": [
                    "Let's practice using the `print()` function.",
                    "Remember to enclose text (strings) in quotes."
                ],
                "challenge": [
                    "Write a single line of Python code that prints the exact text:",
                    "My name is Alex"
                ],
                "expected_stdout": "My name is Alex\n" # Exact output expected, including newline
            },
            {
                "id": "l1_comments",
                "title": "Comments in Python",
                "type": "explanation",
                "text": [
                    "Comments are notes in your code that are ignored by the Python interpreter.",
                    "They are used to explain code, make notes, or temporarily disable lines.",
                    "In Python, a single-line comment starts with the hash symbol `#`.",
                    "Everything after the `#` on that line is ignored."
                ],
                "example": "# This is a comment explaining the next line\nprint(\"Hello!\") # This comment is after the code\n\n# print(\"This line is commented out and won't run\")"
            }
        ]
    },
    {
        "id": "mod_variables",
        "title": "Module 2: Variables and Data Types",
        "lessons": [
            {
                "id": "l2_variables",
                "title": "Variables",
                "type": "explanation",
                "text": [
                    "Variables are used to store data.",
                    "Think of them as labels or names for values.",
                    "You assign a value to a variable using the equals sign `=`."
                ],
                "example": "message = \"Hello there\"\nprint(message)\n\nnumber = 10\nprint(number)"
            },
            {
                 "id": "l2_types",
                 "title": "Basic Data Types",
                 "type": "explanation",
                 "text": [
                    "Python has several built-in data types. The most common basic ones are:",
                    "  - `int`: Integers (whole numbers), e.g., `10`, `-5`, `0`",
                    "  - `float`: Floating-point numbers (decimals), e.g., `3.14`, `-0.5`",
                    "  - `str`: Strings (sequences of characters), e.g., `'Hello'`, `\"Python\"`",
                    "  - `bool`: Booleans (True or False)"
                 ],
                 "example": "age = 30         # int\nprice = 19.99    # float\nname = \"Alice\"     # str\nis_active = True # bool\n\nprint(type(age))\nprint(type(price))\nprint(type(name))\nprint(type(is_active))"
            },
            {
                "id": "l2_var_quiz",
                "title": "Quiz: Variables",
                "type": "quiz",
                "question": "What will be printed by the following code?\n\nx = 5\ny = ' apples'\nprint(str(x) + y)",
                "options": [
                    "5 apples",
                    "x apples",
                    "5y",
                    "Error"
                ],
                "correct_answer": 0
            },
            {
                "id": "l2_var_assign_challenge",
                "title": "Code: Assign and Print",
                "type": "code",
                "explanation": [
                    "Variables store data. You assign data using `=`.",
                    "You can then print the value stored in a variable."
                ],
                "challenge": [
                    "1. Create a variable named `city` and assign it the string value \"London\".",
                    "2. On the next line, print the value stored in the `city` variable."
                ],
                "expected_stdout": "London\n"
            },
             {
                "id": "l2_arithmetic_challenge",
                "title": "Code: Simple Arithmetic",
                "type": "code",
                "explanation": [
                    "You can perform calculations directly within the `print()` function or store results in variables.",
                    "Common arithmetic operators are `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division)."
                ],
                "challenge": [
                    "Write Python code that calculates `5` multiplied by `3`, and then prints the result."
                ],
                "expected_stdout": "15\n"
            },
            {
                "id": "l2_var_swap_challenge", 
                "title": "Code: Variable Swap",
                "type": "code",
                "explanation": [
                    "A common task is swapping the values held by two variables.",
                    "Python offers a concise way to do this using tuple packing and unpacking."
                ],
                "challenge": [
                    "1. Assign the value `10` to a variable named `a`.",
                    "2. Assign the value `20` to a variable named `b`.",
                    "3. Write one line of Python code to swap the values of `a` and `b` using tuple assignment.",
                    "4. Print the value of `a`.",
                    "5. Print the value of `b` (on a new line)."
                ],
                "expected_stdout": "20\n10\n"
            },
            {
                 "id": "l2_type_conversion",
                 "title": "Type Conversion",
                 "type": "explanation",
                 "text": [
                    "Sometimes you need to convert data from one type to another.",
                    "For example, the `input()` function always gives you a string, even if the user types numbers.",
                    "To perform math, you need to convert that string to an `int` or `float`.",
                    "Common conversion functions:",
                    "  - `int(value)`: Converts `value` to an integer (raises ValueError if not possible).",
                    "  - `float(value)`: Converts `value` to a float (raises ValueError if not possible).",
                    "  - `str(value)`: Converts `value` to a string."
                 ],
                 "example": "# Input is always string\n# age_str = input(\"Enter age: \") # Example, won't run here\nage_str = \"25\" # Simulate input\n\n# Convert to integer\nage_int = int(age_str)\nprint(f\"Age as integer: {age_int}\")\nprint(f\"Next year you will be: {age_int + 1}\")\n\n# Convert number to string\ncount = 10\nmessage = \"The count is: \" + str(count)\nprint(message)\n\n# Convert string float to float\nprice_str = \"19.99\"\nprice_float = float(price_str)\nprint(f\"Price as float: {price_float}\")"
            },
            {
                "id": "l2_type_conv_challenge",
                "title": "Code: Convert and Calculate",
                "type": "code",
                "explanation": [
                    "Practice converting a string representation of a number into an actual integer type.",
                    "Remember to use the `int()` function for conversion."
                 ],
                "challenge": [
                    "1. Create a variable `num_str` and assign it the string value \"50\".",
                    "2. Create a variable `num_int` by converting `num_str` to an integer.",
                    "3. Create a variable `result` by adding `10` to `num_int`.",
                    "4. Print the value of `result`."
                ],
                "expected_stdout": "60\n"
            }
            # Consider adding another explanation for % // ** if desired (l2_operators)
        ]
    },
    {
        "id": "mod_strings",
        "title": "Module 3: Working with Strings",
        "lessons": [
            {
                "id": "l3_concatenation",
                "title": "String Concatenation",
                "type": "explanation",
                "text": [
                    "You can combine strings using the `+` operator.",
                    "This is called concatenation."
                ],
                "example": "first_name = \"John\"\nlast_name = \"Doe\"\nfull_name = first_name + \" \" + last_name\nprint(full_name)"
            },
            {
                "id": "l3_concat_challenge",
                "title": "Code: Combine Strings",
                "type": "code",
                "explanation": [
                    "Let's practice joining strings together."
                ],
                "challenge": [
                    "1. Create a variable `part1` with the value \"Hello, \".",
                    "2. Create a variable `part2` with the value \"world!\".",
                    "3. Create a variable `message` by concatenating `part1` and `part2`.",
                    "4. Print the `message` variable."
                ],
                "expected_stdout": "Hello, world!\n"
            },
            {
                "id": "l3_len_challenge",
                "title": "Code: String Length",
                "type": "code",
                "explanation": [
                    "The built-in `len()` function tells you how many characters are in a string."
                ],
                "challenge": [
                    "1. Create a variable `phrase` with the value \"Python is fun\".",
                    "2. Print the length of the `phrase` string."
                ],
                "expected_stdout": "13\n" # Length of "Python is fun"
            },
            {
                "id": "l3_indexing_slicing",
                "title": "String Indexing and Slicing",
                "type": "explanation",
                "text": [
                    "You can access individual characters in a string using their index.",
                    "Python uses **zero-based indexing**, meaning the first character is at index 0.",
                    "Negative indices count from the end: `-1` is the last character, `-2` is the second-to-last, etc.",
                    "**Slicing** extracts a portion of the string using `[start:stop]` or `[start:stop:step]`.",
                    "  - `start` is the index of the first character to include (inclusive).",
                    "  - `stop` is the index of the first character *not* to include (exclusive).",
                    "  - `step` determines the interval between characters (defaults to 1)."
                ],
                "example": "text = \"Python\"\n\n# Indexing\nprint(text[0])    # Output: P\nprint(text[2])    # Output: t\nprint(text[-1])   # Output: n\n\n# Slicing\nprint(text[0:2])  # Output: Py (index 0 up to, but not including, 2)\nprint(text[2:])   # Output: thon (index 2 to the end)\nprint(text[:4])   # Output: Pyth (beginning up to, but not including, 4)\nprint(text[::2])  # Output: Pto (every second character)"
            },
            {
                "id": "l3_methods_case",
                "title": "String Methods: Case Conversion",
                "type": "explanation",
                "text": [
                    "Strings have built-in **methods** (functions attached to the object) that perform operations.",
                    "You call a method using a dot `.` after the string variable.",
                    "Common case conversion methods:",
                    "  - `.upper()`: Returns a new string with all characters in uppercase.",
                    "  - `.lower()`: Returns a new string with all characters in lowercase."
                ],
                "example": "message = \"Hello World\"\n\nprint(message.upper()) # Output: HELLO WORLD\nprint(message.lower()) # Output: hello world\n\n# Note: The original string remains unchanged\nprint(message)         # Output: Hello World"
            },
            {
                "id": "l3_slice_challenge",
                "title": "Code: Extract Substring",
                "type": "code",
                "explanation": [
                    "Practice using slicing `[start:stop]` to get a part of a string."
                ],
                "challenge": [
                    "1. Create a variable `alphabet` with the value \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\".",
                    "2. Using slicing, extract the letters \"EFG\" from the `alphabet` string.",
                    "3. Print the extracted substring."
                ],
                "expected_stdout": "EFG\n" # Indices 4, 5, 6 (stop at 7)
            },
            {
                "id": "l3_case_challenge",
                "title": "Code: Change String Case",
                "type": "code",
                "explanation": [
                    "Use the `.upper()` or `.lower()` string methods."
                ],
                "challenge": [
                    "1. Create a variable `mixed_case` with the value \"PyThOn PrOgRaMmInG\".",
                    "2. Convert the `mixed_case` string to all uppercase.",
                    "3. Print the resulting uppercase string."
                ],
                "expected_stdout": "PYTHON PROGRAMMING\n"
            },
             {
                "id": "l3_fstrings",
                "title": "Formatted String Literals (f-strings)",
                "type": "explanation",
                "text": [
                    "f-strings (formatted string literals) provide a concise and convenient way to embed expressions inside string literals.",
                    "Prefix the string with the letter `f` or `F`.",
                    "Enclose expressions (like variables or calculations) in curly braces `{}` within the string.",
                    "The expressions are evaluated at runtime and formatted into the string."
                ],
                "example": "name = \"Alice\"\nage = 30\n\n# Using f-string\ngreeting = f\"My name is {name} and I am {age} years old.\"\nprint(greeting)\n\n# You can include expressions too\nprint(f\"In 5 years, I will be {age + 5} years old.\")"
            },
            {
                "id": "l3_fstring_challenge",
                "title": "Code: Using f-strings",
                "type": "code",
                "explanation": [
                    "Use an f-string (`f\"...\"`) to embed variables directly into a string."
                ],
                "challenge": [
                    "1. Create a variable `item` with the value \"apples\".",
                    "2. Create a variable `quantity` with the value 5.",
                    "3. Create a variable `cost` with the value 1.25.",
                    "4. Using an f-string, create and print a sentence that exactly reads:",
                    "You bought 5 apples for a total cost of $6.25."
                ],
                 # Note: Calculation {quantity * cost} is expected inside the f-string
                "expected_stdout": "You bought 5 apples for a total cost of $6.25.\n"
            },
            {
                "id": "l3_immutability",
                "title": "String Immutability",
                "type": "explanation",
                "text": [
                    "An important property of strings in Python is that they are **immutable**.",
                    "This means that once a string is created, its contents cannot be changed directly.",
                    "Trying to change a character using index assignment will cause a `TypeError`.",
                    "Methods like `.upper()`, `.lower()`, or `.replace()` do *not* change the original string; they *return a new* modified string."
                ],
                "example": "my_string = \"hello\"\n\n# This will cause an error:\n# my_string[0] = 'H' # TypeError: 'str' object does not support item assignment\n\n# Correct way: Create a new string\nnew_string = 'H' + my_string[1:]\nprint(f\"Original: {my_string}\")\nprint(f\"New: {new_string}\")\n\n# Methods return new strings\nupper_string = my_string.upper()\nprint(f\"Original after upper(): {my_string}\")\nprint(f\"Result of upper(): {upper_string}\")"
            },
            {
                "id": "l3_escape_sequences",
                "title": "Escape Sequences",
                "type": "explanation",
                "text": [
                    "Escape sequences are special character combinations starting with a backslash `\\`.",
                    "They allow you to include characters in a string that are otherwise difficult or impossible to type directly.",
                    "Common escape sequences:",
                    "  - `\\n`: Newline - moves the cursor to the beginning of the next line.",
                    "  - `\\t`: Tab - inserts a horizontal tab space.",
                    "  - `\\\\`: Backslash - includes a literal backslash character.",
                    "  - `\\\"`: Double quote - includes a literal double quote inside a double-quoted string.",
                    "  - `\\'`: Single quote - includes a literal single quote inside a single-quoted string."
                ],
                "example": "print(\"First line\\nSecond line\")\nprint(\"Column1\\tColumn2\")\nprint(\"This is a path: C:\\\\Users\\\\Name\")\nprint(\"She said: \\\"Hello!\\\"\")\nprint('It\\'s a sunny day.')"
                # Expected output of example:
                # First line
                # Second line
                # Column1	Column2
                # This is a path: C:\Users\Name
                # She said: "Hello!"
                # It's a sunny day.
            },
            {
                "id": "l3_methods_other",
                "title": "More String Methods",
                "type": "explanation",
                "text": [
                    "Strings have many useful built-in methods:",
                    "  - `.strip()`: Returns a new string with leading and trailing whitespace removed.",
                    "  - `.replace(old, new)`: Returns a new string where all occurrences of `old` are replaced with `new`.",
                    "  - `.find(substring)`: Returns the starting index of the *first* occurrence of `substring`. Returns `-1` if not found.",
                    "  - `.index(substring)`: Similar to `.find()`, but raises a `ValueError` if the substring is not found.",
                    "  - `.split(separator)`: Returns a list of substrings split by the `separator`. If no separator is given, splits by whitespace."
                ],
                "example": "text = \"   Some example text with spaces   \"\n\nprint(f\"Stripped: '{text.strip()}'\")\n\nprint(f\"Replaced: '{text.replace(' ', '_')}'\")\n\nprint(f\"Find 'example': {text.find('example')}\") # Note: index counts whitespace\nprint(f\"Find 'missing': {text.find('missing')}\")\n\nwords = text.strip().split(' ') # Chain methods!\nprint(f\"Split into words: {words}\")\n\ncsv_data = \"apple,banana,cherry\"\nitems = csv_data.split(',')\nprint(f\"Split CSV: {items}\")"
            },
            {
                "id": "l3_format_cleanup_challenge",
                "title": "Code: Clean Up String",
                "type": "code",
                "explanation": [
                    "Use string methods like `.strip()` and `.replace()` to clean up messy text.",
                    "Remember these methods return *new* strings."
                ],
                "challenge": [
                    "1. Create a variable `raw_data` with the value \"  user:admin;pass:1234;  \".",
                    "2. Create a variable `clean_data` by removing the leading/trailing whitespace from `raw_data`.",
                    "3. Create a variable `formatted_data` by replacing the semicolons (`;`) in `clean_data` with commas (`,`).",
                    "4. Print the `formatted_data`."
                ],
                "expected_stdout": "user:admin,pass:1234,\n"
            }
        ]
    },
    {
        "id": "mod_input_conditionals",
        "title": "Module 4: User Input and Conditionals",
        "lessons": [
            {
                "id": "l4_input",
                "title": "Getting User Input with input()",
                "type": "explanation",
                "text": [
                    "The `input()` function pauses your script and waits for the user to type something into the terminal.",
                    "It optionally takes a string argument, which is displayed as a prompt to the user.",
                    "**Important:** `input()` *always* returns the user's input as a **string**, even if they type numbers.",
                    "If you need the input as a number, you must convert it using `int()` or `float()`."
                ],
                "example": "# Simple input\nname = input(\"Enter your name: \")\nprint(f\"Hello, {name}!\")\n\n# Input requiring conversion\nage_str = input(\"Enter your age: \")\ntry:\n    age_int = int(age_str)\n    print(f\"You will be {age_int + 1} next year.\")\nexcept ValueError:\n    print(\"That wasn't a valid number for age!\")"
            },
            {
                "id": "l4_comparison",
                "title": "Comparison Operators",
                "type": "explanation",
                "text": [
                    "Comparison operators are used to compare values. They evaluate to a Boolean value (`True` or `False`).",
                    "Common operators:",
                    "  - `==` : Equal to",
                    "  - `!=` : Not equal to",
                    "  - `>`  : Greater than",
                    "  - `<`  : Less than",
                    "  - `>=` : Greater than or equal to",
                    "  - `<=` : Less than or equal to",
                    "These are fundamental for making decisions in your code."
                ],
                "example": "x = 10\ny = 5\n\nprint(x == 10)  # Output: True\nprint(x != y)   # Output: True\nprint(x > y)    # Output: True\nprint(y < 10)   # Output: True\nprint(x >= 10)  # Output: True\nprint(y <= 4)   # Output: False"
            },
            {
                "id": "l4_if",
                "title": "Conditional Logic: The 'if' Statement",
                "type": "explanation",
                "text": [
                    "The `if` statement allows you to execute a block of code only if a certain condition is `True`.",
                    "The syntax is: `if condition:`",
                    "The code block to be executed must be **indented** below the `if` statement.",
                    "Indentation (usually 4 spaces) is how Python defines code blocks."
                ],
                "example": "temperature = 25\n\nif temperature > 20:\n    print(\"It's a warm day!\") # This line executes\n\nif temperature < 0:\n    print(\"It's freezing!\")   # This line does NOT execute"
            },
            {
                "id": "l4_if_else",
                "title": "Adding Alternatives: 'else'",
                "type": "explanation",
                "text": [
                    "The `else` statement provides an alternative block of code to execute if the `if` condition is `False`.",
                    "It must follow an `if` statement and its block is also indented.",
                    "Syntax: `else:`"
                ],
                "example": "age = 16\n\nif age >= 18:\n    print(\"You are eligible to vote.\")\nelse:\n    print(\"You are not yet eligible to vote.\") # This line executes"
            },
            {
                "id": "l4_if_elif_else",
                "title": "Multiple Conditions: 'elif'",
                "type": "explanation",
                "text": [
                    "The `elif` (else if) statement allows you to check multiple conditions in sequence.",
                    "It comes after an `if` and before a potential `else`.",
                    "Python checks the `if` condition first. If `False`, it checks the first `elif`. If that's `False`, it checks the next `elif`, and so on.",
                    "As soon as one condition is `True`, its block executes, and the rest of the `if/elif/else` structure is skipped.",
                    "The final `else` (optional) catches any cases where none of the preceding `if` or `elif` conditions were `True`."
                ],
                "example": "score = 75\n\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelif score >= 70:\n    grade = 'C' # This condition is True, its block runs\nelif score >= 60:\n    grade = 'D'\nelse:\n    grade = 'F'\n\nprint(f\"Your grade is: {grade}\") # Output: Your grade is: C"
            },
            {
                "id": "l4_conditionals_quiz",
                "title": "Quiz: Conditionals",
                "type": "quiz",
                "question": "What will the following code print?\n\nx = 5\ny = 10\n\nif x > y:\n    print(\"Alpha\")\nelif y % x == 0: # 10 divided by 5 has remainder 0\n    print(\"Bravo\")\nelse:\n    print(\"Charlie\")",
                "options": [
                    "Alpha",
                    "Bravo",
                    "Charlie",
                    "Nothing will be printed"
                ],
                "correct_answer": 1 # 10 % 5 == 0 is True
            },
            {
                "id": "l4_if_else_challenge",
                "title": "Code: Check Number Sign",
                "type": "code",
                "explanation": [
                    "Use `if`, `elif`, and `else` to determine if a number is positive, negative, or zero.",
                    "Remember to use comparison operators (`>`, `<`, `==`)."
                ],
                "challenge": [
                    "1. Create a variable `number` and assign it the value `-7`.",
                    "2. Write an `if-elif-else` structure that checks the value of `number`:",
                    "   - If the number is greater than 0, print \"Positive\".",
                    "   - Else if the number is less than 0, print \"Negative\".",
                    "   - Else (if the number is 0), print \"Zero\".",
                ],
                "expected_stdout": "Negative\n"
            },
            {
                "id": "l4_logical_operators",
                "title": "Logical Operators (and, or, not)",
                "type": "explanation",
                "text": [
                    "Logical operators combine or modify Boolean (`True`/`False`) values.",
                    "They are essential for creating more complex conditions in `if` statements.",
                    "  - `and`: Returns `True` only if *both* conditions on its left and right are `True`.",
                    "  - `or`: Returns `True` if *at least one* of the conditions on its left or right is `True`.",
                    "  - `not`: Reverses the Boolean value. `not True` becomes `False`, and `not False` becomes `True`."
                ],
                "example": "age = 25\nhas_ticket = True\n\n# Example with 'and'\nif age >= 18 and has_ticket:\n    print(\"Entry allowed (age >= 18 AND has ticket).\")\nelse:\n    print(\"Entry denied.\")\n\nscore = 75\nis_weekend = True\n\n# Example with 'or'\nif score > 90 or is_weekend:\n    print(\"You get a prize (score > 90 OR it's weekend).\")\nelse:\n    print(\"No prize this time.\")\n\n# Example with 'not'\nis_raining = False\nif not is_raining:\n    print(\"It's not raining, let's go out!\")"
            },
            {
                "id": "l4_logical_quiz",
                "title": "Quiz: Logical Operators",
                "type": "quiz",
                "question": "What will the following code print?\n\na = 10\nb = 5\nc = True\n\nif (a > b and c) or (b == 5 and not c):\n    print(\"Alpha\") # (True and True) or (True and False) -> True or False -> True\nelif not c and a == 10:\n    print(\"Bravo\")\nelse:\n    print(\"Charlie\")",
                "options": [
                    "Alpha",
                    "Bravo",
                    "Charlie",
                    "Nothing will be printed"
                ],
                "correct_answer": 0 # (True and True) is True. True or (...) is True. First block runs.
            }
            # Consider adding l4_input_convert_challenge here or after input explanation
        ]
    },
    {
        "id": "mod_loops",
        "title": "Module 5: Loops",
        "lessons": [
            {
                "id": "l5_for_intro",
                "title": "Introduction to 'for' Loops",
                "type": "explanation",
                "text": [
                    "Loops are used to repeat a block of code multiple times.",
                    "The `for` loop iterates over a sequence (like a string, a list, or a range of numbers).",
                    "The basic syntax is `for variable in sequence:`",
                    "The code block to be repeated must be **indented**.",
                    "In each iteration, the `variable` takes the next value from the `sequence`."
                ],
                "example": "# Looping through a string\nword = \"Hi\"\nfor letter in word:\n    print(letter)\n\n# Looping through a range of numbers\n# range(3) generates numbers 0, 1, 2\nprint(\"\\nNumbers:\")\nfor i in range(3):\n    print(i)"
                # Expected Output of example:
                # H
                # i
                #
                # Numbers:
                # 0
                # 1
                # 2
            },
            {
                "id": "l5_for_range",
                "title": "'for' Loops with range()",
                "type": "explanation",
                "text": [
                    "The `range()` function is commonly used with `for` loops to repeat code a specific number of times.",
                    "  - `range(stop)`: Generates numbers from 0 up to (but not including) `stop`.",
                    "  - `range(start, stop)`: Generates numbers from `start` up to (but not including) `stop`.",
                    "  - `range(start, stop, step)`: Generates numbers from `start` up to `stop`, incrementing by `step`."
                ],
                "example": "print(\"Numbers 0 to 4:\")\nfor i in range(5):\n    print(i)\n\nprint(\"\\nNumbers 2 to 4:\")\nfor i in range(2, 5):\n    print(i)\n\nprint(\"\\nEven numbers 0 to 8:\")\nfor i in range(0, 9, 2):\n    print(i)"
                # Expected Output of example:
                # Numbers 0 to 4:
                # 0
                # 1
                # 2
                # 3
                # 4
                #
                # Numbers 2 to 4:
                # 2
                # 3
                # 4
                #
                # Even numbers 0 to 8:
                # 0
                # 2
                # 4
                # 6
                # 8
            },
            {
                "id": "l5_for_challenge",
                "title": "Code: Print Numbers with 'for'",
                "type": "code",
                "explanation": [
                    "Use a `for` loop and the `range()` function to print a sequence of numbers.",
                    "Remember that `range(n)` goes from 0 up to n-1."
                ],
                "challenge": [
                    "Write a `for` loop that prints the numbers 1, 2, 3, 4, and 5, each on a new line."
                ],
                "expected_stdout": "1\n2\n3\n4\n5\n" # Note: range should likely be range(1, 6)
            },
            {
                "id": "l5_while_intro",
                "title": "Introduction to 'while' Loops",
                "type": "explanation",
                "text": [
                    "The `while` loop repeats a block of code as long as a certain condition remains `True`.",
                    "The syntax is `while condition:`",
                    "The code block to be repeated must be **indented**.",
                    "The condition is checked *before* each iteration. If the condition is initially `False`, the loop body never executes.",
                    "**Important:** You must ensure that something inside the loop eventually makes the condition `False`, otherwise you'll create an infinite loop!"
                ],
                "example": "count = 0\n\nprint(\"Counting up:\")\nwhile count < 3: # Condition: count is less than 3\n    print(count)\n    count = count + 1 # Make the condition eventually False\n\nprint(f\"Loop finished. Final count: {count}\")"
                # Expected Output of example:
                # Counting up:
                # 0
                # 1
                # 2
                # Loop finished. Final count: 3
            },
            {
                "id": "l5_while_challenge",
                "title": "Code: Countdown with 'while'",
                "type": "code",
                "explanation": [
                    "Use a `while` loop to repeat actions until a condition is met.",
                    "You'll need a variable to keep track, and you must change that variable inside the loop."
                ],
                "challenge": [
                    "1. Create a variable `counter` initialized to 3.",
                    "2. Write a `while` loop that continues as long as `counter` is greater than 0.",
                    "3. Inside the loop, print the value of `counter`.",
                    "4. Also inside the loop, decrease the value of `counter` by 1.",
                    "5. After the loop finishes, print the word \"Go!\""
                ],
                "expected_stdout": "3\n2\n1\nGo!\n"
            },
            {
                "id": "l5_loops_quiz",
                "title": "Quiz: Loops",
                "type": "quiz",
                "question": "What will the following code print?\n\nn = 0\nfor i in range(1, 4): # i will be 1, 2, 3\n    n = n + i\nprint(n)",
                "options": [
                    "3",
                    "6", # 0 + 1 + 2 + 3 = 6
                    "10",
                    "Infinite loop"
                ],
                "correct_answer": 1
            },
             {
                "id": "l5_loop_string_challenge",
                "title": "Code: Iterate and Print String",
                "type": "code",
                "explanation": [
                    "You can use a `for` loop to iterate directly over the characters of a string."
                ],
                "challenge": [
                    "1. Create a variable `my_string` with the value \"LOOP\".",
                    "2. Write a `for` loop that iterates through each character of `my_string`.",
                    "3. Inside the loop, print each character on its own line."
                ],
                "expected_stdout": "L\nO\nO\nP\n"
            },
            {
                "id": "l5_break_continue",
                "title": "Loop Control: break and continue",
                "type": "explanation",
                "text": [
                    "Sometimes you need more control over how a loop executes.",
                    "  - `break`: Immediately terminates the *entire* current loop (the `for` or `while` loop it's inside). Execution continues with the statement after the loop.",
                    "  - `continue`: Skips the *rest of the current iteration* of the loop. Execution jumps to the top of the loop for the next iteration (if any)."
                ],
                "example": "# Example using break\nprint(\"Finding first number divisible by 3:\")\nnumbers = [1, 2, 5, 6, 8, 9]\nfound_num = None\nfor num in numbers:\n    print(f\"Checking {num}...\")\n    if num % 3 == 0:\n        found_num = num\n        print(\"Found it!\")\n        break # Exit the loop now\nprint(f\"First number divisible by 3: {found_num}\")\n\n# Example using continue\nprint(\"\\nPrinting only even numbers:\")\nfor i in range(1, 6):\n    if i % 2 != 0: # If odd\n        continue   # Skip the print for this iteration\n    print(f\"Even number: {i}\")"
            },
            {
                "id": "l5_break_challenge",
                "title": "Code: Find First Multiple",
                "type": "code",
                "explanation": [
                    "Use a `for` loop and the `break` statement to efficiently find the first item in a sequence that meets a condition.",
                    "The modulo operator `%` is useful for checking divisibility."
                ],
                "challenge": [
                    "1. Create a list `nums = [11, 14, 21, 25, 30, 35, 42]`.",
                    "2. Write a `for` loop to iterate through `nums`.",
                    "3. Inside the loop, check if the current number is divisible by 7.",
                    "4. If it is divisible by 7, print the number and then immediately `break` out of the loop.",
                ],
                "expected_stdout": "14\n" # 14 is the first number divisible by 7
            }
            # Consider adding l5_enumerate explanation later
        ]
    },
    {
        "id": "mod_lists",
        "title": "Module 6: Lists",
        "lessons": [
            {
                "id": "l6_intro",
                "title": "Introduction to Lists",
                "type": "explanation",
                "text": [
                    "Lists are ordered, mutable (changeable) sequences of items.",
                    "They are one of the most versatile data types in Python.",
                    "Lists are created using square brackets `[]`, with items separated by commas.",
                    "Lists can contain items of different data types (heterogeneous)."
                ],
                "example": "# An empty list\nempty_list = []\nprint(empty_list)\n\n# A list of integers\nnumbers = [1, 2, 3, 5, 8]\nprint(numbers)\n\n# A list of strings\nfruits = [\"apple\", \"banana\", \"cherry\"]\nprint(fruits)\n\n# A list with mixed data types\nmixed_list = [1, \"hello\", 3.14, True]\nprint(mixed_list)"
            },
            {
                "id": "l6_indexing_slicing",
                "title": "List Indexing and Slicing",
                "type": "explanation",
                "text": [
                    "Just like strings, you can access individual items in a list using their index.",
                    "Python uses **zero-based indexing** for lists as well (first item is at index 0).",
                    "Negative indices work from the end (`-1` is the last item).",
                    "**Slicing** (`[start:stop:step]`) works the same way as with strings, returning a new list containing the selected items."
                ],
                "example": "colors = [\"red\", \"green\", \"blue\", \"yellow\", \"purple\"]\n\n# Indexing\nprint(colors[0])    # Output: red\nprint(colors[2])    # Output: blue\nprint(colors[-1])   # Output: purple\n\n# Slicing\nprint(colors[1:3])  # Output: ['green', 'blue'] (index 1 up to, not including, 3)\nprint(colors[:2])   # Output: ['red', 'green'] (from start up to index 2)\nprint(colors[3:])   # Output: ['yellow', 'purple'] (from index 3 to the end)\nprint(colors[::2])  # Output: ['red', 'blue', 'purple'] (every second item)"
            },
            {
                "id": "l6_list_challenge_access",
                "title": "Code: Access List Element",
                "type": "code",
                "explanation": [
                    "Remember that list indexing starts at 0."
                ],
                "challenge": [
                    "1. Create a list named `planets` containing the strings: \"Mercury\", \"Venus\", \"Earth\", \"Mars\".",
                    "2. Print the third planet in the list (which is \"Earth\")."
                ],
                "expected_stdout": "Earth\n" # Index 2
            },
            {
                "id": "l6_methods_append_insert",
                "title": "List Methods: Adding Items",
                "type": "explanation",
                "text": [
                    "Lists are mutable, meaning you can change them after creation.",
                    "Common methods for adding items:",
                    "  - `.append(item)`: Adds `item` to the *end* of the list.",
                    "  - `.insert(index, item)`: Inserts `item` at the specified `index`, shifting existing items to the right."
                ],
                "example": "my_list = [10, 20]\nprint(f\"Original list: {my_list}\")\n\n# Append\nmy_list.append(30)\nprint(f\"After append(30): {my_list}\")\n\n# Insert\nmy_list.insert(1, 15) # Insert 15 at index 1\nprint(f\"After insert(1, 15): {my_list}\")"
                # Expected Output:
                # Original list: [10, 20]
                # After append(30): [10, 20, 30]
                # After insert(1, 15): [10, 15, 20, 30]
            },
            {
                "id": "l6_methods_remove_pop",
                "title": "List Methods: Removing Items",
                "type": "explanation",
                "text": [
                    "Methods for removing items:",
                    "  - `.remove(value)`: Removes the *first* occurrence of the specified `value`. Raises a `ValueError` if the value is not found.",
                    "  - `.pop(index)`: Removes and *returns* the item at the specified `index`. If no index is given, it removes and returns the *last* item.",
                    "  - `del list_name[index]`: Another way to remove an item by index (or slice)."
                ],
                "example": "items = ['a', 'b', 'c', 'b', 'd']\nprint(f\"Original: {items}\")\n\n# Remove by value\nitems.remove('b') # Removes the first 'b'\nprint(f\"After remove('b'): {items}\")\n\n# Pop by index\npopped_item = items.pop(1) # Removes 'c' (at index 1)\nprint(f\"After pop(1): {items}\")\nprint(f\"Popped item: {popped_item}\")\n\n# Pop last item\nlast_item = items.pop()\nprint(f\"After pop(): {items}\")\nprint(f\"Last item popped: {last_item}\")\n\n# Delete by index\ndel items[0]\nprint(f\"After del items[0]: {items}\")"
                # Expected Output:
                # Original: ['a', 'b', 'c', 'b', 'd']
                # After remove('b'): ['a', 'c', 'b', 'd']
                # After pop(1): ['a', 'b', 'd']
                # Popped item: c
                # After pop(): ['a', 'b']
                # Last item popped: d
                # After del items[0]: ['b']
            },
            {
                "id": "l6_list_challenge_modify",
                "title": "Code: Modify a List",
                "type": "code",
                "explanation": [
                    "Practice using `.append()`, `.insert()`, and `.remove()` or `.pop()` to change a list."
                ],
                "challenge": [
                    "1. Create a list `nums` containing the numbers `[1, 2, 4]`.",
                    "2. Append the number `5` to the end of the list.",
                    "3. Insert the number `3` at index 2.",
                    "4. Remove the number `1` from the list.",
                    "5. Print the final `nums` list."
                ],
                "expected_stdout": "[2, 3, 4, 5]\n" # [1, 2, 4] -> [1, 2, 4, 5] -> [1, 2, 3, 4, 5] -> [2, 3, 4, 5]
            },
            {
                "id": "l6_len",
                "title": "List Length with len()",
                "type": "explanation",
                "text": [
                    "The built-in `len()` function works with lists just like strings.",
                    "It returns the total number of items currently in the list."
                ],
                "example": "languages = [\"Python\", \"Java\", \"C++\"]\n\ncount = len(languages)\nprint(f\"There are {count} languages in the list.\")\n\nempty = []\nprint(f\"Length of empty list: {len(empty)}\")"
            },
            {
                "id": "l6_looping",
                "title": "Looping Through Lists",
                "type": "explanation",
                "text": [
                    "You can easily iterate over all items in a list using a `for` loop.",
                    "The loop variable will take the value of each list item in turn, from beginning to end."
                ],
                "example": "animals = [\"cat\", \"dog\", \"fish\"]\n\nprint(\"Animals:\")\nfor animal in animals:\n    print(f\"- {animal}\")\n\n# You can also loop with index using range(len(list))\nprint(\"\\nAnimals with index:\")\nfor i in range(len(animals)):\n    print(f\"Index {i}: {animals[i]}\")"
            },
            {
                "id": "l6_list_challenge_loop",
                "title": "Code: Loop and Transform",
                "type": "code",
                "explanation": [
                    "Use a `for` loop to process each item in a list.",
                ],
                "challenge": [
                    "1. Create a list `numbers` containing `[10, 20, 30]`.",
                    "2. Write a `for` loop that iterates through the `numbers` list.",
                    "3. Inside the loop, print each number multiplied by 2 (each result on a new line)."
                ],
                "expected_stdout": "20\n40\n60\n"
            },
            {
                "id": "l6_quiz",
                "title": "Quiz: Lists",
                "type": "quiz",
                "question": "Consider the list `my_list = [5, 10, 15, 20]`. What is the value of `my_list[1]`?",
                "options": [
                    "5",
                    "10", # Index 1 is the second element
                    "15",
                    "Error: Index out of range"
                ],
                "correct_answer": 1
            },
            {
                "id": "l6_quiz_methods",
                "title": "Quiz: List Methods",
                "type": "quiz",
                "question": "Which method adds an element to the *end* of a list?",
                "options": [
                    ".insert()",
                    ".add()",
                    ".append()",
                    ".extend()"
                ],
                "correct_answer": 2
            },
            {
                "id": "l6_membership",
                "title": "List Membership (in)",
                "type": "explanation",
                "text": [
                    "You can check if an item exists within a list using the `in` operator.",
                    "It returns `True` if the item is found in the list, and `False` otherwise.",
                    "You can also use `not in` to check if an item is *not* present in the list."
                ],
                "example": "my_list = [\"apple\", \"banana\", \"cherry\"]\n\n# Check if 'banana' is in the list\nif \"banana\" in my_list:\n    print(\"Yes, 'banana' is in the list.\")\nelse:\n    print(\"No, 'banana' is not in the list.\")\n\n# Check if 'orange' is NOT in the list\nif \"orange\" not in my_list:\n    print(\"Yes, 'orange' is not in the list.\")\nelse:\n    print(\"No, 'orange' is in the list.\")"
            },
            {
                "id": "l6_membership_quiz",
                "title": "Quiz: Membership Testing",
                "type": "quiz",
                "question": "What will the following code print?\n\nnumbers = [1, 3, 5, 7]\nif 4 not in numbers:\n    print(\"A\")\nif 5 in numbers:\n    print(\"B\")\n", # 4 is not in numbers (True), 5 is in numbers (True)
                "options": [
                    "A",
                    "B",
                    "A\nB", # Both conditions are true
                    "Nothing will be printed"
                ],
                "correct_answer": 2
            },
            {
                "id": "l6_methods_other",
                "title": "More List Methods",
                "type": "explanation",
                "text": [
                    "Lists have several other handy methods:",
                    "  - `.sort()`: Sorts the list **in-place** (modifies the original list). Does not return anything.",
                    "  - `sorted(list)`: Returns a **new sorted list**, leaving the original unchanged. (This is a built-in function, not a list method).",
                    "  - `.index(value)`: Returns the index of the *first* occurrence of `value`. Raises `ValueError` if not found.",
                    "  - `.count(value)`: Returns the number of times `value` appears in the list.",
                    "  - `.extend(iterable)`: Adds all items from an `iterable` (like another list) to the end of the current list **in-place**."
                ],
                "example": "nums = [4, 1, 5, 1, 3]\n\nprint(f\"Original: {nums}\")\n\n# Using sorted() function\nnew_sorted_list = sorted(nums)\nprint(f\"Original after sorted(): {nums}\")\nprint(f\"New list from sorted(): {new_sorted_list}\")\n\n# Using .sort() method\nnums.sort() # Sorts in-place\nprint(f\"Original after .sort(): {nums}\")\n\n# Other methods\nprint(f\"Index of 5: {nums.index(5)}\")\nprint(f\"Count of 1: {nums.count(1)}\")\n\nmore_nums = [9, 8]\nnums.extend(more_nums) # Extends in-place\nprint(f\"After extend([9, 8]): {nums}\")"
            },
            {
                "id": "l6_sort_count_challenge",
                "title": "Code: Sort and Count",
                "type": "code",
                "explanation": [
                    "Practice using the `.sort()` method to modify a list and `.count()` to find item frequency.",
                    "Remember that `.sort()` changes the list directly."
                ],
                "challenge": [
                    "1. Create a list `grades = [88, 92, 75, 92, 85, 92]`.",
                    "2. Count how many times the grade `92` appears in the list and print this count.",
                    "3. Sort the `grades` list in ascending order (in-place).",
                    "4. Print the sorted `grades` list."
                ],
                "expected_stdout": "3\n[75, 85, 88, 92, 92, 92]\n"
            }
            # Consider adding l6_comprehensions or l6_nested later
        ]
    },
    {
        "id": "mod_dictionaries",
        "title": "Module 7: Dictionaries",
        "lessons": [
            {
                "id": "l7_intro",
                "title": "Introduction to Dictionaries",
                "type": "explanation",
                "text": [
                    "Dictionaries are unordered collections of key-value pairs.",
                    "They are mutable (changeable) and indexed by keys (unlike lists indexed by numbers).",
                    "Keys must be unique and immutable (e.g., strings, numbers, tuples).",
                    "Values can be of any data type and can be duplicated.",
                    "Dictionaries are created using curly braces `{}` with `key: value` pairs separated by commas."
                ],
                "example": "# An empty dictionary\nempty_dict = {}\nprint(empty_dict)\n\n# A dictionary of student info\nstudent = {\n    \"name\": \"Bob\",\n    \"age\": 20,\n    \"major\": \"Computer Science\",\n    \"gpa\": 3.5\n}\nprint(student)\n\n# Keys can be numbers too\nnum_dict = {1: 'one', 2: 'two'}\nprint(num_dict)"
            },
            {
                "id": "l7_accessing",
                "title": "Accessing Dictionary Values",
                "type": "explanation",
                "text": [
                    "You access the value associated with a key using square brackets `[]` with the key inside.",
                    "If you try to access a key that doesn't exist using `[]`, you'll get a `KeyError`.",
                    "Alternatively, you can use the `.get(key, default)` method.",
                    "  - It returns the value for the key if it exists.",
                    "  - If the key doesn't exist, it returns `None` by default, or the `default` value you specify.",
                    "  - Using `.get()` avoids KeyErrors."
                ],
                "example": "student = {\"name\": \"Bob\", \"age\": 20, \"major\": \"CompSci\"}\n\n# Access using square brackets\nprint(f\"Name: {student['name']}\")\n\n# Access using .get()\nprint(f\"Age: {student.get('age')}\")\n\n# Accessing a non-existent key\n# print(student['city']) # This would cause a KeyError\n\n# Using .get() for a non-existent key (returns None)\nprint(f\"City: {student.get('city')}\")\n\n# Using .get() with a default value\nprint(f\"Minor: {student.get('minor', 'Not specified')}\")"
            },
            {
                "id": "l7_add_modify",
                "title": "Adding and Modifying Entries",
                "type": "explanation",
                "text": [
                    "Dictionaries are mutable, so you can easily add new key-value pairs or change existing values.",
                    "To add a new entry, assign a value to a new key using square bracket notation.",
                    "To modify an existing entry, assign a new value to an existing key. The old value will be overwritten."
                ],
                "example": "student = {\"name\": \"Bob\", \"age\": 20}\nprint(f\"Original: {student}\")\n\n# Add a new key-value pair\nstudent['major'] = \"Physics\"\nprint(f\"After adding major: {student}\")\n\n# Modify an existing value\nstudent['age'] = 21\nprint(f\"After modifying age: {student}\")"
            },
            {
                "id": "l7_removing",
                "title": "Removing Dictionary Entries",
                "type": "explanation",
                "text": [
                    "You can remove key-value pairs from a dictionary in several ways:",
                    "  - `del dictionary[key]`: Removes the entry with the specified key. Raises `KeyError` if the key doesn't exist.",
                    "  - `.pop(key, default)`: Removes the entry with the specified key and *returns its value*. Raises `KeyError` if the key isn't found and no `default` is provided. If a `default` is provided, it's returned instead of raising an error when the key is missing.",
                    "  - `.popitem()`: Removes and returns an *arbitrary* (key, value) pair. Useful for iterating through and consuming a dictionary. Raises `KeyError` if the dictionary is empty.",
                    "  - `.clear()`: Removes *all* entries from the dictionary, making it empty."
                ],
                "example": "car = {'make': 'Ford', 'model': 'Mustang', 'year': 2022, 'color': 'Red'}\nprint(f\"Original: {car}\")\n\n# Using del\ndel car['color']\nprint(f\"After del 'color': {car}\")\n\n# Using pop (and getting the value)\nmodel_name = car.pop('model')\nprint(f\"After pop 'model': {car}\")\nprint(f\"Popped model: {model_name}\")\n\n# Using popitem (Python 3.7+ removes last inserted)\nlast_item = car.popitem()\nprint(f\"After popitem: {car}\")\nprint(f\"Popped item: {last_item}\")\n\n# Using clear\ncar.clear()\nprint(f\"After clear: {car}\")"
            },
            {
                "id": "l7_dict_challenge_crud",
                "title": "Code: Create, Modify, Access Dict",
                "type": "code",
                "explanation": [
                    "Practice creating a dictionary and performing basic operations:",
                    "accessing, adding, modifying, and removing key-value pairs."
                ],
                "challenge": [
                    "1. Create a dictionary named `person` with two key-value pairs:",
                    "   - `name`: \"Alice\"",
                    "   - `city`: \"New York\"",
                    "2. Add a new key-value pair: `age`: 30.",
                    "3. Modify the value associated with the `city` key to \"London\".",
                    "4. Use the `del` keyword to remove the `age` entry.",
                    "5. Print the final value associated with the `city` key."
                ],
                "expected_stdout": "London\n"
                # Steps: {'name':'Alice','city':'NY'} -> {'name':'Alice','city':'NY','age':30} -> {'name':'Alice','city':'London','age':30} -> {'name':'Alice','city':'London'} -> Print city -> London
            },
            {
                "id": "l7_looping",
                "title": "Looping Through Dictionaries",
                "type": "explanation",
                "text": [
                    "You can iterate through dictionaries in several ways:",
                    "1. **Iterating over keys (default):** `for key in my_dict:`",
                    "2. **Iterating over values:** `for value in my_dict.values():`",
                    "3. **Iterating over key-value pairs:** `for key, value in my_dict.items():` (This is often the most useful).",
                    "Dictionary views (`.keys()`, `.values()`, `.items()`) reflect changes made to the dictionary during iteration in some cases, but it's generally safer not to modify the dictionary size while iterating over it."
                ],
                "example": "capitals = {\"USA\": \"Washington D.C.\", \"France\": \"Paris\", \"Japan\": \"Tokyo\"}\n\nprint(\"Keys:\")\nfor country in capitals:\n    print(country) # Prints keys by default\n\nprint(\"\\nValues:\")\nfor city in capitals.values():\n    print(city)\n\nprint(\"\\nKey-Value Pairs:\")\nfor country, city in capitals.items():\n    print(f\"The capital of {country} is {city}.\")"
            },
             {
                "id": "l7_dict_challenge_loop",
                "title": "Code: Loop Through Dictionary Items",
                "type": "code",
                "explanation": [
                    "Use a `for` loop with the `.items()` method to access both keys and values within a dictionary.",
                ],
                "challenge": [
                    "1. Create a dictionary `stock` representing items and their quantities:",
                    "   `{\"apples\": 50, \"bananas\": 25, \"oranges\": 30}`",
                    "2. Write a `for` loop that iterates through the `stock` dictionary using `.items()`.",
                    "3. Inside the loop, print each item and its quantity in the format:",
                    "   `Item: [key], Quantity: [value]` (each on a new line)."
                ],
                "expected_stdout": "Item: apples, Quantity: 50\nItem: bananas, Quantity: 25\nItem: oranges, Quantity: 30\n"
                # Note: Dictionary order is guaranteed in Python 3.7+, but output might vary in older versions.
                # However, testing systems often use newer Python. The expected output assumes insertion order.
            },
            {
                "id": "l7_quiz_methods",
                "title": "Quiz: Dictionary Operations",
                "type": "quiz",
                "question": "Which method safely retrieves a value from a dictionary, returning `None` or a specified default if the key doesn't exist, thus avoiding a `KeyError`?",
                "options": [
                    "dict[key]",
                    "dict.pop(key)",
                    "dict.get(key, default)",
                    "dict.items()"
                ],
                "correct_answer": 2 # .get() is the safe way
            },
            {
                "id": "l7_methods_other",
                "title": "Other Dictionary Methods & Notes",
                "type": "explanation",
                "text": [
                    "A few other useful things to know about dictionaries:",
                    "  - `len(my_dict)`: Returns the number of key-value pairs in the dictionary.",
                    "  - `'key' in my_dict`: Checks if a key exists in the dictionary (returns `True` or `False`). This is efficient.",
                    "  - `sorted(my_dict)`: Returns a *list* of the dictionary's keys, sorted.",
                    "  - **Keys must be immutable:** You cannot use lists or other dictionaries as keys, but you can use strings, numbers, or tuples (if they contain only immutable elements).",
                    "  - **Values can be anything:** Values can be numbers, strings, lists, other dictionaries, etc."
                ],
                "example": "data = {'id': 101, 'name': 'Widget', 'tags': ['A', 'B']}\n\n# Length\nprint(f\"Number of items: {len(data)}\")\n\n# Membership testing (for keys)\nprint(f\"'name' in data? {'name' in data}\")\nprint(f\"'price' in data? {'price' in data}\")\n\n# Sorting keys\nprint(f\"Sorted keys: {sorted(data)}\")\n\n# Example of a dictionary as a value\ncomplex_data = {\n    'user_id': 123,\n    'prefs': {'theme': 'dark', 'notifications': True}\n}\nprint(f\"User theme: {complex_data['prefs']['theme']}\")"
            }
            # Consider adding nested dictionaries as a separate lesson if needed later.
        ]
    },
    {
        "id": "mod_tuples",
        "title": "Module 8: Tuples",
        "lessons": [
            {
                "id": "l8_intro",
                "title": "Introduction to Tuples",
                "type": "explanation",
                "text": [
                    "Tuples are ordered, **immutable** sequences of items.",
                    "Think of them like lists, but once created, you cannot change their contents (add, remove, or modify items).",
                    "Tuples are created using parentheses `()` or just by separating items with commas.",
                    "They are often used for fixed collections of items, like coordinates (x, y) or returning multiple values from a function.",
                    "Because they are immutable, they can be used as keys in dictionaries (unlike lists)."
                ],
                "example": "# Creating tuples\nempty_tuple = ()\npoint = (10, 20)\ncoordinates = 34.05, -118.24 # Parentheses optional\nsingle_item_tuple = (5,) # Note the trailing comma!\n\nprint(point)\nprint(coordinates)\nprint(type(coordinates))\nprint(single_item_tuple)\nprint(type(single_item_tuple))\n\n# Trying to change a tuple causes an error\n# point[0] = 15 # This will raise a TypeError"
            },
            {
                "id": "l8_indexing_slicing",
                "title": "Tuple Indexing and Slicing",
                "type": "explanation",
                "text": [
                    "Tuples support indexing and slicing, just like lists and strings.",
                    "Zero-based indexing is used (first item is at index 0).",
                    "Negative indices count from the end (`-1` is the last item).",
                    "Slicing `[start:stop:step]` extracts a portion of the tuple, creating a *new* tuple."
                ],
                "example": "rgb_color = (\"red\", \"green\", \"blue\")\n\n# Indexing\nprint(f\"First element: {rgb_color[0]}\")\nprint(f\"Last element: {rgb_color[-1]}\")\n\n# Slicing\nfirst_two = rgb_color[0:2]\nprint(f\"First two: {first_two}\") # Output: ('red', 'green')\n\nprint(f\"From index 1: {rgb_color[1:]}\") # Output: ('green', 'blue')\n\nprint(f\"Original tuple unchanged: {rgb_color}\")"
            },
            {
                "id": "l8_packing_unpacking",
                "title": "Tuple Packing and Unpacking",
                "type": "explanation",
                "text": [
                    "**Packing:** When you create a tuple by assigning comma-separated values without parentheses, you are 'packing' those values into a tuple.",
                    "**Unpacking:** You can assign the elements of a tuple to individual variables if the number of variables matches the number of tuple elements.",
                    "This is very useful for assignments, swapping variables, and handling functions that return multiple values."
                ],
                "example": "# Packing\npacked_tuple = 1, 2, 3 # Creates tuple (1, 2, 3)\nprint(f\"Packed: {packed_tuple}\")\n\n# Unpacking\npoint = (10, 20)\nx, y = point # Assigns 10 to x, 20 to y\nprint(f\"Unpacked: x={x}, y={y}\")\n\n# Variable swap using packing/unpacking\na = 5\nb = 10\na, b = b, a # Packs (b, a) -> (10, 5), then unpacks to a, b\nprint(f\"Swapped: a={a}, b={b}\")\n\n# Unpacking with mismatch causes error\n# x, y = (1, 2, 3) # ValueError: too many values to unpack"
            },
            {
                "id": "l8_methods",
                "title": "Tuple Methods",
                "type": "explanation",
                "text": [
                    "Because tuples are immutable, they have very few built-in methods compared to lists.",
                    "The main methods are:",
                    "  - `.count(value)`: Returns the number of times `value` appears in the tuple.",
                    "  - `.index(value)`: Returns the index of the *first* occurrence of `value`. Raises a `ValueError` if the value is not found."
                ],
                "example": "my_tuple = (1, 2, 'a', 'b', 2, 'a', 2)\n\nprint(f\"Count of 2: {my_tuple.count(2)}\")       # Output: 3\nprint(f\"Count of 'a': {my_tuple.count('a')}\")   # Output: 2\n\nprint(f\"Index of 'b': {my_tuple.index('b')}\")   # Output: 3\nprint(f\"Index of first 2: {my_tuple.index(2)}\") # Output: 1\n\n# print(my_tuple.index('z')) # This would cause a ValueError"
            },
            {
                "id": "l8_tuple_challenge",
                "title": "Code: Create and Unpack Tuple",
                "type": "code",
                "explanation": [
                    "Create a tuple and then use unpacking to assign its elements to separate variables."
                ],
                "challenge": [
                    "1. Create a tuple named `user_info` containing three elements: the string \"Alice\", the integer 30, and the string \"New York\".",
                    "2. Use tuple unpacking to assign the elements of `user_info` to three variables: `name`, `age`, and `city`.",
                    "3. Print the value of the `age` variable.",
                    "4. On a new line, print the value of the `city` variable."
                ],
                "expected_stdout": "30\nNew York\n"
            },
            {
                "id": "l8_quiz",
                "title": "Quiz: Tuples",
                "type": "quiz",
                "question": "Which of the following statements about tuples is FALSE?",
                "options": [
                    "Tuples are ordered sequences.",
                    "Tuples can contain items of different data types.",
                    "Tuples are mutable (can be changed after creation).",
                    "Tuples can be used as dictionary keys."
                ],
                "correct_answer": 2 # Tuples are immutable
            }
        ]
    },
    {
        "id": "mod_sets",
        "title": "Module 9: Sets",
        "lessons": [
            {
                "id": "l9_intro",
                "title": "Introduction to Sets",
                "type": "explanation",
                "text": [
                    "Sets are **unordered** collections of **unique** items.",
                    "Unordered means items are not stored in a specific sequence, so you cannot access them by index.",
                    "Unique means a set cannot contain duplicate elements.",
                    "Sets are mutable (you can add or remove items).",
                    "They are created using curly braces `{}` or the `set()` function.",
                    "**Important:** To create an empty set, you *must* use `set()`, because `{}` creates an empty dictionary.",
                    "Sets are highly optimized for membership testing (`in`) and removing duplicates."
                ],
                "example": "# Creating sets\nfruits = {\"apple\", \"banana\", \"cherry\"}\nprint(fruits)\n\n# Duplicates are automatically removed\nnumbers = {1, 2, 2, 3, 4, 4, 4}\nprint(numbers) # Output: {1, 2, 3, 4}\n\n# Creating a set from a list (removes duplicates)\nmy_list = [1, 'a', 1, 'b', 'a']\nmy_set = set(my_list)\nprint(my_set) # Output: {1, 'a', 'b'} or {'a', 1, 'b'} etc. (order may vary)\n\n# Empty set\nempty_s = set()\nprint(empty_s)\n\n# Empty dictionary (for comparison)\nempty_d = {}\nprint(empty_d)\n\n# Membership testing (fast!)\nprint(f\"'apple' in fruits: {'apple' in fruits}\")\nprint(f\"'orange' in fruits: {'orange' in fruits}\")\n\n# Cannot index\n# print(fruits[0]) # This will cause a TypeError"
            },
            {
                "id": "l9_add_remove",
                "title": "Adding and Removing Set Items",
                "type": "explanation",
                "text": [
                    "Sets are mutable, so you can add and remove elements.",
                    "Methods for modification:",
                    "  - `.add(element)`: Adds a single element to the set. If the element is already present, the set remains unchanged.",
                    "  - `.update(iterable)`: Adds all elements from an iterable (like a list, tuple, or another set) to the set.",
                    "  - `.remove(element)`: Removes the specified element. Raises a `KeyError` if the element is not found.",
                    "  - `.discard(element)`: Removes the specified element *if it is present*. Does **not** raise an error if the element is not found.",
                    "  - `.pop()`: Removes and returns an *arbitrary* element from the set. Raises `KeyError` if the set is empty.",
                    "  - `.clear()`: Removes all elements from the set."
                ],
                "example": "s = {1, 2, 3}\nprint(f\"Original: {s}\")\n\ns.add(4)\nprint(f\"After add(4): {s}\")\n\ns.add(2) # Adding existing element does nothing\nprint(f\"After add(2): {s}\")\n\ns.update([3, 4, 5, 6])\nprint(f\"After update([3, 4, 5, 6]): {s}\")\n\ns.remove(1)\nprint(f\"After remove(1): {s}\")\n# s.remove(10) # This would cause KeyError\n\ns.discard(2)\nprint(f\"After discard(2): {s}\")\ns.discard(10) # No error if element doesn't exist\nprint(f\"After discard(10): {s}\")\n\npopped_item = s.pop()\nprint(f\"After pop(): {s}\")\nprint(f\"Popped item: {popped_item}\")\n\ns.clear()\nprint(f\"After clear(): {s}\")"
            },
            {
                "id": "l9_operations",
                "title": "Set Operations",
                "type": "explanation",
                "text": [
                    "Sets support mathematical operations like union, intersection, difference, etc.",
                    "These can be performed using operators or methods:",
                    "  - **Union (`|` or `.union()`):** Returns a new set with all elements from *both* sets.",
                    "  - **Intersection (`&` or `.intersection()`):** Returns a new set with elements common to *both* sets.",
                    "  - **Difference (`-` or `.difference()`):** Returns a new set with elements in the first set but *not* in the second.",
                    "  - **Symmetric Difference (`^` or `.symmetric_difference()`):** Returns a new set with elements in *either* set, but *not both*.",
                    "There are also methods like `.issubset()`, `.issuperset()`, and `.isdisjoint()` for checking relationships between sets."
                ],
                "example": "set_a = {1, 2, 3, 4}\nset_b = {3, 4, 5, 6}\n\n# Union\nunion_set = set_a | set_b\nprint(f\"Union (A | B): {union_set}\") # {1, 2, 3, 4, 5, 6}\n\n# Intersection\nintersection_set = set_a & set_b\nprint(f\"Intersection (A & B): {intersection_set}\") # {3, 4}\n\n# Difference (A - B)\ndiff_a_b = set_a - set_b\nprint(f\"Difference (A - B): {diff_a_b}\") # {1, 2}\n\n# Difference (B - A)\ndiff_b_a = set_b - set_a\nprint(f\"Difference (B - A): {diff_b_a}\") # {5, 6}\n\n# Symmetric Difference\nsym_diff = set_a ^ set_b\nprint(f\"Symmetric Difference (A ^ B): {sym_diff}\") # {1, 2, 5, 6}\n\n# Subset/Superset checks\nset_c = {1, 2}\nprint(f\"Is C subset of A? {set_c.issubset(set_a)}\") # True\nprint(f\"Is A superset of C? {set_a.issuperset(set_c)}\") # True\n\n# Disjoint check (no common elements)\nset_d = {10, 11}\nprint(f\"Are A and D disjoint? {set_a.isdisjoint(set_d)}\") # True"
            },
            {
                "id": "l9_set_challenge_basics",
                "title": "Code: Set Basics",
                "type": "code",
                "explanation": [
                    "Practice creating a set, adding an element, removing an element using a safe method, and checking for membership."
                ],
                "challenge": [
                    "1. Create a set named `colors` containing \"red\", \"green\", \"blue\".",
                    "2. Add the color \"yellow\" to the set.",
                    "3. Use the `.discard()` method to remove \"green\".",
                    "4. Check if \"red\" is present in the `colors` set and print the boolean result (`True` or `False`).",
                    "5. Finally, print the number of elements currently in the `colors` set using `len()`."
                ],
                "expected_stdout": "True\n3\n" # {"red", "blue", "yellow"} -> "red" is True, length is 3
            },
            {
                "id": "l9_set_challenge_ops",
                "title": "Code: Find Common Items",
                "type": "code",
                "explanation": [
                    "Use set operations (specifically intersection) to efficiently find common elements between two lists.",
                    "Remember to convert the lists to sets first."
                ],
                "challenge": [
                    "1. Create a list `list1 = [1, 2, 3, 4, 5]`.",
                    "2. Create another list `list2 = [4, 5, 6, 7, 8]`.",
                    "3. Convert both lists into sets.",
                    "4. Find the intersection of the two sets (the common elements).",
                    "5. Convert the resulting intersection set back into a list.",
                    "6. Sort the final list in ascending order.",
                    "7. Print the sorted list of common elements."
                ],
                "expected_stdout": "[4, 5]\n" # Intersection is {4, 5}, sorted list is [4, 5]
            },
            {
                "id": "l9_quiz",
                "title": "Quiz: Sets",
                "type": "quiz",
                "question": "What is the primary characteristic that distinguishes sets from lists and tuples?",
                "options": [
                    "Sets are ordered.",
                    "Sets can contain duplicate elements.",
                    "Sets only contain unique elements and are unordered.",
                    "Sets are immutable."
                ],
                "correct_answer": 2 # Unique elements and unordered are key characteristics
            }
        ]
    },
    {
        "id": "mod_functions",
        "title": "Module 10: Functions",
        "lessons": [
            {
                "id": "l10_intro",
                "title": "Introduction to Functions",
                "type": "explanation",
                "text": [
                    "Functions are named blocks of reusable code that perform a specific task.",
                    "They help organize code, make it more readable, and avoid repetition (DRY - Don't Repeat Yourself).",
                    "You **define** a function using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`.",
                    "The code block inside the function must be indented.",
                    "You **call** (or execute) a function by using its name followed by parentheses `()`."
                ],
                "example": "# Define a simple function\ndef greet():\n    print(\"Hello from the function!\")\n    print(\"Welcome.\")\n\n# Call the function\nprint(\"Calling the function now...\")\ngreet() # This executes the code inside greet()\nprint(\"Function call finished.\")\n\n# Call it again\ngreet()"
            },
            {
                "id": "l10_arguments",
                "title": "Functions with Arguments",
                "type": "explanation",
                "text": [
                    "Functions can accept input values, called **arguments** (or parameters).",
                    "You define parameters within the parentheses `()` in the function definition.",
                    "When you call the function, you pass the actual values (arguments) inside the parentheses.",
                    "These arguments are assigned to the corresponding parameters within the function's scope."
                ],
                "example": "# Define a function that takes one argument\ndef greet_user(name): # 'name' is the parameter\n    print(f\"Hello, {name}!\")\n\n# Call the function with different arguments\ngreet_user(\"Alice\") # \"Alice\" is the argument\ngreet_user(\"Bob\")\n\n# Define a function that takes two arguments\ndef add_numbers(num1, num2):\n    result = num1 + num2\n    print(f\"The sum of {num1} and {num2} is: {result}\")\n\nadd_numbers(5, 3)\nadd_numbers(10, -2)"
            },
            {
                "id": "l10_return",
                "title": "Return Values from Functions",
                "type": "explanation",
                "text": [
                    "Functions can send a result back to the part of the code that called them using the `return` statement.",
                    "When `return` is executed, the function immediately stops, and the specified value is sent back.",
                    "If a function doesn't have a `return` statement, or just has `return` with no value, it implicitly returns `None`.",
                    "The returned value can be stored in a variable or used directly in expressions."
                ],
                "example": "# Function that returns a value\ndef multiply(x, y):\n    product = x * y\n    return product # Send the result back\n\n# Call the function and store the result\nresult = multiply(4, 6)\nprint(f\"Result from multiply(4, 6): {result}\")\n\n# Use the return value directly\nprint(f\"Double the result: {multiply(4, 6) * 2}\")\n\n# Function that returns None implicitly\ndef print_message(msg):\n    print(msg)\n    # No return statement here\n\nreturned_value = print_message(\"Test message\")\nprint(f\"Value returned from print_message: {returned_value}\") # Output: None"
            },
            {
                "id": "l10_define_call_challenge",
                "title": "Code: Define and Call",
                "type": "code",
                "explanation": [
                    "Define a basic function using `def` and then call it to execute its code."
                ],
                "challenge": [
                    "1. Define a function named `display_message`.",
                    "2. Inside the function, write a `print()` statement that outputs the exact text: \"Learning functions is fun!\"",
                    "3. After defining the function, call `display_message()` to run it."
                ],
                "expected_stdout": "Learning functions is fun!\n"
            },
            {
                "id": "l10_arg_return_challenge",
                "title": "Code: Argument and Return",
                "type": "code",
                "explanation": [
                    "Define a function that takes an argument, performs a simple calculation, and returns the result.",
                    "Then call the function and print the returned value."
                ],
                "challenge": [
                    "1. Define a function named `square` that takes one argument (a number).",
                    "2. Inside the function, calculate the square of the argument (number * number).",
                    "3. Use the `return` statement to send the calculated square back.",
                    "4. Call the `square` function with the argument `5`.",
                    "5. Store the returned value in a variable named `result`.",
                    "6. Print the value of the `result` variable."
                ],
                "expected_stdout": "25\n"
            },
            {
                "id": "l10_scope",
                "title": "Variable Scope (Basic)",
                "type": "explanation",
                "text": [
                    "**Scope** refers to the region of your code where a variable can be accessed.",
                    "Variables defined *inside* a function have **local scope**. They only exist within that function and cannot be accessed from outside.",
                    "Variables defined *outside* any function have **global scope**. They can generally be accessed from anywhere, including inside functions (though modifying globals inside functions requires the `global` keyword, which is often discouraged).",
                    "Function parameters also have local scope within that function."
                ],
                "example": "global_var = 100 # Global variable\n\ndef my_function(param):\n    local_var = 10 # Local variable\n    print(f\"Inside function: global_var = {global_var}\") # Can access global\n    print(f\"Inside function: param = {param}\")       # Can access parameter\n    print(f\"Inside function: local_var = {local_var}\") # Can access local\n\nprint(f\"Outside function: global_var = {global_var}\")\n\nmy_function(5) # Call the function\n\n# Trying to access local variables outside the function causes an error\n# print(f\"Outside function: param = {param}\")     # NameError\n# print(f\"Outside function: local_var = {local_var}\") # NameError"
            },
            {
                "id": "l10_quiz",
                "title": "Quiz: Functions",
                "type": "quiz",
                "question": "What keyword is used to define a new function in Python?",
                "options": [
                    "function",
                    "define",
                    "def",
                    "fun"
                ],
                "correct_answer": 2
            },
            {
                "id": "l10_return_quiz",
                "title": "Quiz: Return Values",
                "type": "quiz",
                "question": "What value does a Python function return if it doesn't have an explicit `return` statement?",
                "options": [
                    "0",
                    "False",
                    "An empty string ''",
                    "None"
                ],
                "correct_answer": 3
            }
        ]
    },
    {
        "id": "mod_files",
        "title": "Module 11: Basic File I/O",
        "lessons": [
            {
                "id": "l11_intro",
                "title": "Introduction to File I/O",
                "type": "explanation",
                "text": [
                    "File Input/Output (I/O) allows your Python programs to read data from files and write data to files.",
                    "This is crucial for data persistence – saving information so it's not lost when your program closes.",
                    "You can work with various file types, most commonly text files (.txt, .csv, .py, etc.).",
                    "Key operations involve opening, reading, writing, appending, and closing files."
                ]
            },
            {
                "id": "l11_open_with",
                "title": "Opening Files with open() and 'with'",
                "type": "explanation",
                "text": [
                    "The built-in `open()` function is used to open a file and returns a file object.",
                    "Syntax: `open(filename, mode)`",
                    "  - `filename`: The path to the file (e.g., 'my_data.txt').",
                    "  - `mode`: A string indicating how the file will be used. Common modes:",
                    "    - `'r'`: Read (default). Opens for reading. Error if file doesn't exist.",
                    "    - `'w'`: Write. Opens for writing. Creates the file if it doesn't exist, **overwrites** it if it does.",
                    "    - `'a'`: Append. Opens for writing, adding to the end. Creates file if it doesn't exist.",
                    "    - `'r+'`: Read and Write.",
                    "    - `'b'`: Binary mode (add to other modes, e.g., 'rb', 'wb'). For non-text files.",
                    "    - `'x'`: Exclusive creation. Fails if the file already exists.",
                    "",
                    "**Best Practice: Using `with` Statement**",
                    "The `with open(...) as file_variable:` syntax is recommended.",
                    "It automatically handles closing the file, even if errors occur within the block.",
                    "This prevents resource leaks."
                ],
                "example": "# Recommended way using 'with'\n# Example assumes 'example.txt' exists for reading\n# with open('example.txt', 'r') as f:\n#     content = f.read()\n#     print(\"Read content:\", content)\n\n# Example for writing (will create or overwrite 'output.txt')\ntry:\n    with open('output.txt', 'w') as outfile:\n        outfile.write(\"This will be written to the file.\\n\")\n    print(\"Successfully wrote to output.txt (using 'with')\")\nexcept IOError as e:\n    print(f\"Error writing to file: {e}\")\n\n# Example for appending\ntry:\n    with open('output.txt', 'a') as outfile:\n        outfile.write(\"This will be appended.\\n\")\n    print(\"Successfully appended to output.txt (using 'with')\")\nexcept IOError as e:\n    print(f\"Error appending to file: {e}\")\n\n# Old way (requires manual closing - less safe)\n# file = open('output.txt', 'r')\n# content = file.read()\n# file.close() # Must remember to close!"
            },
            {
                "id": "l11_reading",
                "title": "Reading from Files",
                "type": "explanation",
                "text": [
                    "Once a file is opened in read mode (`'r'`), you can read its contents:",
                    "  - `file.read()`: Reads the entire content of the file into a single string.",
                    "  - `file.read(size)`: Reads at most `size` bytes (or characters in text mode).",
                    "  - `file.readline()`: Reads a single line (including the newline `\\n` at the end) until the next newline or end-of-file.",
                    "  - `file.readlines()`: Reads all lines into a list of strings, each string including its newline.",
                    "  - **Iterating directly over the file object:** This is memory-efficient for large files, as it reads line by line.",
                    "    ```python",
                    "    with open('myfile.txt', 'r') as f:",
                    "        for line in f:",
                    "            print(line.strip()) # Process line",
                    "    ```"
                ],
                                "example": '''# "Setup: Create a dummy file to read from (will be removed after)
                                                setup_code = """
                                                with open("dummy_read.txt", "w") as f:
                                                    f.write("First line.\\n")
                                                    f.write("Second line here.\\n")
                                                    f.write("Third and final line.\\n")
                                                """
                                                import os
                                                try:
                                                    exec(setup_code)

                                                    print("--- Reading entire file with read() ---")
                                                    with open("dummy_read.txt", "r") as f:
                                                        content = f.read()
                                                        print(repr(content)) # Use repr to show newlines

                                                    print("\\n--- Reading line by line with readline() ---")
                                                    with open("dummy_read.txt", "r") as f:
                                                        line1 = f.readline()
                                                        print(repr(line1))
                                                        line2 = f.readline()
                                                        print(repr(line2))

                                                    print("\\n--- Reading all lines with readlines() ---")
                                                    with open("dummy_read.txt", "r") as f:
                                                        lines_list = f.readlines()
                                                        print(lines_list)

                                                    print("\\n--- Iterating directly over the file ---")
                                                    with open("dummy_read.txt", "r") as f:
                                                        for i, line in enumerate(f):
                                                            print(f"Line {i+1}: {line.strip()}") # Strip removes leading/trailing whitespace/newlines

                                                finally:
                                                    # Clean up the dummy file
                                                    if os.path.exists("dummy_read.txt"):
                                                        os.remove("dummy_read.txt")
                                                '''
            },
            {
                "id": "l11_read_challenge",
                "title": "Code: Read Specific Line",
                "type": "code",
                # Inject setup code to create the file the user needs to read
                "setup_code": "with open('sample_data.txt', 'w') as f:\n    f.write('Apple\\n')\n    f.write('Banana\\n')\n    f.write('Cherry\\n')",
                "explanation": [
                    "Practice opening a file, reading its contents, and accessing a specific part.",
                    "Using `readlines()` or iterating are common ways to handle lines."
                ],
                "challenge": [
                    "A file named `sample_data.txt` has been created with the following content:",
                    "```",
                    "Apple",
                    "Banana",
                    "Cherry",
                    "```",
                    "(Each word is on its own line).",
                    "1. Write Python code to open `sample_data.txt` in read mode.",
                    "2. Read all the lines from the file.",
                    "3. Print only the second line from the file (which should be 'Banana'). Make sure to include the newline character that's part of the line."
                ],
                # The second line read by readlines() will be 'Banana\n'
                "expected_stdout": "Banana\n"
            },
            {
                "id": "l11_writing_appending",
                "title": "Writing and Appending to Files",
                "type": "explanation",
                "text": [
                    "To write data, open the file in write (`'w'`) or append (`'a'`) mode.",
                    "  - `file.write(string)`: Writes the given `string` to the file. It does **not** automatically add a newline character (`\\n`), you must include it if needed.",
                    "  - `file.writelines(list_of_strings)`: Writes each string from the list to the file. Again, newlines are usually needed within the strings.",
                    "",
                    "**Key Differences:**",
                    "  - **Write (`'w'`)**: If the file exists, its **entire content is erased** before writing begins. If it doesn't exist, it's created.",
                    "  - **Append (`'a'`)**: If the file exists, new data is added to the **end** of the file. If it doesn't exist, it's created.",
                    "Remember to use the `with` statement for safety!"
                ],
                "example": "# -- Writing Example ('w' mode) --\ntry:\n    with open('write_example.txt', 'w') as f:\n        f.write(\"Hello from Python!\\n\")\n        f.write(\"This is the second line.\\n\")\n        lines_to_write = [\"Third line.\\n\", \"Fourth line.\\n\"]\n        f.writelines(lines_to_write)\n    print(\"write_example.txt created/overwritten.\")\n\n    # Verify writing\n    with open('write_example.txt', 'r') as f:\n        print(\"Content of write_example.txt:\")\n        print(f.read())\n\nexcept IOError as e:\n    print(f\"Error writing: {e}\")\n\n# -- Appending Example ('a' mode) --\ntry:\n    with open('write_example.txt', 'a') as f:\n        f.write(\"--- Appended Content ---\\n\")\n        f.write(\"This line was appended.\\n\")\n    print(\"\\nContent appended to write_example.txt.\")\n\n    # Verify appending\n    with open('write_example.txt', 'r') as f:\n        print(\"New content of write_example.txt:\")\n        print(f.read())\n\nexcept IOError as e:\n    print(f\"Error appending: {e}\")\nfinally:\n    # Clean up\n    import os\n    if os.path.exists('write_example.txt'):\n        os.remove('write_example.txt')\n"
            },
            {
                "id": "l11_write_append_challenge",
                "title": "Code: Write and Append",
                "type": "code",
                "setup_code": "# No setup needed, the code will create the file.\n# We will check the file content after execution.",
                "explanation": [
                    "Practice writing to a new file and then appending to that same file.",
                    "Remember the difference between 'w' and 'a' modes.",
                    "The verification process will check the final content of the file created by your code."
                ],
                "challenge": [
                    "1. Write Python code to open a file named `log.txt` in write mode (`'w'`).",
                    "2. Write the exact string `\"Log Start\\n\"` to the file.",
                    "3. Close the file (implicitly using `with` is best).",
                    "4. Open the same file (`log.txt`) again, this time in append mode (`'a'`).",
                    "5. Write the exact string `\"Event 1 Occurred\\n\"` to the file.",
                    "6. Close the file.",
                    "7. Finally, open `log.txt` one more time in read mode (`'r'`).",
                    "8. Read the *entire* content of the file into a variable.",
                    "9. Print the content you just read."
                ],
                # Expected output is the final content of the file printed to stdout
                "expected_stdout": "Log Start\nEvent 1 Occurred\n"
            },
            {
                "id": "l11_quiz",
                "title": "Quiz: File Modes",
                "type": "quiz",
                "question": "Which file mode should you use if you want to add data to the end of an existing file without deleting its current contents?",
                "options": [
                    "'r' (Read)",
                    "'w' (Write)",
                    "'a' (Append)",
                    "'x' (Exclusive creation)"
                ],
                "correct_answer": 2 # 'a' for append
            },
             {
                "id": "l11_quiz_with",
                "title": "Quiz: The 'with' Statement",
                "type": "quiz",
                "question": "What is the primary benefit of using the `with open(...) as ...:` statement for file handling?",
                "options": [
                    "It makes the code run faster.",
                    "It automatically creates the file if it doesn't exist.",
                    "It ensures the file is automatically and safely closed, even if errors occur.",
                    "It reads the entire file into memory at once."
                ],
                "correct_answer": 2 # Automatic closing is the main benefit
            }
        ]
    },
    {
        "id": "mod_errors",
        "title": "Module 12: Error Handling (try/except)",
        "lessons": [
            {
                "id": "l12_intro_errors",
                "title": "Understanding Errors",
                "type": "explanation",
                "text": [
                    "Errors, also called **exceptions**, occur when something goes wrong during program execution.",
                    "Python stops and prints a **traceback** showing where the error occurred.",
                    "Common types of errors:",
                    "  - `SyntaxError`: Code doesn't follow Python's grammar (caught before execution).",
                    "  - `NameError`: Using a variable or function name that hasn't been defined.",
                    "  - `TypeError`: Performing an operation on an inappropriate data type (e.g., `len(123)`).",
                    "  - `ValueError`: Function receives an argument of the correct type but an inappropriate value (e.g., `int('abc')`).",
                    "  - `IndexError`: Trying to access a list/string index that doesn't exist.",
                    "  - `KeyError`: Trying to access a dictionary key that doesn't exist.",
                    "  - `FileNotFoundError`: Trying to open a file that doesn't exist.",
                    "Understanding tracebacks helps you debug your code."
                ],
                "example": "# Example that would cause a NameError if run:\n# print(undefined_variable)\n\n# Example that would cause a TypeError if run:\n# result = 'hello' + 5\n\n# Example that would cause an IndexError if run:\n# my_list = [1, 2]\n# print(my_list[5])"
            },
            {
                "id": "l12_try_except",
                "title": "Handling Errors with 'try...except'",
                "type": "explanation",
                "text": [
                    "To prevent your program from crashing due to runtime errors, you can use a `try...except` block.",
                    "Python *tries* to execute the code inside the `try` block.",
                    "If an error (exception) occurs within the `try` block, Python immediately jumps to the `except` block.",
                    "The code inside the `except` block is then executed, handling the error gracefully.",
                    "If no error occurs in the `try` block, the `except` block is skipped entirely."
                ],
                "example": "try:\n    num_str = input(\"Enter a number: \")\n    num_int = int(num_str) # This might cause a ValueError\n    print(f\"You entered the number: {num_int}\")\nexcept ValueError:\n    # This block runs ONLY if int() fails\n    print(\"That wasn't a valid integer!\")\n\nprint(\"Program continues after the try-except block...\")"
            },
            {
                "id": "l12_except_specific",
                "title": "Handling Specific Exceptions",
                "type": "explanation",
                "text": [
                    "You can handle different types of errors separately by specifying the exception type after `except`.",
                    "Syntax: `except ExceptionType:`",
                    "You can have multiple `except` blocks to handle various potential errors.",
                    "You can also catch multiple exceptions in one block using a tuple: `except (ValueError, TypeError):`",
                    "A generic `except:` block (without specifying a type) will catch *any* exception. This is generally discouraged unless you know exactly why you need it, as it can hide unexpected errors."
                ],
                "example": "try:\n    x = int(input(\"Enter numerator: \"))\n    y = int(input(\"Enter denominator: \"))\n    result = x / y # Potential ValueError or ZeroDivisionError\n    print(f\"Result: {result}\")\n\nexcept ValueError:\n    print(\"Please enter valid integers only.\")\n\nexcept ZeroDivisionError:\n    print(\"Cannot divide by zero!\")\n\nexcept Exception as e: # Catch any other unexpected error\n    print(f\"An unexpected error occurred: {e}\")"
            },
            {
                "id": "l12_else_finally",
                "title": "The 'else' and 'finally' Clauses",
                "type": "explanation",
                "text": [
                    "The `try...except` structure can optionally include `else` and `finally` blocks.",
                    "  - `else`: The code in the `else` block runs **only if** the `try` block completes *without* raising any exceptions.",
                    "  - `finally`: The code in the `finally` block runs **always**, regardless of whether an exception occurred in `try` or was handled by `except`, or if `else` ran. It's typically used for cleanup actions (like closing files or network connections)."
                ],
                "example": "file = None # Initialize file variable\ntry:\n    file_path = 'data.txt' # Assume this exists for success case\n    # In a real scenario, we might create data.txt first\n    # Let's simulate its existence for the 'else' path first\n    try:\n        with open('data.txt', 'w') as f: f.write('Sample data')\n    except: pass # Ignore if creation fails, just for demo\n\n    file = open(file_path, 'r')\n    content = file.read()\n    print(\"File opened and read successfully.\")\n\nexcept FileNotFoundError:\n    print(f\"Error: File '{file_path}' not found.\")\n\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n\nelse:\n    # Runs only if try block succeeds\n    print(\"--- Else block executed --- \")\n    print(f\"File content: '{content}'\")\n\nfinally:\n    # Runs no matter what happened before\n    print(\"--- Finally block executed --- \")\n    if file:\n        file.close()\n        print(\"File closed.\")\n    else:\n        print(\"No file was opened.\")\n\n# Clean up the demo file\nimport os\nif os.path.exists('data.txt'): os.remove('data.txt')"
            },
            {
                "id": "l12_raise",
                "title": "Raising Exceptions with 'raise'",
                "type": "explanation",
                "text": [
                    "You can manually trigger an exception using the `raise` statement.",
                    "This is useful when you detect an error condition in your code that prevents it from proceeding correctly.",
                    "You can raise built-in exceptions or define your own custom exception types (more advanced).",
                    "Syntax: `raise ExceptionType(\"Optional error message\")`"
                ],
                "example": "def calculate_discount(price, discount_percent):\n    if not 0 <= discount_percent <= 100:\n        # Raise an error if the discount is invalid\n        raise ValueError(\"Discount percentage must be between 0 and 100.\")\n    \n    discount_amount = price * (discount_percent / 100)\n    return price - discount_amount\n\ntry:\n    final_price = calculate_discount(50, 110) # Invalid discount\n    print(f\"Final price: {final_price}\")\nexcept ValueError as e:\n    print(f\"Error calculating discount: {e}\") # Catches the raised error\n\ntry:\n    final_price = calculate_discount(50, 10) # Valid discount\n    print(f\"Final price (valid): {final_price}\")\nexcept ValueError as e:\n    print(f\"Error calculating discount: {e}\")"
            },
            {
                "id": "l12_try_challenge",
                "title": "Code: Handle Input Error",
                "type": "code",
                "explanation": [
                    "Practice using `try...except ValueError` to handle cases where user input cannot be converted to an integer."
                ],
                "challenge": [
                    "1. Ask the user to enter their age using `input()`. Store the result in a variable.",
                    "2. Use a `try` block to attempt converting the input string to an integer using `int()`.",
                    "3. If the conversion is successful, print the message: `\"Age successfully entered: [age]\"` (replace [age] with the integer value).",
                    "4. Use an `except ValueError` block.",
                    "5. If a `ValueError` occurs during conversion, print the message: `\"Invalid input. Please enter a number.\"`"
                ],
                "expected_stdout": "Invalid input. Please enter a number.\n" # Assumes non-numeric input for testing this path
                # Note: Testing this fully requires simulating user input. The expected_stdout
                # assumes the error path is tested. A successful input (e.g., "30") would
                # result in "Age successfully entered: 30\n". The testing framework should ideally
                # be able to test both scenarios if possible. For now, we test the error path.
            },
            {
                "id": "l12_file_error_challenge",
                "title": "Code: Handle File Not Found",
                "type": "code",
                "setup_code": "# Ensure the file does NOT exist for the test\nimport os\nif os.path.exists('non_existent_file.txt'):\n    os.remove('non_existent_file.txt')",
                "explanation": [
                    "Use `try...except FileNotFoundError` to gracefully handle attempts to open files that don't exist."
                ],
                "challenge": [
                    "1. Use a `try` block to attempt opening a file named `\"non_existent_file.txt\"` in read mode (`'r'`) using `with open(...)`.",
                    "2. Inside the `try` block (after the `with` statement, though it won't be reached if the file doesn't exist), add a `print(\"File opened successfully.\")` statement.",
                    "3. Use an `except FileNotFoundError` block.",
                    "4. Inside the `except` block, print the message: `\"Error: The file was not found.\"`"
                ],
                "expected_stdout": "Error: The file was not found.\n"
            },
            {
                "id": "l12_quiz",
                "title": "Quiz: Error Handling",
                "type": "quiz",
                "question": "Which block of code in a `try...except...finally` structure is guaranteed to execute, regardless of whether an error occurred?",
                "options": [
                    "try",
                    "except",
                    "else",
                    "finally"
                ],
                "correct_answer": 3 # finally always runs
            }
        ]
    },
    {
        "id": "mod_modules_packages",
        "title": "Module 13: Modules and Packages",
        "lessons": [
            {
                "id": "l13_intro",
                "title": "Introduction to Modules",
                "type": "explanation",
                "text": [
                    "As programs grow, it's useful to split code into multiple files called **modules**.",
                    "A module is simply a Python file (`.py`) containing Python definitions and statements (functions, classes, variables).",
                    "Modules allow you to:",
                    "  - Organize your code logically.",
                    "  - Reuse code across different programs.",
                    "  - Avoid naming conflicts.",
                    "Python comes with a rich **Standard Library** of built-in modules providing tools for common tasks."
                ]
            },
            {
                "id": "l13_import",
                "title": "Using 'import'",
                "type": "explanation",
                "text": [
                    "To use the code defined in a module, you need to **import** it into your current script.",
                    "The simplest way is `import module_name`.",
                    "After importing, you access the functions, classes, or variables within that module using **dot notation**:",
                    "`module_name.function_name()` or `module_name.variable_name`."
                ],
                "example": "# Import the built-in 'math' module\nimport math\n\n# Use functions from the math module\npi_value = math.pi\nsquare_root = math.sqrt(16)\n\nprint(f\"The value of Pi is approximately: {pi_value}\")\nprint(f\"The square root of 16 is: {square_root}\")\n\n# Import the built-in 'random' module\nimport random\n\nrandom_number = random.randint(1, 10) # Get random integer between 1 and 10\nprint(f\"A random number: {random_number}\")"
            },
            {
                "id": "l13_from_import",
                "title": "Using 'from...import'",
                "type": "explanation",
                "text": [
                    "Instead of importing the entire module, you can import specific names (functions, variables, classes) directly into your current script's namespace using `from module_name import name1, name2`.",
                    "This allows you to use the imported names directly without the module prefix.",
                    "You can import all names using `from module_name import *`, but this is generally **discouraged** as it can lead to naming conflicts and make code harder to read (it's unclear where names came from)."
                ],
                "example": "# Import specific functions from the 'math' module\nfrom math import pi, sqrt\n\n# Use the imported functions directly\nprint(f\"Pi: {pi}\")\nprint(f\"Square root of 25: {sqrt(25)}\")\n\n# Import a specific function from 'random'\nfrom random import choice\n\nmy_list = ['apple', 'banana', 'cherry']\nrandom_fruit = choice(my_list)\nprint(f\"Random fruit: {random_fruit}\")\n\n# Example of discouraged 'import *' (don't do this often!)\n# from math import *\n# print(cos(0)) # Works, but where did cos come from?"
            },
            {
                "id": "l13_import_as",
                "title": "Using Aliases with 'as'",
                "type": "explanation",
                "text": [
                    "You can provide an **alias** (an alternative, often shorter name) when importing a module or specific names using the `as` keyword.",
                    "This is useful for:",
                    "  - Avoiding naming conflicts.",
                    "  - Shortening long module names.",
                    "Syntax:",
                    "  `import module_name as alias`",
                    "  `from module_name import name as alias`"
                ],
                "example": "# Import 'math' module with an alias 'm'\nimport math as m\n\nprint(f\"Using alias: sqrt(36) = {m.sqrt(36)}\")\n\n# Import a specific function with an alias\nfrom random import randint as generate_random_integer\n\nrandom_int = generate_random_integer(100, 200)\nprint(f\"Random integer between 100 and 200: {random_int}\")"
            },
            {
                "id": "l13_standard_library",
                "title": "Exploring the Standard Library",
                "type": "explanation",
                "text": [
                    "Python's Standard Library is a vast collection of modules included with every Python installation.",
                    "It provides tools for many common programming tasks.",
                    "Some commonly used modules include:",
                    "  - `math`: Mathematical functions (trigonometry, logarithms, etc.).",
                    "  - `random`: Generating random numbers, choices, shuffling sequences.",
                    "  - `os`: Interacting with the operating system (file paths, directories).",
                    "  - `sys`: Accessing system-specific parameters and functions (command-line arguments, exit).",
                    "  - `datetime`: Working with dates and times.",
                    "  - `json`: Encoding and decoding JSON data.",
                    "  - `csv`: Reading and writing CSV files.",
                    "You can explore the full library documentation online."
                ],
                "example": "import os\nimport datetime\n\ncurrent_directory = os.getcwd() # Get current working directory\nprint(f\"Current directory: {current_directory}\")\n\nnow = datetime.datetime.now()\nprint(f\"Current date and time: {now}\")\nprint(f\"Current year: {now.year}\")"
            },
            {
                "id": "l13_pip",
                "title": "Third-Party Packages and 'pip'",
                "type": "explanation",
                "text": [
                    "Beyond the standard library, there's a huge ecosystem of **third-party packages** created by the Python community.",
                    "These packages offer functionality for web development, data science, game development, and much more.",
                    "The **Python Package Index (PyPI)** is the main repository for these packages.",
                    "You use the command-line tool **`pip`** (Pip Installs Packages) to install, upgrade, and manage these packages.",
                    "Common commands:",
                    "  - `pip install package_name`: Installs a package.",
                    "  - `pip install --upgrade package_name`: Upgrades a package.",
                    "  - `pip uninstall package_name`: Uninstalls a package.",
                    "  - `pip list`: Lists installed packages.",
                    "  - `pip freeze > requirements.txt`: Saves installed packages to a file.",
                    "  - `pip install -r requirements.txt`: Installs packages from a file.",
                    "(You typically run `pip` commands in your terminal/command prompt, not directly in a Python script)."
                ],
                 "example": "# You would run these in your terminal:\n# pip install requests\n# pip install numpy\n\n# Example of using an installed package (assumes 'requests' is installed)\n# import requests\n# try:\n#     response = requests.get('https://api.github.com')\n#     print(f\"GitHub API status code: {response.status_code}\")\n# except Exception as e:\n#     print(f\"Could not connect: {e}\")\n\nprint(\"Remember to run 'pip install <package>' in your terminal first!\")"
            },
            {
                "id": "l13_import_challenge",
                "title": "Code: Use the 'math' Module",
                "type": "code",
                "explanation": [
                    "Import the `math` module and use one of its functions."
                ],
                "challenge": [
                    "1. Import the `math` module.",
                    "2. Use the `math.pow()` function to calculate 3 raised to the power of 4 (3^4).",
                    "3. Print the result."
                ],
                "expected_stdout": "81.0\n" # math.pow returns a float
            },
            {
                "id": "l13_random_challenge",
                "title": "Code: Use 'from...import'",
                "type": "code",
                "explanation": [
                    "Use `from...import` to bring a specific function into your namespace and use it directly."
                ],
                "challenge": [
                    "1. From the `random` module, import only the `choice` function.",
                    "2. Create a list named `options` containing the strings: \"rock\", \"paper\", \"scissors\".",
                    "3. Use the `choice()` function to select a random element from the `options` list.",
                    "4. Print the selected option."
                ],
                # Output will vary, so can't use expected_stdout for verification easily.
                # Mark as complete upon execution without error, or maybe just practice?
                # For now, let's make it a practice exercise without strict output check.
                "expected_stdout": None # Indicates practice, no specific output needed
            },
            {
                "id": "l13_quiz",
                "title": "Quiz: Importing",
                "type": "quiz",
                "question": "If you import a module using `import my_module`, how do you call a function named `my_function` defined inside it?",
                "options": [
                    "my_function()",
                    "my_module.my_function()",
                    "my_module::my_function()",
                    "from my_module import my_function()"
                ],
                "correct_answer": 1 # Use dot notation module_name.function_name()
            }
        ]
    },
    {
        "id": "mod_oop",
        "title": "Module 14: Object-Oriented Programming (OOP)",
        "lessons": [
            {
                "id": "l14_oop_intro",
                "title": "Introduction to OOP Concepts",
                "type": "explanation",
                "text": [
                    "Object-Oriented Programming (OOP) is a programming paradigm based on the concept of 'objects'.",
                    "Objects can contain data (in the form of fields, often known as **attributes** or properties) and code (in the form of procedures, often known as **methods**).",
                    "Key principles of OOP include:",
                    "  - **Encapsulation:** Bundling data (attributes) and methods that operate on the data within a single unit (the object).",
                    "  - **Inheritance:** Allowing new classes (child/subclasses) to inherit properties and methods from existing classes (parent/superclasses).",
                    "  - **Polymorphism:** Allowing objects of different classes to respond to the same method call in different ways.",
                    "  - **Abstraction:** Hiding complex implementation details and exposing only the essential features of an object.",
                    "OOP helps in creating modular, reusable, and maintainable code, especially for larger applications."
                ]
            },
            {
                "id": "l14_classes",
                "title": "Defining Classes with 'class'",
                "type": "explanation",
                "text": [
                    "A **class** is a blueprint or template for creating objects.",
                    "It defines the attributes (data) and methods (behavior) that all objects of that class will have.",
                    "You define a class using the `class` keyword, followed by the class name (typically using CamelCase convention), and a colon `:`.",
                    "The code block inside the class definition must be indented.",
                    "An empty class is defined using the `pass` statement."
                ],
                "example": "# Define a simple empty class\nclass Dog:\n    pass\n\n# Define a class with a simple attribute\nclass Car:\n    # This is a class attribute (shared by all instances)\n    wheels = 4 \n\nprint(\"Class 'Dog' defined.\")\nprint(\"Class 'Car' defined.\")\nprint(f\"A car typically has {Car.wheels} wheels.\")"
            },
            {
                "id": "l14_objects",
                "title": "Creating Objects (Instances)",
                "type": "explanation",
                "text": [
                    "An **object** (or **instance**) is a specific realization of a class.",
                    "You create an object by calling the class name followed by parentheses `()`, similar to calling a function.",
                    "This process is called **instantiation**.",
                    "Each object created from a class is independent, although they share the structure defined by the class."
                ],
                "example": "class Dog:\n    pass # Simple empty class\n\n# Create two different Dog objects (instances)\nmy_dog = Dog()\nanother_dog = Dog()\n\nprint(f\"my_dog is an object of type: {type(my_dog)}\")\nprint(f\"another_dog is an object of type: {type(another_dog)}\")\n\n# Check if they are the same object (they are not)\nprint(f\"Are my_dog and another_dog the same object? {my_dog is another_dog}\")"
            },
            {
                "id": "l14_init",
                "title": "The __init__() Method (Constructor)",
                "type": "explanation",
                "text": [
                    "The `__init__()` method is a special method in Python classes.",
                    "It acts as the **constructor** and is automatically called when you create a new object (instance) of the class.",
                    "It's commonly used to initialize the **instance attributes** (data specific to each object).",
                    "The first parameter of `__init__` (and most instance methods) is always `self`, which refers to the instance being created.",
                    "You pass arguments to `__init__` when you create the object.",
                ],
                "example": "class Cat:\n    # Constructor method\n    def __init__(self, name, color):\n        print(f\"Creating a new Cat object!\")\n        # Assign the passed arguments to instance attributes\n        self.name = name \n        self.color = color\n\n# Create Cat instances, passing arguments to __init__\ncat1 = Cat(\"Whiskers\", \"Gray\")\ncat2 = Cat(\"Shadow\", \"Black\")\n\n# Access the instance attributes using dot notation\nprint(f\"Cat 1's name: {cat1.name}, Color: {cat1.color}\")\nprint(f\"Cat 2's name: {cat2.name}, Color: {cat2.color}\")"
            },
             {
                "id": "l14_attributes",
                "title": "Instance Attributes",
                "type": "explanation",
                "text": [
                    "**Instance attributes** are variables that belong to a specific instance (object) of a class.",
                    "Each object can have its own unique values for these attributes.",
                    "They are typically defined within the `__init__` method using `self.attribute_name = value`.",
                    "You access or modify instance attributes using dot notation: `object_name.attribute_name`."
                ],
                "example": "class Book:\n    def __init__(self, title, author):\n        self.title = title     # Instance attribute\n        self.author = author   # Instance attribute\n        self.is_lent = False # Default instance attribute\n\nbook1 = Book(\"The Hobbit\", \"J.R.R. Tolkien\")\nbook2 = Book(\"1984\", \"George Orwell\")\n\nprint(f\"Book 1: {book1.title} by {book1.author} (Lent: {book1.is_lent})\")\n\n# Modify an attribute for a specific instance\nbook1.is_lent = True\nprint(f\"Book 1 is now lent out: {book1.is_lent}\")\n\n# book2's attribute remains unchanged\nprint(f\"Book 2: {book2.title} (Lent: {book2.is_lent})\")"
            },
            {
                "id": "l14_attribute_challenge",
                "title": "Code: Create Class with Attributes",
                "type": "code",
                "explanation": [
                    "Define a class with an `__init__` method to set up instance attributes based on arguments passed during object creation."
                ],
                "challenge": [
                    "1. Define a class named `Student`.",
                    "2. Inside the `Student` class, define the `__init__` method.",
                    "3. The `__init__` method should accept two arguments (besides `self`): `name` and `student_id`.",
                    "4. Inside `__init__`, assign the passed `name` to an instance attribute also called `name`.",
                    "5. Inside `__init__`, assign the passed `student_id` to an instance attribute also called `student_id`.",
                    "6. After defining the class, create an instance of `Student` named `s1` with the name \"Alice\" and student ID 12345.",
                    "7. Print the `name` attribute of the `s1` object.",
                    "8. On the next line, print the `student_id` attribute of the `s1` object.",
                ],
                "expected_stdout": "Alice\n12345\n"
            },
            {
                "id": "l14_methods",
                "title": "Methods (Functions in Classes)",
                "type": "explanation",
                "text": [
                    "**Methods** are functions defined inside a class.",
                    "They define the behaviors or actions that objects of the class can perform.",
                    "Like `__init__`, instance methods always take `self` as their first parameter.",
                    "`self` allows the method to access and modify the object's own attributes.",
                    "You call methods on an object using dot notation: `object_name.method_name(arguments)`."
                ],
                "example": "class Dog:\n    def __init__(self, name):\n        self.name = name\n        self.tricks = [] # Start with an empty list of tricks\n\n    # An instance method to add a trick\n    def add_trick(self, trick):\n        self.tricks.append(trick)\n        print(f\"{self.name} learned {trick}!\")\n\n    # Another instance method\n    def bark(self):\n        print(f\"{self.name} says Woof!\")\n\ndog1 = Dog(\"Buddy\")\ndog2 = Dog(\"Lucy\")\n\n# Call methods on the objects\ndog1.bark()\ndog2.add_trick(\"Sit\")\ndog1.add_trick(\"Roll Over\")\ndog2.bark()\n\nprint(f\"{dog1.name}'s tricks: {dog1.tricks}\")\nprint(f\"{dog2.name}'s tricks: {dog2.tricks}\")"
            },
             {
                "id": "l14_self",
                "title": "Understanding 'self'",
                "type": "explanation",
                "text": [
                    "The `self` parameter is a reference to the **current instance** of the class.",
                    "It's used within methods to access the instance's attributes and other methods.",
                    "Python automatically passes the instance as the first argument when you call a method on an object (`object.method(args)` becomes `Class.method(object, args)` internally).",
                    "While `self` is the conventional name, you could technically name it something else (but it's strongly discouraged)."
                ],
                "example": "class Counter:\n    def __init__(self):\n        self.count = 0 # Instance attribute\n\n    def increment(self):\n        # Access and modify instance attribute using self\n        self.count += 1 \n        print(f\"Count is now: {self.count}\")\n\n    def get_count(self):\n        # Access instance attribute using self\n        return self.count\n\nc1 = Counter()\nc2 = Counter()\n\nc1.increment() # self refers to c1 inside increment\nc1.increment() # self refers to c1 inside increment\nc2.increment() # self refers to c2 inside increment\n\nprint(f\"c1 final count: {c1.get_count()}\") # self refers to c1\nprint(f\"c2 final count: {c2.get_count()}\") # self refers to c2"
            },
             {
                "id": "l14_method_challenge",
                "title": "Code: Class with a Method",
                "type": "code",
                "explanation": [
                    "Define a class with an `__init__` method and another method that uses the instance's attributes."
                ],
                "challenge": [
                    "1. Define a class named `Rectangle`.",
                    "2. Define the `__init__` method to accept `width` and `height` and store them as instance attributes.",
                    "3. Define a method named `calculate_area` that takes no arguments (besides `self`).",
                    "4. Inside `calculate_area`, calculate the area (`self.width * self.height`) and return it.",
                    "5. After defining the class, create an instance named `rect` with width 5 and height 10.",
                    "6. Call the `calculate_area` method on the `rect` object.",
                    "7. Print the value returned by `calculate_area`.",
                ],
                "expected_stdout": "50\n"
            },
            {
                "id": "l14_oop_basics_quiz",
                "title": "Quiz: Classes and Objects",
                "type": "quiz",
                "question": "What is the conventional name for the first parameter in an instance method, which refers to the object itself?",
                "options": [
                    "this",
                    "instance",
                    "object",
                    "self"
                ],
                "correct_answer": 3 # self is the convention
            },
            {
                "id": "l14_inheritance_intro",
                "title": "Inheritance: Creating Subclasses",
                "type": "explanation",
                "text": [
                    "**Inheritance** is a mechanism where a new class (the **child** or **subclass**) inherits attributes and methods from an existing class (the **parent** or **superclass** or **base class**).",
                    "This promotes code reuse and establishes an 'is-a' relationship (e.g., a `Dog` 'is-a' type of `Animal`).",
                    "To create a subclass, specify the parent class in parentheses after the subclass name: `class ChildClass(ParentClass):`",
                    "The subclass automatically gains access to the parent's attributes and methods (unless they are private, denoted by `__`).",
                    "Subclasses can also add their own unique attributes and methods."
                ],
                "example": "# Parent class\nclass Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        # Generic implementation, might be overridden\n        print(f\"{self.name} makes a sound.\")\n\n# Child class inheriting from Animal\nclass Dog(Animal):\n    # Dog inherits __init__ from Animal\n    \n    # Add a method specific to Dog\n    def fetch(self):\n        print(f\"{self.name} fetches the ball!\")\n\n# Create instances\nmy_animal = Animal(\"Generic Creature\")\nmy_dog = Dog(\"Rex\")\n\nmy_animal.speak() # Calls Animal's speak\n\nmy_dog.speak()  # Calls Animal's speak (inherited)\nmy_dog.fetch()  # Calls Dog's own method\n\nprint(f\"Rex's name (from inherited __init__): {my_dog.name}\")"
            },
            {
                "id": "l14_method_overriding",
                "title": "Method Overriding",
                "type": "explanation",
                "text": [
                    "A subclass can provide its own specific implementation of a method that is already defined in its parent class. This is called **method overriding**.",
                    "When you call the overridden method on a subclass object, the subclass's version of the method is executed instead of the parent's version.",
                    "This allows subclasses to customize or specialize behavior inherited from the parent."
                ],
                "example": "class Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        print(f\"{self.name} makes a generic sound.\")\n\n# Dog overrides the speak method\nclass Dog(Animal):\n    def speak(self): # Override the parent's speak method\n        print(f\"{self.name} says Woof!\")\n\n# Cat also overrides speak\nclass Cat(Animal):\n    def speak(self): # Override with a different implementation\n        print(f\"{self.name} says Meow!\")\n\nmy_dog = Dog(\"Buddy\")\nmy_cat = Cat(\"Whiskers\")\n\nmy_dog.speak() # Calls Dog's overridden speak method\nmy_cat.speak() # Calls Cat's overridden speak method"
            },
            {
                "id": "l14_super",
                "title": "Using super()",
                "type": "explanation",
                "text": [
                    "The `super()` function allows a subclass to call methods from its parent class.",
                    "It's commonly used within a subclass's `__init__` method to call the parent's `__init__` (ensuring parent initialization happens) before adding subclass-specific initialization.",
                    "It's also useful in overridden methods when you want to extend the parent's behavior rather than completely replacing it.",
                    "Syntax: `super().method_name(arguments)`"
                ],
               "example": '''"class Vehicle:\n    def __init__(self, make, model):\n        print(\"Vehicle __init__ called\")\n        self.make = make\n        self.model = model\n\n    def display_info(self):\n        print(f\"Make: {self.make}, Model: {self.model}\")\n\nclass Car(Vehicle):\n    def __init__(self, make, model, num_doors):\n        print(\"Car __init__ starting\")\n        # Call the parent's __init__ using super()\n        super().__init__(make, model)\n        # Add Car-specific initialization\n        self.num_doors = num_doors\n        print(\"Car __init__ finished\")\n\n    def display_info(self):\n        # Call parent's display_info first\n        super().display_info()\n        # Add Car-specific info\n        print(f\"Doors: {self.num_doors}\")\n\nmy_car = Car(\"Toyota\", \"Camry\", 4)\nprint(\"--- Calling display_info ---")\nmy_car.display_info()"'''
            },
            {
                "id": "l14_inheritance_challenge",
                "title": "Code: Simple Inheritance",
                "type": "code",
                "explanation": [
                    "Create a parent class and a child class that inherits from it.",
                    "The child class should utilize the parent's `__init__` via `super()` and add its own attribute."
                ],
                "challenge": [
                    "1. Define a parent class named `Person`.",
                    "2. Give `Person` an `__init__` method that accepts `name` and stores it as `self.name`.",
                    "3. Define a child class named `Employee` that inherits from `Person`.",
                    "4. Give `Employee` an `__init__` method that accepts `name` and `employee_id`.",
                    "5. Inside `Employee`'s `__init__`, use `super()` to call the `Person`'s `__init__` method, passing the `name`.",
                    "6. Also inside `Employee`'s `__init__`, store the `employee_id` as `self.employee_id`.",
                    "7. After defining the classes, create an instance of `Employee` named `emp1` with name \"Bob\" and ID 789.",
                    "8. Print the `name` attribute of `emp1`.",
                    "9. On the next line, print the `employee_id` attribute of `emp1`.",
                ],
                "expected_stdout": "Bob\n789\n"
            },
             {
                "id": "l14_inheritance_quiz",
                "title": "Quiz: Inheritance",
                "type": "quiz",
                "question": "If class `Dog` inherits from class `Animal`, and both have a method called `speak()`, which `speak()` method is called when you execute `my_dog.speak()` (where `my_dog` is an instance of `Dog`)?",
                "options": [
                    "The `Animal` class's `speak()` method.",
                    "The `Dog` class's `speak()` method.",
                    "Both methods are called automatically.",
                    "It results in an error."
                ],
                "correct_answer": 1 # Method overriding means the subclass's method is called
            }
            # Future OOP topics: Polymorphism, Encapsulation (private attributes), Properties, Class/Static Methods
        ]
    }
]