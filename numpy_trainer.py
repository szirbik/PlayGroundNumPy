# This is a Python script for educational purposes .

# The purpose is to teach NumPy to beginners.
# Author: Nick Szirbik - September 2021.

import numpy as np

# the most important thing to remember is that albeit the syntax looks the same for using lists and numpy arrays
# these two (lists and arrays) are completely different things (i.e. data structures)
# a list is a dynamic, flexible, data structure specific for the core Python language
# an array in NumPy is Python wrapped data structure in C (more efficient/fast than the lists in Python)
# for mathematical operations, using lists, albeit possible, if very inefficient and slow
# by using NumPy arrays and the associated routines, we do not have to re-invent the
# already coded mathematical operations, but our programs will run much, much faster!!!

# if we have list in Python, for example
a_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
# we can transform into a NumPy (i.e. a C efficient array wrapped for Python use) array type (class) of object
a_numpy_array = np.asarray(a_list)
print(a_list)
print(a_numpy_array)
# observe the difference in how these two are printed

# we can also create directly NumPy arrays, in multiple ways...
# for example, defining a one dimensional array (or in mathspeak, a vector)

a_vector = np.array([-3, -2, -1, 0, 1, 2, 3])
# the vector can have any length, btw
print(a_vector)
# the whole vector is printed
print(a_vector[3])
# a single element of the vector is printed

# defining a two dimensional array (or in mathspeak, a matrix, three by three big here, but it can be of any size)

a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# printing an element, a line and then the whole matrix
print(a_matrix[1, 1])
print(a_matrix[1])
print(a_matrix)

# a matrix of the same size but with elements that are randomly generated by numpy
a_random_matrix = np.random.rand(3, 3)
print(a_random_matrix)
# observe that the default is to produce float/real elements in the (0.0, 1.0) interval

# what if we want a hyper-matrix (super multi dimensional)?
# four dimensions, for example, but we will have to write a lot by hand, and...
# it is easier to create its elements via another random generator, one for positive integer values
multi_dim_matrix = np.random.randint(100, size=(4, 12, 7, 8))
# the first argument, 100 here, determines the range of the numbers (0 to 99) in the matrix
# the second the size of the matrix on each dimension
# we can print it, but don't forget that it is huge! (2688 values == 8 * 7 * 12 *4 )
print(multi_dim_matrix)
# the number of dimensions can be found by inquiring the array's property ndim
print("this matrix has ", multi_dim_matrix.ndim, " dimensions")

# other types than integer are also possible (Float/real numbers, Boolean/true or false values, and Complex numbers)

# for example, a small two dimensional random boolean matrix would be created via
bool_matrix = np.random.choice([False, True], size=(5, 7))
print(bool_matrix)

# to create a random float/real values array, we should also think about the kind of distribution we want
# typically, we want a uniform distribution, and there is a routine in place for that
a_real_random_vector = np.random.uniform(low=0.0, high=5.0, size=10)
print(a_real_random_vector)

# a few more useful routines

# creating an empty array
an_empty_matrix = np.empty([9, 11])
# creates an "empty" two dimensional array with 9 rows and 11 columns
print(an_empty_matrix)
# however, these are not all necessarily zeroes

# creating arrays full of true zeroes
a_zero_filled_vector = np.zeros(12)
print(a_zero_filled_vector)

# or even with ones (float value 1.0)
a_one_filled_matrix = np.ones([2, 3])
print(a_one_filled_matrix)

# we can create various sequences of numbers as arrays by using the numpy.arange() (i.e. "a range") routine
simple_range = np.arange(144)
print(simple_range)
# this creates integers

# numpy.arange() is in fact a routine that can create more complicated mathematical sequences
float_type_range = np.arange(start=11.0, stop=108.5, step=2.5)
print(float_type_range)

# to the same effect we can use another routine, numpy.linspace()
same_range = np.linspace(11.0, 108.5, 40)
print(same_range)
# this is useful if we know the number of points in an interval, but not bothering with the linear interval/step
# between the points

# we can create sequences of points that are not linearly spaced, but logarithmically!
logarithmic_seq_range = np.logspace(start=1, stop=9, num=5)
print(logarithmic_seq_range)
# notice that the stop value 9 means here 10 at power of nine, that is one billion!

# in Python fashion, we can add and remove elements from a NumPy array
# adding to an array is done via the routine numpy.append(). For example:
head = np.array([1, 2, 3])
body = np.array([4, 5, 6])
tail = np.array([7, 8, 9])
linear_animal = np.append(head, [body, tail])
print(linear_animal)

# numpy.append has a third parameter, "axis", which can make the following difference:
matrix_animal = np.append([head, body], [tail], axis=0)
print(matrix_animal)
# see how the input parameters and the result differ from the previous one
# If the value for "axis" is not given, both input values are "flattened" before use.
# Otherwise, the input values have to be of the same "shape"/dimension

