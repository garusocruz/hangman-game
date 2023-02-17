# Solving the board: Enhancing Sudoku Game Performance with chatGPT + Python
My friend had developed a Sudoku game using Angular, but was sad about the loading time of the game board. He approached me and asked, "Garuso, can you create an API service to calculate the board faster?

"Sure," I replied, "I've been dying to try ChatGPT's to convert a function code from one language to another, and this seems like the perfect opportunity. But could you help us with this? I mean, it's not like you can solve all the problems, right?"

I asked ChatGPT, "Can you convert this function in Angular to Python?"

To which it replied, "This is very similar to a Sudoku game. Here is an example of how to create a Sudoku game in Python."

The first solution suggested by the AI worked, but the generated board was invalid. I decided to ask again with a new request, "Can you add a validation to the code to ensure that all generated games are valid?".

However, even after adding the validation, the game board was still taking a long time to respond. I asked ChatGPT, "Is there any way to improve the code's performance?"

It was recommended that I use a backtracking validation approach, and I followed the code with these improvements. While this solution was effective, it returned the same Sudoku board game every time.

After several improvements, I discovered an error in the code: the solution was right, but each new game only differed in difficulty level, while the board solution remained the same. "It's like déjà vu all over again".

I decided to use NumPy, a package with focus on multidimensional array processing, to improve the code. "Well, let's bring in the big guns.This code is about to get a serious upgrade."

Finally, after the last improvement with ChatGPT, we were able to solve all the problems. My friend was happy with the API that AI helped create, and the game is now loading much faster.

So, let's play a Sudoku? 

Thanks [Cleiton Schönardie](https://www.linkedin.com/in/cleitonsch/) for the challenge and the nice UI.

Try the [UI](https://github.com/cleitonpax/sudoku-ng15) repository. 

