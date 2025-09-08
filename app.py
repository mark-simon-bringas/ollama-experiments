import ollama

model_name = 'ooga-booga:latest'

while True:
    question = input("Give words. Ooga-booga.\n>>> ")
    
    if question.strip().lower() in ['exit', 'quit']:
        print("Stop. Ooga-booga.")
        break

    # prompt to your heart's content 
    try:
        stream = ollama.chat(
            model=model_name,
            messages=[{'role': 'user', 'content': question}],
            stream = True
        )

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
        
        print("\n")

    except ollama.ResponseError as err:
        # if model has not been downloaded yet
        if err.status_code == 404:
            print(f"Model '{model_name}' not found. Pulling model...")
            ollama.pull(model_name)
            print(f"Model '{model_name}' pulled successfully. Please re-run the script.")
        else :
            print(f"Error occurred: {err.error}")