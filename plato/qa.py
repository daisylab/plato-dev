from transformers import pipeline

nlp = pipeline("question-answering")


def fr(question, context):

    answer = nlp(question=question, context=context)

    return answer
