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


******

Reseach Notes - Answer Evaluation AI

Googling “Python AI for answer evaluation” was not bearing much benefit. I had to think simpler—break down the problem to its bare bones and go from there.

In its most basic form, I need an AI to check the similarity between the user's input and the correct answer, then return a statement on whether the two are very similar or not. **Update after some research. The model will need to *understand* the semantics and do a proper comparison**

Then, I discovered Natural Language Processing (NLP) and fuzzy string matching.
I ruled out fuzzy string matching for two main reasons:
1) it seemed less flexible and not likely to fix the "close enough but phrased differently" problem
2) I'd prefer if the algorithm was actually capable of understanding the context of the problem and solution. Using the aforementioned Benedict's colour test, it would be ideal if the program could accept a wider scope varying yet correct answers, e.g. "brick-red" to describe the particular shade or "reddish orange". Little things like that, as well as users omitting/including non-important words, misspelling, etc. require a certain level of nuance that fuzzy string matching doesn't seem to provide.
   
Further research indicated that a simple NLP model won’t fully capture the nuance in some answers. For example, it might fail to recognize that “brick-red” or “reddish orange” fall within the same category as “Orange/red.” As humans, it is easy for us to infer this implicit information using common-sense reasoning; not so much for a basic NLP model.

I'll use a pre-trained model given how small and rather simple my dataset is (Not because my laptop is kinda bad so building and training my own would set it on fire :3)

**Side note: All AI experimentation will be on its own separate branch and merged later on**

spaCy was a common choice for similar problems. I'll go with it and keep track of some issues that may arise later on. Off the top of my head, here are some things that might go wrong:
1) short answers (1-2 words) might mess things up
2) words similar in theory might get a pass, e.g. "sugar" gets points when the answer is "deoxyribose"
3) very specific jargon might get mixed up (stuff like phosphodiester bonds or michaelis menten come to mind)

Regardless, I'll have to start somewhere.
