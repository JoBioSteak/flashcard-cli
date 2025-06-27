DEVLOG of flashcard-cli

27/06/2025

What's been done so far?

CSV file loaded into objects
Card order is randomized
Quiz loop keeps track of scoring and skipped cards, with the option of quitting
Option to only attempt skipped cards was implemented

Common Issue

When user enters an answer **very similar** to the correct one, it is still considered incorrect.
E.g. What color does Benedict's test turn for reducing sugars?
>red or orange
Wrong answer! Try again......
The answer was Orange/red

This is prevalent throughout the program I believe that the implementation of AI would be benficial.
It would allow for:
1) Adaptive learning where question difficulty is based on user_score rather than being randomly generated
2) Smarter evaluation of answers rather than focusing on exact matches
3) The whole experience to feel more interactive and fun
4) Me to become more adept at using AI and have fun

Next steps:
Research AI and the different algorithms to find the ones best suited to me and my goals 

I'll start with one geared towards smarter answer evaluation as this is the most pressing issue.

