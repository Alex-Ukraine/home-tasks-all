def swap_quotes(some_string: str) -> str:
    return some_string.translate({34: 39, 39: 34})