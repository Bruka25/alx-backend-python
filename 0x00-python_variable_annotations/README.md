The following python codes are for ALX 0x00-python_variable_annotations project for the alx-backend-python, inside it contains the following python codes:

* Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float
* Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string
* Write a type-annotated function floor which takes a float n as argument and returns the floor of the float
* Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float
* Define and annotate the following variables with the specified values:
```
               -> a, an integer with a value of 1
               -> pi, a float with a value of 3.14
               -> i_understand_annotations, a boolean with a value of True
               -> school, a string with a value of “Holberton”
```

* Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float
* Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float
* Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of  the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float

* Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float  by multiplier
* Annotate the below function’s parameters and return values with the appropriate types
```
   def element_length(lst):
       return [(i, len(i)) for i in lst]
```
* Augment the following code with the correct duck-typed annotations:
```
  # The types of the elements of the input are not know
  def safe_first_element(lst):
      if lst:
          return lst[0]
      else:
          return None
```

* Given the parameters and the return values, add type annotations to the function
```
  def safely_get_value(dct, key, default = None):
      if key in dct:
          return dct[key]
      else:
          return default
```

* Use mypy to validate the following piece of code and apply any necessary changes
```
  def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
      zoomed_in: Tuple = [
          item for item in lst
          for i in range(factor)
      ]
      return zoomed_in

  array = [12, 72, 91]

  zoom_2x = zoom_array(array)

  zoom_3x = zoom_array(array, 3.0)
```
