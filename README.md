## Repeated intent example

This simple bot varies the responses for successive `out_of_scope` messages by using a custom action `action_count_repeated_intent` to set the slot `repeated_intent_counter`. That slot stores the count for the number of times the current intent has been repeated. Then conditional response variations is used to make the response selection to the user.

This uses global slot mappings feature of Rasa 3.x to set the slot `repeated_intent_counter` with a custom action after every turn. For more details, see [this blog post](https://rasa.com/blog/how-to-use-global-slot-mappings/)


## How to use this example?

1. Train a Rasa model containing the Rasa NLU and Rasa Core models by running:

    ```
    rasa train
    ```

    The model will be stored in the `/models` directory as a zipped file.

2. Test the assistant by running:

    ```
    rasa run actions
    rasa shell
    ```

    This will load the assistant in your command line for you to chat.

3. Try repeatedly entering either:

- "give me a human" (variations for first 3 entries)
- "what is the meaning of life" (enter 5 times to see results)

An example conversation:

```
Your input ->  what is the meaning of life                                                     
I do not know.
Your input ->  what is the meaning of life                                                     
I do not know.
Your input ->  what is the meaning of life                                                     
I do not know.
Your input ->  what is the meaning of life                                                     
I do not know.
Your input ->  what is the meaning of life                                                     
Since you persist, it is 42
```
