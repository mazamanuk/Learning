# Analyzing Time and Space Complexity

You're satisfied with your implementation and you've demonstrated how it works, but you're not quite done.

Analyze the time and space complexity of the solution. With this step you are demonstrating that you care about the efficiency of your code.

Explain your code's big O notation. If you can optimize to a more efficient runtime, explain how that would work. If you can't optimize, explain why it's not possible.

---

**Optimize:**

Proof of concept:

Our original solution loops once through for each element we're keeping track of, `i`, `j` and `k`. This means our original time complexity is O(n<sup>3</sup>), which isn't particularly efficient. Is there a way we can optimize our solution?

For an input of `[1, 2, 3, 4, 5]`, we can store the squared values in a new list: `[1, 4, 9, 16, 25]`.

For our loops, we can begin at the largest square, `25`, and loop backwards for our c<sup>2</sup> comparisons.

For each loop, we can set up pointers at the next largest square (`k`) and the smallest square (`j`) and add them to compare to our `i` variable (first loop).

1. 1 + 16 = 17, we haven't reached 25 yet and we're still below the value, so we can increment our lower pointer => j += 1
2. 4 + 16 = 20, we still haven't reached 25 and we're still below the value, so we can increment our lower pointer => j += 1
3. 9 + 16 = 25, we've reached 25, so we can return `True` or print the values associated with this Pythagorean triplet.

This solution loops once in reverse order through each element in the list, and for each element looped we set pointers to loop through the remaining elements, so this solution is now O(n<sup>2</sup>) time complexity.
