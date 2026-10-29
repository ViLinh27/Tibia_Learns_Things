# Introduction to ChoiceScript

- url to read more in detail:
  - https://www.choiceofgames.com/make-your-own-games/choicescript-intro/

## What is ChoiceScript?

- simple interactive novel programming language
- syntax looks really similar to ren'py except more text based product instead of visuals
- a finished ChoiceScript game can be submitted to choiceofgames.com

## Trying it out

- need Node.js installed
- download ChoiceScript from Github
  - zip file
  - I have a mac so :
    - double click on `serve.command`
    - Will need to go to System Settings and look for "Gatekeeper".
    - Look for a dialog that will get you to `Open Anyway`.
- Your browser will open to get an example game since the server is on now

## Your First Scene: *choice and *finish

- There's an example game found under web/mygame/startup.txt
- syntx very similar to ren'py
- `#` is for options
- a lot of choices to maek your own "choose your own adventure" story

## Go on , play with it!

- in mac the text editor default is TextEdit and in windows it's Notepad
- the server has to be running to see the effects of any changes on a refresh

## Indentation

- keep indentations consistent in each file
  - don't use spaces and tabs in one file
- similar to ren'py

## Reusing Code: Goto and Label

- The `*goto` command lets you go to another story slots if they're labeled properly
  - use `*label`
- Every nested (indented) block has to end with a `*finish` command which ends scene (the story slot) or a `*goto` which jumps to another scene

## Setting and Checking Variables (aka "stats")

- variables are how stats will work
- adds more interactivity than just the choices
- how to declare variable
  `*create leadership 50`
- how to define variable
  `*set leadership 30`
- `*create` only allowed at top of `startup.txt`
- can use `*set` anywhere (since this is how you change the variable)
- Ex:
  ```
  *choice
    #Leadership
      *set leadership +10
      *goto action
    #Strength
      *set strength +10
  ```
- Check value of variable like this (once set):

  ```
  #Run for class president
  *if leadership > 15
  You win election
  *finish
  You lose election
  *finish
  ```

  - condtional statements work in choice script too
    - if else statements

- variables can determine what choices are usable in later parts of a story (for example)
  - say you don't have enough mana (as a magician) at a point in your story
  - that means you won't cast certain spells (these are choices)

- variables can also been seen in a stats screen (there's a Show Stats button in the main game UI)
  - [More on customizing stats screen](https://www.choiceofgames.com/make-your-own-games/customizing-the-choicescript-stats-screen/)
- variables in choice script work like other languages: you can store anything basically
- There's also an `elseif`

## What happens when we \*finish?

- `*finish` goes to next scene in game
  - ```*scene_list
         startup
         animal
         variiables
         ending
         death
    ```
  - new scene needs a new txt file in the mygame folder

- ending of the game
  - ex:
    ```
    This is the last scene! GAME OVER!
    *ending
    ```
- The `*ending` will give the player an automatic "Play Again" dialogue

- You don't need to use the scene list
- You can use `*goto_scene` if you're not using the scene list to jump around scenes
  - helps for deaths so you don't have 1000 death files
  - can also use it for going to SPECIFIC labels

- Choice Script uses UTF-8 encoding
  - if you use different encoding, Choice script could break accented letters.
