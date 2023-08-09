# Clarifying the Problem

Whiteboarding interviews begion with a problem from the interviewer. The interviewee must be confident they understand the dimensions of the problem!

Software development is full of ambiguity. Programming requires concrete deliverables, but company needs can be murky. Even when the need is clear, a feature could have dozens of possible implementations. The ability to clearly define a problem is an important skill to demonstrate.

When the interviewer presents their technical question, repeat the question back to the interview **in your own words**. This gives you a moment to think and will resolve any glaring misunderstandings.

Once you've repeared the question, **ask every clarifying question that comes to mind**.

Assumptions must be communicated to the interviewer so there is agreement on the scope of the problem.

For example, if asked:

> Write a function that returns duplicate characters in string.

Here are some questions which may come to mind:

- What is the desired return value?
  - `True|False`, a list of characters, or ...?
- Do punctutation and spaces count as "characters"?
- Should case be considered?
  - are `"a"` and `"A"` duplicates?
- Should we be checking for Unicode characters?
- Can we assume it's a 26 character alphabet?

---

We'll apply these steps to a single problem through the rest of the lesson.

```text
Given a list of numbers, return whether the list contains Pythagorean Triplets.
```

**Questions or assumptions:**

- The input list should only contain integers. Do we need to check for this?
  - Any floats can be squared and added to create a new squared float to satisfy Pythagoras' rule, but a Pythagorean Triple usually refers to integers values **a**, **b** and **c** for **a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>**.
- Return value should be `True|False` instead of outputting the actual Pythagorean Triple values.
