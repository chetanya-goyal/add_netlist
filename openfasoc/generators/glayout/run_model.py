import argparse

from glayout.llm.train_and_run import GlayoutLLMSessionHandler
from glayout.llm.train_and_run import run_llm_normal

import torch

def verify_model_type(value: str):
    models = ["3b", "7b", "22b"]
    if value.strip().lower() not in models:
        raise argparse.ArgumentTypeError(f"Model must be one of {models}")
    return value.strip().lower()

def get_huggingface_token_and_model() -> tuple:
    """Parse the command-line arguments to retrieve the Hugging Face access token.
    This function uses argparse to handle command-line arguments and specifically looks for an 
    access token required to download models and tokenizers from Hugging Face. If the token is 
    not provided, it raises an EnvironmentError with instructions on how to obtain one.
    Returns:
        str: The Hugging Face access token.
        str: the name of the model of choice either []
    Raises:
        EnvironmentError: If the access token is not provided in the command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Manage, interact, and run the Glayout LLM")
    parser.add_argument(
        "-m", "--model",
        type=str,
        choices=["3b", "7b", "22b"],
        required=False,
        default="7b",
        help="Specify the model to use (3b, 7b, 22b), case insensitive"
    )
    parser.add_argument(
        "-t",
        "--token",
        type=str,
        help="Specify the access token you are using to download the model and tokenizer from huggingface",
    )
    args = parser.parse_args()
    if args.token is None:
        errstring = "To download models from huggingface you need a hugging face account and an access token"
        errstring += "\nYou can create a hugging face account here: https://huggingface.co/join\n"
        errstring += "Once you have an account and sign in, you can create an access token (need read access) here:\n"
        errstring += "https://huggingface.co/settings/tokens\n"
        errstring += "pass the access token in the command line with the option --token=[insert token here]"
        raise EnvironmentError(errstring)
    return args.token, args.model
#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
#accesstoken = get_huggingface_token()


def main():
    accesstoken, model = get_huggingface_token_and_model()
    session = GlayoutLLMSessionHandler(accesstoken=accesstoken, model=model)
    try:
        while True:
            # Read user input
            print("\nEnter clear to reset chat history, and exit to end this session.")
            user_input = input("Enter your input: ")
            if user_input=="exit":
                print("\nSession ended by user.")
                break
            elif user_input=="clear":
                print("\nClearing chat history (your next prompt should be a description of a circuit to create)\n")
                session.clear_history()
            else:
                # Pass the user input to the session handler and get the response
                response = session(user_input=user_input)
                print(response)
    except KeyboardInterrupt:
        # Gracefully exit the loop on Ctrl+C
        print("\nSession ended by user.")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")

if __name__=="__main__":
    main()