# Producing Inputs and Finding Edge Cases

When the question is clear, we then produce concrete inputs and outputs. These inputs guide a solution for the remainder of the interview so write them on the board!

You may still be unclear how to solve the problem in code, but it's certain that given an input, `X`, your function will produce an output, `Y`.

Make one input the _happy path_: input that reflects the common scenario.

For example, you're asked to write a function which capitalizes the first letter of an input string.

A good input could be `"apple"`, which returns `"Apple"` because this demonstrates the function's purpose.

If the input were `"Apple"`, it would return `"Apple"`. That's correct but less informative.

Also think about _edge cases_, or inputs which **do not** reflect a common scenario and may cause problems.

For the captalization function, what should you return if given `None` as input? Or a number?

---

**Inputs:**

- a list of integers
- empty list
- list of strings
- list of mixed inputs
- null values

Happy path:

- `[3, 4, 5]`
- `[1, 2, 3]`

Output:

- `True`
- `[0, 1, 2]`
- `[3, 4, 5]`

**Outputs:**

- `True|False`
- list indices corresponding to Pythagorean triple values
- tuple containing Pythagorean triplet values
