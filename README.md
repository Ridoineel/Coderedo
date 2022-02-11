# Coderedo
Python code reformater

> Coderedo is simple program to reformat your python code, after indention error for example 🤗️.

> ###### To use coderedo, make this

```bash
git clone https://github.com/RidoineEl/coderedo.git
cd coderedo
python3 coderedo.py -f test.py
```

#### Coderedo parameters:
* -f or --file: the path of python file
* -go or --get-old: set value on 1 to get the old version of the processed file. *(optional)*
* -t or --tab-size: your tab size, default is 4 *(optional)*

## Example scenario
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

## Futures
* Make recursive on a directory 🤔️
