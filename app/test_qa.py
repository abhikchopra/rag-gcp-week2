from rag_pipeline import build_index
from qa import ask_question

print("Building RAG index...")

# STEP 1: build memory from PDF
store = build_index("data/sample.pdf")

print("Index built successfully!")

# STEP 2: interactive loop
while True:
    q = input("\nAsk a question (type 'exit' to quit): ")

    if q.lower() == "exit":
        break

    print("\nThinking...\n")

    answer = ask_question(store, q)

    print("\nANSWER:\n", answer)