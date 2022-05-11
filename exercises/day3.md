### Dicts exercises
1. Given the following dictionary:
    ```python
    d = {
      'times': 100, 
      'name': 'George', 
      'hobbies': ['fishing', 'hiking'],
    }
    ```
    * add key `'friends'` to `d` with `['Andrei', 'Mihai', 'Alina']` as value
    * sort value for key `'friends'`
    * remove `'hiking'` from hobbies list
    * remove `'times'` key from `d`
   
2. Create a dictionary of dictionaries to store the following data 
(`{<id>: {"interface": <interface>, "ip": <ip>, ...}, ...}`):

| id | Interface | IP      | status |
|----|-----------|---------|--------|
| 1  | Ethernet0 | 1.1.1.1 | up     |
| 2  | Ethernet1 | 2.2.2.2 | down   |
| 3  | Serial0   | 3.3.3.3 | up     |
| 4  | Serial1   | 4.4.4.4 | up     |

   * Write a python program to find the status of a given id
   * Write a python program to find interface and IP of all interfaces which are up 
   * Write a python program to count how many ethernet interfaces there are
   * Write a python program to add a new entry to the dictionary (auto-increment the id)
   
3. Given a list of strings build a dictionary that has each unique string as a key and the 
number of appearances as a value.
    
     E.g. `['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']` ->
`{'hello': 2, 'is': 1, 'there': 2, 'anybody': 1, 'in': 1}`

### Functions exercises
1. Write a function that takes a number as a parameter and prints its square.
1. Write another function that takes a number as a parameter and returns the square. 
Are the results of the two functions different? 
1. Write a function that takes any number of strings and an integer `n` as parameters.
`n` should be an optional parameter. Return the list of strings longer than `n`. 
By default, it should return a list containing all words.

    E.g. 
    * `f('hello', 'hi', 'bye', n=2)` -> `['hello', 'bye']`
    * `f('hello', 'hi')` -> `['hello', 'hi']`
    * `f()` -> `[]`
    * `f(n=10)` -> `[]`
1. Write a function that builds html tags. Apply html escaping for html special chars. 
The function will receive 2 parameters – tag type and tag content and will return the generated html as a string. 
    
    E.g.: `f('b', 'Ham&Eggs')` returns `"<b>Ham&amp;Eggs</b>"`
    
    HTML char escaping:
    * `<` becomes `&lt`;
    * `>` becomes `&gt`;
    * `"` becomes `&quot`;
    * `&` becomes `&amp`;

### Modules and packages exercises
1. Create a Python package with a module in it where you place one of the functions defined above.
1. Create a Python module where you import and call the functions defined above 
(the one from the package and the remaining ones from `<functions_exercises_module>`).
