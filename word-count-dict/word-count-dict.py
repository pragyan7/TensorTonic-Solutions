def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    d = {}
    for sent in sentences:
        for s in sent:
            d[s] = d.get(s, 0) + 1
    return d