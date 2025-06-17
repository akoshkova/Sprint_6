def verify_search_results(search_term, results):
    for result in results:
        assert search_term.lower() in result.lower(), f"Search term '{search_term}' not found in result: {result}"