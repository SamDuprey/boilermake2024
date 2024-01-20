import os
from openai import OpenAI
import asyncio
def generate_story(subreddit):
    client = OpenAI(
        # This is the default and can be omitted
        api_key='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',
    )

    user_message = f"Create a short example post that replicates the nature of stories in the subreddit r/{subreddit}. Make sure that the post is full of drama and the story is unique."

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content

def main():
    subreddit_name = "TIFU"
    result = generate_story(subreddit_name)
    print(result)

if __name__ == "__main__":
    main()
