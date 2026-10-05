# Python File Handling 1
 
Python File handling
https://drive.google.com/file/d/1sIv9rb6PizW9sfts9eVu0BkLYWLjysiT/view

**Rules**

- Always `close()` a file after you finish with it.
- Pick the right mode. `"w"` **erases** the file first. `"a"` **adds** to the end.
  `"r"` only reads.
- `filename` is given to you as a parameter — never type a file name inside
  your function.
- Every line you write must end with `"\n"`.


## Exercise 1

**Problem:**

`items` is a list of strings. Write them to the file, one per line, each one
numbered starting from 1. The function returns nothing.

If the file already exists, the old content must be **replaced**, not added to.

**Example:**

    Example Input:
        items    = ["Bread", "Milk", "Eggs"]
        filename = "shopping.txt"

    File Output (shopping.txt):
        1. Bread
        2. Milk
        3. Eggs

Note the format carefully: number, full stop, **one space**, then the item.

---

## Exercise 2

**Problem:**

Read the file and return a **list of the names** in it, in order.

- Remove the `"\n"` and any spaces at the start or end of each name.
- Skip any blank lines completely.

**Example:**

    Example File Content (names.txt):
        Bat

          Saraa
        Anu

    Program Output:
        ["Bat", "Saraa", "Anu"]

    Example File Content (empty file):

    Program Output:
        []

*Hint:* `readlines()` gives you a list of lines, but each one still has `"\n"`
stuck on the end. `.strip()` removes it.

---

## Exercise 3

**Problem:**

Add `text` to the **end** of the file as a new line, without deleting what is
already there. Then return how many lines the file has now.

If the file does not exist yet, it must be created.

**Example:**

    Example File Content (log.txt):
        Mon
        Tue

    Example Input:
        text = "Wed"

    File Content afterwards (log.txt):
        Mon
        Tue
        Wed

    Program Output:
        3

*Hint:* you need to open the file twice — once in `"a"` mode to add the line,
then again in `"r"` mode to count the lines.

---

## Exercise 4

**Problem:**

Return a list of the **line numbers** (starting at 1) of every line that
contains `word` anywhere inside it.

Capital letters must be ignored, so searching for `"python"` also finds
`"Python"`. Return an empty list if nothing matches.

**Example:**

    Example File Content (text.txt):
        I like Python
        Python is fun
        Goodbye world
        python again

    Example Input:
        word = "python"

    Program Output:
        [1, 2, 4]

    Example Input:
        word = "mongolia"

    Program Output:
        []

*Hint:* `"Python is fun".lower()` gives `"python is fun"`. You can check
whether one string is inside another with `if small in big:`.

---

## Exercise 5

**Problem:**

Read the file `source` and write a **new** file `destination` containing the
same lines, but with a line number and a colon in front of each one.
Return how many lines you wrote.

The `source` file must not be changed.

**Example:**

    Example File Content (in.txt):
        apple
        banana
        cherry

    File Output (out.txt):
        1: apple
        2: banana
        3: cherry

    Program Output:
        3

Note the format: number, colon, **one space**, then the line.

*Hint:* read everything from `source` and `close()` it **before** you open
`destination`. Two files, two `open()` calls, two `close()` calls.

---

## Exercise 6 (Optional)

**Problem:**

A notes program with a menu that keeps working after you close it,
because the notes are saved in `notes.txt`.

    1. Add a note       -> ask for text, add it to the end of notes.txt
    2. View all notes   -> print every note with a number in front
    3. Search notes     -> ask for a word, print the notes containing it
    4. Quit

The program keeps showing the menu until the user chooses 4.
If the user types anything else, say so and show the menu again.

**Example**

    --- My Notes ---
    1. Add a note
    2. View all notes
    3. Search notes
    4. Quit
    Choose 1-4: 1
    Write your note: Buy milk
    Note saved.

    --- My Notes ---
    ...
    Choose 1-4: 2
    Your notes:
    1. Buy milk
    2. Study Python

    --- My Notes ---
    ...
    Choose 1-4: 3
    Search for: python
    2. Study Python
    Found 1 note(s).

---