# removing an element is done via numpy.delete()
boring_matrix = np.array([[0, 1, 2, 1], [3, 4, 1, 5], [1, 6, 1, 7]])
less_boring_matrix = np.delete(boring_matrix, 1, axis=0)
print(less_boring_matrix)
# inspect the result and try to understand what exactly is removed
# try without the "axis" argument and see what happens...

# the shape (dimensions) of an array are an important characteristic of the Numpy objects of the "array" type
# if we do not know the shape of an array, we can find it out!
shape_boring = np.shape(boring_matrix)
shape_less_boring = np.shape(less_boring_matrix)
print("first shape is ", shape_boring, " (rows, columns)\nsecond shape is ", shape_less_boring, " (rows, columns)")
# notice that the routine returns a Python tuple, which for a n-dimensional array will be n-long

# we can reshape an array, without copying its elements into a new object
# the easiest is to flatten a multi dimensional array into a vector
boring_vector = boring_matrix.flatten()
print(boring_vector)

# and we can transform the result into a matrix of another shape
born_again_matrix = boring_vector.reshape(2, 6)
print(born_again_matrix)

# we can do these operations "in-situ" without creating new objects, as in the following lines of code
print(born_again_matrix.ravel())
# we can make it back to the initial shape, by changing its "shape property"
born_again_matrix.shape = (3, 4)
print(born_again_matrix)

# the full power of NumPy comes to fore when we want to do mathematical operations on vectors and matrices
# we can add, subtract, divide, raise to power, do modulo (reminder) between the identically placed
# elements of two arrays that have the same shape and if they are numerical

# adding
first_vector = np.asarray([-1.5, 0, 2, 5])
second_vector = np.asarray([-5, 3, 4, 2.5])
sum_vector = np.add(first_vector, second_vector)
print(sum_vector)

# subtracting
sub_vector = np.subtract(first_vector, second_vector)
print(sub_vector)

# multiplying
mult_vector = np.multiply(first_vector, second_vector)
print(mult_vector)

# dividing
div_vector = np.divide(first_vector, second_vector)
print(div_vector)

# raising to power
pw_vector = np.power(first_vector, second_vector)
print(pw_vector)

# modulo operation (reminder of division)
mod_vector = np.mod(first_vector, second_vector)
print(mod_vector)
rem_vector = np.remainder(first_vector, second_vector)
print(rem_vector)
# these two last routines are the same

# we can also make operations between an array a scalar value
added_ten = first_vector + 10
print("with 10 bigger ", added_ten)
divided_by_thirty = second_vector / 30
print("divided by 30 ", divided_by_thirty)

# we can also change the precision of the elements of an array (rounding in various ways)
print(np.around(first_vector))
print(np.ceil(second_vector))
print(np.floor(mult_vector))

# the trigonometric operations are also available, see a few below
print(np.sin(first_vector))
print(np.cos(first_vector))
print(np.tan(first_vector))
print(np.arcsin(divided_by_thirty))  # think why this is necessary
print(np.arccos(divided_by_thirty))
print(np.arctan(first_vector))

# however, the full power of the NumPy library is given by the routines used in statistics
# a few, the mostly used, below...
print(np.min(first_vector))
print(np.max(first_vector))
print(np.mean(first_vector))  # given the same result as numpy.average()
print(np.average(first_vector))  # but this one can calculate a weighted average if a weights parameter is supplied
print(np.std(first_vector))  # standard deviation
print(np.var(first_vector))  # variance, the spread of the distribution

# finally, algebraic operations between arrays are also implemented as routines
# for those students who are familiar with these, the basic ones are:

# dot (or scalar) product of two arrays
a = np.array([1, 2, 3])
b = np.array([4, -5, 6])
a_dot_b = np.dot(a, b)
print(a_dot_b)

# inner product of arrays - the first one is now a matrix 3x3 shaped
a_prod_b = np.inner([a, [7, 8, 9], [10, 11, 12]], b)
print(a_prod_b)

# determinant of an array
print(np.linalg.det([[[1, 2], [3, 4]], [[1, 2], [2, 1]], [[1, 3], [3, 1]]]))
# the above is a three dimensional array, therefore the result will be a one dimensional array
# most of the linear algebra operations are in the module (a part of the library/package) named "linalg"

# for the very curious student, NumPy can be used for a very specialized kind of mathematical operation,
# named the Discrete Fourier Transforms - However, this NumPy has only very basic code for this routines
# a more advanced library shall be used in this case, named SciPy

# to continue to study NumPy, the best is to use the https://numpy.org/doc/stable/index.html website
# here, you will have search functionality, a beginners guide, a quickstart chapter, the fundamentals chapter,
# tutorials, How To's, glossary, etc.
