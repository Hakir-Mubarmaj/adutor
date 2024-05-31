from googlesearch import search

def google_search(query, num_results=10):
    try:
        # Perform the Google search
        results = search(query, num_results=num_results)
        
        # Print the search results
        for i, result in enumerate(results, start=1):
            print(f"{i}. {result}")
    except Exception as e:
        print("An error occurred during the search:", str(e))

# Replace 'your_query_here' with the query you want to search for
query = "doraemon"
num_results = 10  # Number of results to retrieve

google_search(query, num_results)
