# Coderedo
Python code reformater

> Coderedo is a simple program to reformat your python code, after indention error for example 🤗️.

# Installation

```bash
pip install coderedo
python -m coderedo -p file.py
# or apply on a directory
python -m coderedo -p projects/
```

## Arguments:
* -p or --path: the path to a python file or python project directory
* -go or --get-old: set value on 1 to get the old version of the processed file. *(optional)*
* -t or --tab-size: your tab size, default value: 4

## Example with a file
Take this file: test.py in test directory <br>
test/test.py

```python
def func():
  print("Hello Wolrd !")
  print("Your are awesome")

func()
```
**Output after running this**

```python
File "test/test.py", line 4
  print("Your are awesome")
                           ^
TabError: inconsistent use of tabs and spaces in indentation
```

🤧️ There was a runtime error because, there are spaces for indentation on line 2 and tabulations on line 3.
> Note: In python, there only must be indentions or spaces per code sub bloc

### Fix this with coderedo
**fix**

```bash
python3 coderedo.py -f test/test.py
```

**Run this now**

```bash
python3 test/test.py
```

**Output**

```bash
Hello Wolrd !
Your are awesome
```

Ouff 🙂️...

## Example with a directory

You can apply coderedo on all the files of a directory recursively

Example

```bash
project/
  utils/
    functions.py
    variables.py
  main.py  
```

```bash
python -m coderedo -d project
```

is equal to

```bash
python -m coderedo -d project/main.py
python -m coderedo -d project/utils/functions.py
python -m coderedo -d project/utils/variables.py
```