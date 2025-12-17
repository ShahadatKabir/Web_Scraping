import pandas as pd
import requests

data_list = []

def movie_scraper(category, platform):

    base_url = f'https://www.rottentomatoes.com/cnapi/browse/{category}/affiliates:{platform}'
    url = base_url
    has_next_page = True

    while has_next_page:
        response = requests.get(url)
        data = response.json()

        movies = data.get('grid', {}).get('list', [])

        for movie in movies:
            movies_dict = {
                'title': movie.get('title', ''),
                'critic_score': movie.get('criticsScore', {}).get('scorePercent'),
                'critic_sentiment': movie.get('criticsScore', {}).get('sentiment'),
                'audience_score': movie.get('audienceScore', {}).get('scorePercent'),
                'audience_sentiment': movie.get('audienceScore', {}).get('sentiment')
            }

            print(movies_dict)
            data_list.append(movies_dict)

        # Pagination
        next_page_token = data.get('pageInfo', {}).get('endCursor')

        if next_page_token:
            url = f'{base_url}?after={next_page_token}%3D'
        else:
            has_next_page = False

    # Save to CSV after all pages
    df = pd.DataFrame(data_list)
    df.to_csv(f'{category}-{platform}.csv', index=False)


movie_scraper('movies_at_home', 'netflix')
