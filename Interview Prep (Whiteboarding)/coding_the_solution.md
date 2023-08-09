# Coding the Solution

We've finally come to the portion where you'll write some code! Previous steps improve your odds for success because you have an outline and clear inputs for testing.

Writing code on the board is a collaborative process. Refer to your outline and explain the step you're implementing.

The goal is to be facing the interviewer when talking through the implementation and facing the board when you're writing code.

Try to avoid writing code in silence or narrating at a low level like "for... i... in... range... length of the list... colon" when writing `for i in range(len(input_list)):`.

When you're finished with the implementation, look it over for any mistaken syntax or logical errors.

---

**Code:**

```python
def pythagorean_triple(input_list):
    # add in a sort on the input list to ensure other valid inputs aren't incorrectly flagged as False
    input_list.sort()
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            for k in range(j+1, len(input_list)):
                if input_list[i]**2 + input_list[j]**2 == input_list[k]**2:
                    return True
    return False
```

Before writing each step on paper, **say what you will do out loud**. Better to practice by yourself than in a real interview.
