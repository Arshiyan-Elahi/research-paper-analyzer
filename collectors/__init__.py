"""
Film Industry Data Collection System (Mock Version)
---------------------------------------------------
This backend simulates data collection using mock data instead of API calls
"""

import pandas as pd
from datetime import datetime
import random

class FilmDataCollector:
    def __init__(self, api_keys=None):
        """Initialize collector (no API keys needed for mock version)"""
        pass
        
    def get_company_films(self, company_name, limit=100):
        """
        Get films from a specific production company using mock data
        """
        # Mock data for different companies
        mock_films = {
            'A24': [
                {
                    'id': 1,
                    'title': 'Everything Everywhere All at Once',
                    'release_date': '2022-03-25',
                    'budget': 25000000,
                    'revenue': 103000000,
                    'runtime': 139,
                    'genre': 'Sci-Fi/Comedy/Action',
                    'director': 'Daniel Kwan, Daniel Scheinert',
                    'top_cast': 'Michelle Yeoh, Stephanie Hsu, Ke Huy Quan',
                    'vote_average': 7.9,
                    'vote_count': 3800,
                    'production_companies': 'A24',
                    'overview': 'A middle-aged Chinese immigrant is swept up in an insane adventure where she alone can save existence by exploring other universes and connecting with the lives she could have led.',
                    'rt_critic_score': 95,
                    'rt_audience_score': 89,
                    'metacritic_score': 81,
                    'oscar_nominations': 11,
                    'oscar_wins': 7
                },
                {
                    'id': 2,
                    'title': 'Midsommar',
                    'release_date': '2019-07-03',
                    'budget': 9000000,
                    'revenue': 48000000,
                    'runtime': 148,
                    'genre': 'Horror/Drama',
                    'director': 'Ari Aster',
                    'top_cast': 'Florence Pugh, Jack Reynor, William Jackson Harper',
                    'vote_average': 7.1,
                    'vote_count': 4200,
                    'production_companies': 'A24',
                    'overview': 'A couple travels to Northern Europe to visit a rural hometown\'s fabled Swedish mid-summer festival. What begins as an idyllic retreat quickly devolves into an increasingly violent and bizarre competition at the hands of a pagan cult.',
                    'rt_critic_score': 83,
                    'rt_audience_score': 63,
                    'metacritic_score': 72,
                    'oscar_nominations': 0,
                    'oscar_wins': 0
                },
                {
                    'id': 3,
                    'title': 'Uncut Gems',
                    'release_date': '2019-12-25',
                    'budget': 19000000,
                    'revenue': 50000000,
                    'runtime': 135,
                    'genre': 'Thriller/Crime/Drama',
                    'director': 'Josh Safdie, Benny Safdie',
                    'top_cast': 'Adam Sandler, Julia Fox, Kevin Garnett',
                    'vote_average': 7.4,
                    'vote_count': 3900,
                    'production_companies': 'A24',
                    'overview': 'A charismatic jeweler makes a high-stakes bet that could lead to the windfall of a lifetime. In a precarious high-wire act, he must balance business, family, and adversaries on all sides in pursuit of the ultimate win.',
                    'rt_critic_score': 91,
                    'rt_audience_score': 92,
                    'metacritic_score': 90,
                    'oscar_nominations': 1,
                    'oscar_wins': 0
                },
                {
                    'id': 4,
                    'title': 'Moonlight',
                    'release_date': '2016-10-21',
                    'budget': 4000000,
                    'revenue': 65000000,
                    'runtime': 111,
                    'genre': 'Drama',
                    'director': 'Barry Jenkins',
                    'top_cast': 'Mahershala Ali, Naomie Harris, Trevante Rhodes',
                    'vote_average': 7.9,
                    'vote_count': 4500,
                    'production_companies': 'A24',
                    'overview': 'A young African-American man grapples with his identity and sexuality while experiencing the everyday struggles of childhood, adolescence, and burgeoning adulthood.',
                    'rt_critic_score': 98,
                    'rt_audience_score': 91,
                    'metacritic_score': 99,
                    'oscar_nominations': 8,
                    'oscar_wins': 3
                },
                {
                    'id': 5,
                    'title': 'Lady Bird',
                    'release_date': '2017-11-03',
                    'budget': 10000000,
                    'revenue': 79000000,
                    'runtime': 94,
                    'genre': 'Drama/Comedy',
                    'director': 'Greta Gerwig',
                    'top_cast': 'Saoirse Ronan, Laurie Metcalf, Tracy Letts',
                    'vote_average': 7.4,
                    'vote_count': 3700,
                    'production_companies': 'A24',
                    'overview': 'In 2002, an artistically inclined seventeen-year-old girl comes of age in Sacramento, California.',
                    'rt_critic_score': 99,
                    'rt_audience_score': 79,
                    'metacritic_score': 94,
                    'oscar_nominations': 5,
                    'oscar_wins': 0
                },
                {
                    'id': 6,
                    'title': 'The Lighthouse',
                    'release_date': '2019-10-18',
                    'budget': 11000000,
                    'revenue': 18000000,
                    'runtime': 109,
                    'genre': 'Horror/Drama',
                    'director': 'Robert Eggers',
                    'top_cast': 'Robert Pattinson, Willem Dafoe',
                    'vote_average': 7.5,
                    'vote_count': 3100,
                    'production_companies': 'A24',
                    'overview': 'Two lighthouse keepers try to maintain their sanity while living on a remote and mysterious New England island in the 1890s.',
                    'rt_critic_score': 90,
                    'rt_audience_score': 72,
                    'metacritic_score': 83,
                    'oscar_nominations': 1,
                    'oscar_wins': 0
                },
                {
                    'id': 7,
                    'title': 'Ex Machina',
                    'release_date': '2015-04-24',
                    'budget': 15000000,
                    'revenue': 36000000,
                    'runtime': 108,
                    'genre': 'Sci-Fi/Thriller',
                    'director': 'Alex Garland',
                    'top_cast': 'Alicia Vikander, Domhnall Gleeson, Oscar Isaac',
                    'vote_average': 7.7,
                    'vote_count': 8800,
                    'production_companies': 'A24',
                    'overview': 'A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a highly advanced humanoid A.I.',
                    'rt_critic_score': 92,
                    'rt_audience_score': 86,
                    'metacritic_score': 78,
                    'oscar_nominations': 2,
                    'oscar_wins': 1
                },
                {
                    'id': 8,
                    'title': 'The Witch',
                    'release_date': '2016-02-19',
                    'budget': 4000000,
                    'revenue': 40000000,
                    'runtime': 92,
                    'genre': 'Horror/Mystery',
                    'director': 'Robert Eggers',
                    'top_cast': 'Anya Taylor-Joy, Ralph Ineson, Kate Dickie',
                    'vote_average': 6.8,
                    'vote_count': 4700,
                    'production_companies': 'A24',
                    'overview': 'A family in 1630s New England is torn apart by the forces of witchcraft, black magic, and possession.',
                    'rt_critic_score': 90,
                    'rt_audience_score': 71,
                    'metacritic_score': 83,
                    'oscar_nominations': 0,
                    'oscar_wins': 0
                }
            ],
            'Neon': [
                {
                    'id': 101,
                    'title': 'Parasite',
                    'release_date': '2019-10-11',
                    'budget': 11400000,
                    'revenue': 258000000,
                    'runtime': 132,
                    'genre': 'Thriller/Drama/Comedy',
                    'director': 'Bong Joon-ho',
                    'top_cast': 'Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong',
                    'vote_average': 8.5,
                    'vote_count': 12000,
                    'production_companies': 'Neon',
                    'overview': 'Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.',
                    'rt_critic_score': 99,
                    'rt_audience_score': 90,
                    'metacritic_score': 96,
                    'oscar_nominations': 6,
                    'oscar_wins': 4
                },
                {
                    'id': 102,
                    'title': 'Portrait of a Lady on Fire',
                    'release_date': '2020-02-14',
                    'budget': 5500000,
                    'revenue': 23000000,
                    'runtime': 122,
                    'genre': 'Drama/Romance',
                    'director': 'Céline Sciamma',
                    'top_cast': 'Noémie Merlant, Adèle Haenel, Luàna Bajrami',
                    'vote_average': 8.1,
                    'vote_count': 3500,
                    'production_companies': 'Neon',
                    'overview': 'On an isolated island in Brittany at the end of the eighteenth century, a female painter is obliged to paint a wedding portrait of a young woman.',
                    'rt_critic_score': 98,
                    'rt_audience_score': 92,
                    'metacritic_score': 95,
                    'oscar_nominations': 0,
                    'oscar_wins': 0
                }
            ],
            'Netflix Studios': [
                {
                    'id': 201,
                    'title': 'Roma',
                    'release_date': '2018-11-21',
                    'budget': 15000000,
                    'revenue': 5000000,
                    'runtime': 135,
                    'genre': 'Drama',
                    'director': 'Alfonso Cuarón',
                    'top_cast': 'Yalitza Aparicio, Marina de Tavira',
                    'vote_average': 7.7,
                    'vote_count': 5700,
                    'production_companies': 'Netflix Studios',
                    'overview': 'A year in the life of a middle-class family\'s maid in Mexico City in the early 1970s.',
                    'rt_critic_score': 96,
                    'rt_audience_score': 72,
                    'metacritic_score': 91,
                    'oscar_nominations': 10,
                    'oscar_wins': 3
                },
                {
                    'id': 202,
                    'title': 'The Irishman',
                    'release_date': '2019-11-01',
                    'budget': 159000000,
                    'revenue': 8000000,
                    'runtime': 209,
                    'genre': 'Crime/Drama/Biography',
                    'director': 'Martin Scorsese',
                    'top_cast': 'Robert De Niro, Al Pacino, Joe Pesci',
                    'vote_average': 7.8,
                    'vote_count': 6100,
                    'production_companies': 'Netflix Studios',
                    'overview': 'An old man recalls his time painting houses for his friend, Jimmy Hoffa, through the 1950-70s.',
                    'rt_critic_score': 95,
                    'rt_audience_score': 86,
                    'metacritic_score': 94,
                    'oscar_nominations': 10,
                    'oscar_wins': 0
                }
            ]
        }
        
        # Return data for requested company, or empty DataFrame if not found
        if company_name in mock_films:
            return pd.DataFrame(mock_films[company_name][:limit])
        else:
            # Return a generic dataset if company not in our mock data
            generic_data = []
            for i in range(1, min(6, limit+1)):
                generic_data.append({
                    'id': i,
                    'title': f'Film {i} ({company_name})',
                    'release_date': f'202{i}-01-01',
                    'budget': random.randint(5, 30) * 1000000,
                    'revenue': random.randint(10, 100) * 1000000,
                    'runtime': random.randint(90, 150),
                    'genre': random.choice(['Drama', 'Comedy', 'Action', 'Horror', 'Sci-Fi']),
                    'director': f'Director {i}',
                    'top_cast': f'Actor A, Actor B, Actor C',
                    'vote_average': round(random.uniform(5.5, 8.5), 1),
                    'vote_count': random.randint(1000, 10000),
                    'production_companies': company_name,
                    'overview': f'This is a mock description for film {i} from {company_name}.',
                    'rt_critic_score': random.randint(60, 95),
                    'rt_audience_score': random.randint(50, 90),
                    'metacritic_score': random.randint(60, 90),
                    'oscar_nominations': random.randint(0, 5),
                    'oscar_wins': random.randint(0, 2)
                })
            return pd.DataFrame(generic_data)
    
    def get_film_details(self, film_id):
        """This function is not needed in mock version as data is pre-populated"""
        pass
    
    def get_country_films(self, country_code, limit=100):
        """Get films from a specific country using mock data"""
        # Mock data for different countries
        country_films = {
            'za': [  # South Africa
                {
                    'id': 301,
                    'title': 'District 9',
                    'release_date': '2009-08-14',
                    'budget': 30000000,
                    'revenue': 210900000,
                    'runtime': 112,
                    'genre': 'Sci-Fi/Action',
                    'director': 'Neill Blomkamp',
                    'top_cast': 'Sharlto Copley, Jason Cope, Nathalie Boltt',
                    'vote_average': 7.9,
                    'vote_count': 7900,
                    'production_companies': 'TriStar Pictures',
                    'overview': 'An extraterrestrial race forced to live in slum-like conditions on Earth suddenly finds a kindred spirit in a government agent who is exposed to their biotechnology.',
                    'rt_critic_score': 90,
                    'rt_audience_score': 82,
                    'metacritic_score': 81,
                    'oscar_nominations': 4,
                    'oscar_wins': 0
                },
                {
                    'id': 302,
                    'title': 'Tsotsi',
                    'release_date': '2006-02-24',
                    'budget': 3000000,
                    'revenue': 9000000,
                    'runtime': 94,
                    'genre': 'Crime/Drama',
                    'director': 'Gavin Hood',
                    'top_cast': 'Presley Chweneyagae, Mothusi Magano',
                    'vote_average': 7.3,
                    'vote_count': 1200,
                    'production_companies': 'Miramax Films',
                    'overview': 'Six days in the violent life of a young Johannesburg gang leader.',
                    'rt_critic_score': 82,
                    'rt_audience_score': 87,
                    'metacritic_score': 70,
                    'oscar_nominations': 1,
                    'oscar_wins': 1
                },
                {
                    'id': 303,
                    'title': 'Seriously Single',
                    'release_date': '2020-07-31',
                    'budget': 3000000,
                    'revenue': None,
                    'runtime': 107,
                    'genre': 'Comedy/Romance',
                    'director': 'Katleho Ramaphakela, Rethabile Ramaphakela',
                    'top_cast': 'Fulu Mugovhani, Tumi Morake',
                    'vote_average': 5.2,
                    'vote_count': 450,
                    'production_companies': 'Netflix',
                    'overview': 'While her free-living bestie urges her to embrace singlehood, a commitment-craving social media expert can\'t stop following the life of a former love.',
                    'rt_critic_score': 60,
                    'rt_audience_score': 45,
                    'metacritic_score': None,
                    'oscar_nominations': 0,
                    'oscar_wins': 0
                }
            ],
            'kr': [  # South Korea
                {
                    'id': 401,
                    'title': 'Parasite',
                    'release_date': '2019-10-11',
                    'budget': 11400000,
                    'revenue': 258000000,
                    'runtime': 132,
                    'genre': 'Thriller/Drama/Comedy',
                    'director': 'Bong Joon-ho',
                    'top_cast': 'Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong',
                    'vote_average': 8.5,
                    'vote_count': 12000,
                    'production_companies': 'Neon',
                    'overview': 'Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.',
                    'rt_critic_score': 99,
                    'rt_audience_score': 90,
                    'metacritic_score': 96,
                    'oscar_nominations': 6,
                    'oscar_wins': 4
                },
                {
                    'id': 402,
                    'title': 'Oldboy',
                    'release_date': '2003-11-21',
                    'budget': 3000000,
                    'revenue': 15000000,
                    'runtime': 120,
                    'genre': 'Action/Drama/Mystery',
                    'director': 'Park Chan-wook',
                    'top_cast': 'Choi Min-sik, Yoo Ji-tae, Kang Hye-jung',
                    'vote_average': 8.4,
                    'vote_count': 5000,
                    'production_companies': 'Show East',
                    'overview': 'After being kidnapped and imprisoned for fifteen years, Oh Dae-Su is released, only to find that he must find his captor in five days.',
                    'rt_critic_score': 82,
                    'rt_audience_score': 94,
                    'metacritic_score': 77,
                    'oscar_nominations': 0,
                    'oscar_wins': 0
                }
            ]
        }
        
        # Return data for requested country, or empty DataFrame if not found
        if country_code.lower() in country_films:
            return pd.DataFrame(country_films[country_code.lower()][:limit])
        else:
            # Return a generic dataset if country not in our mock data
            generic_data = []
            for i in range(1, min(5, limit+1)):
                generic_data.append({
                    'id': i + 500,
                    'title': f'Film {i} ({country_code})',
                    'release_date': f'202{i}-01-01',
                    'budget': random.randint(3, 20) * 1000000,
                    'revenue': random.randint(5, 50) * 1000000,
                    'runtime': random.randint(90, 150),
                    'genre': random.choice(['Drama', 'Comedy', 'Action', 'Documentary']),
                    'director': f'Director from {country_code} {i}',
                    'top_cast': f'Local Actor A, Local Actor B',
                    'vote_average': round(random.uniform(5.5, 8.0), 1),
                    'vote_count': random.randint(500, 3000),
                    'production_companies': f'Studio {country_code}',
                    'overview': f'This is a mock description for film {i} from {country_code}.',
                    'rt_critic_score': random.randint(60, 90),
                    'rt_audience_score': random.randint(50, 85),
                    'metacritic_score': random.randint(55, 85),
                    'oscar_nominations': random.randint(0, 2),
                    'oscar_wins': random.randint(0, 1)
                })
            return pd.DataFrame(generic_data)
    
    def get_netflix_films(self, country=None, limit=100):
        """
        Get films available on Netflix, optionally filtered by country
        """
        # Mock Netflix films
        netflix_films = [
            {
                'title': 'The Harder They Fall',
                'release_date': '2021-10-22',
                'genre': 'Western/Action',
                'director': 'Jeymes Samuel',
                'country': 'United States',
                'netflix_release': '2021-11-03',
                'runtime': 139,
                'budget': 90000000,
                'revenue': None,
                'imdb_rating': 6.6,
                'rt_critic_score': 88,
                'rt_audience_score': 93,
                'metacritic_score': 68
            },
            {
                'title': 'Seriously Single',
                'release_date': '2020-07-31',
                'genre': 'Comedy/Romance',
                'director': 'Katleho Ramaphakela, Rethabile Ramaphakela',
                'country': 'South Africa',
                'netflix_release': '2020-07-31',
                'runtime': 107,
                'budget': 3000000,
                'revenue': None,
                'imdb_rating': 5.2,
                'rt_critic_score': 60,
                'rt_audience_score': 45,
                'metacritic_score': None
            },
            {
                'title': 'Queen Sono',
                'release_date': '2020-02-28',
                'genre': 'Action/Drama',
                'director': 'Kagiso Lediga',
                'country': 'South Africa',
                'netflix_release': '2020-02-28',
                'runtime': 45,
                'budget': 5000000,
                'revenue': None,
                'imdb_rating': 6.1,
                'rt_critic_score': 80,
                'rt_audience_score': 65,
                'metacritic_score': None
            },
            {
                'title': 'Blood & Water',
                'release_date': '2020-05-20',
                'genre': 'Drama/Mystery',
                'director': 'Nosipho Dumisa',
                'country': 'South Africa',
                'netflix_release': '2020-05-20',
                'runtime': 45,
                'budget': 4000000,
                'revenue': None,
                'imdb_rating': 6.7,
                'rt_critic_score': 80,
                'rt_audience_score': 70,
                'metacritic_score': None
            },
            {
                'title': 'Roma',
                'release_date': '2018-11-21',
                'genre': 'Drama',
                'director': 'Alfonso Cuarón',
                'country': 'Mexico',
                'netflix_release': '2018-12-14',
                'runtime': 135,
                'budget': 15000000,
                'revenue': 5000000,
                'imdb_rating': 7.7,
                'rt_critic_score': 96,
                'rt_audience_score': 72,
                'metacritic_score': 91
            }
        ]
        
        # Filter by country if specified
        if country:
            filtered_films = [film for film in netflix_films if film['country'] == country]
        else:
            filtered_films = netflix_films
            
        return pd.DataFrame(filtered_films[:limit])
    
    def get_box_office_data(self, film_title, year=None):
        """
        Get box office data for a film
        """
        # Normalize film title for searching
        search_title = film_title.lower().replace(' ', '_')
        
        # Mock box office data
        mock_box_office = {
            'everything_everywhere_all_at_once': {
                'budget': 25000000,
                'domestic_gross': 70000000,
                'international_gross': 33000000,
                'worldwide_gross': 103000000,
                'opening_weekend': 501305,
                'widest_release': 2220,
                'release_date': '2022-03-25'
            },
            'moonlight': {
                'budget': 4000000,
                'domestic_gross': 27000000,
                'international_gross': 38000000,
                'worldwide_gross': 65000000,
                'opening_weekend': 402075,
                'widest_release': 1564,
                'release_date': '2016-10-21'
            },
            'midsommar': {
                'budget': 9000000,
                'domestic_gross': 27400000,
                'international_gross': 20600000,
                'worldwide_gross': 48000000,
                'opening_weekend': 6600000,
                'widest_release': 2707,
                'release_date': '2019-07-03'
            },
            'parasite': {
                'budget': 11400000,
                'domestic_gross': 53300000,
                'international_gross': 204700000,
                'worldwide_gross': 258000000,
                'opening_weekend': 384216,
                'widest_release': 2001,
                'release_date': '2019-10-11'
            }
        }
        
        # Return data if found, otherwise empty dict
        for key, data in mock_box_office.items():
            if search_title in key:
                return data
        
        # If not found, return generic mock data
        return {
            'budget': random.randint(5, 40) * 1000000,
            'domestic_gross': random.randint(10, 80) * 1000000,
            'international_gross': random.randint(10, 100) * 1000000,
            'worldwide_gross': random.randint(30, 200) * 1000000,
            'opening_weekend': random.randint(1, 20) * 1000000,
            'widest_release': random.randint(800, 3000),
            'release_date': '2021-01-01'
        }
    
    def get_critical_reception(self, film_title, year=None):
        """
        Get critical reception data (Rotten Tomatoes, Metacritic)
        """
        # Normalize film title for searching
        search_title = film_title.lower().replace(' ', '_')
        
        # Mock data
        mock_reviews = {
            'everything_everywhere_all_at_once': {
                'rt_critic_score': 95,
                'rt_audience_score': 89,
                'rt_critic_count': 367,
                'rt_audience_count': 10000,
                'metacritic_score': 81,
                'metacritic_user_score': 8.3,
                'metacritic_review_count': 54,
                'top_critic_quote': "Mind-bending multiverse adventure that's both heartfelt and hilarious."
            },
            'moonlight': {
                'rt_critic_score': 98,
                'rt_audience_score': 91,
                'rt_critic_count': 389,
                'rt_audience_count': 25000,
                'metacritic_score': 99,
                'metacritic_user_score': 8.2,
                'metacritic_review_count': 51,
                'top_critic_quote': "Breathtaking in its visual poetry, lyrical in its narrative."
            },
            'midsommar': {
                'rt_critic_score': 83,
                'rt_audience_score': 63,
                'rt_critic_count': 380,
                'rt_audience_count': 17500,
                'metacritic_score': 72,
                'metacritic_user_score': 7.5,
                'metacritic_review_count': 54,
                'top_critic_quote': "Disturbing folk horror that's as beautiful as it is unsettling."
            },
            'parasite': {
                'rt_critic_score': 99,
                'rt_audience_score': 90,
                'rt_critic_count': 450,
                'rt_audience_count': 22000,
                'metacritic_score': 96,
                'metacritic_user_score': 8.9,
                'metacritic_review_count': 52,
                'top_critic_quote': "A genre-defying masterpiece that's both wildly entertaining and deeply insightful."
            }
        }
        
        # Return data if found, otherwise empty dict
        for key, data in mock_reviews.items():
            if search_title in key:
                return data
        
        # If not found, return generic mock data
        return {
            'rt_critic_score': random.randint(60, 95),
            'rt_audience_score': random.randint(50, 90),
            'rt_critic_count': random.randint(100, 400),
            'rt_audience_count': random.randint(1000, 20000),
            'metacritic_score': random.randint(60, 90),
            'metacritic_user_score': round(random.uniform(6.0, 8.5), 1),
            'metacritic_review_count': random.randint(30, 60),
            'top_critic_quote': "A notable entry in the filmmaker's body of work."
        }
    
    def get_awards_data(self, film_title, year=None):
        """
        Get awards data for a film
        """
        # Normalize film title for searching
        search_title = film_title.lower().replace(' ', '_')
        
        # Mock data
        mock_awards = {
            'everything_everywhere_all_at_once': {
                'oscar_nominations': 11,
                'oscar_wins': 7,
                'golden_globe_nominations': 6,
                'golden_globe_wins': 2,
                'bafta_nominations': 10,
                'bafta_wins': 1,
                'festival_appearances': ['SXSW', 'AFI Fest'],
                'festival_awards': {'SXSW': 'Audience Award'}
            },
            'moonlight': {
                'oscar_nominations': 8,
                'oscar_wins': 3,
                'golden_globe_nominations': 6,
                'golden_globe_wins': 1,
                'bafta_nominations': 4,
                'bafta_wins': 1,
                'festival_appearances': ['Telluride', 'Toronto', 'New York'],
                'festival_awards': {'Gotham Awards': 'Best Feature'}
            },
            'ex_machina': {
                'oscar_nominations': 2,
                'oscar_wins': 1,
                'golden_globe_nominations': 0,
                'golden_globe_wins': 0,
                'bafta_nominations': 5,
                'bafta_wins': 0,
                'festival_appearances': ['SXSW'],
                'festival_awards': {}
            },
            'parasite': {
                'oscar_nominations': 6,
                'oscar_wins': 4,
                'golden_globe_nominations': 3,
                'golden_globe_wins': 1,
                'bafta_nominations': 4,
                'bafta_wins': 2,
                'festival_appearances': ['Cannes', 'Telluride', 'Toronto'],
                'festival_awards': {'Cannes': 'Palme d\'Or'}
            }
        }
        
        # Return data if found, otherwise empty dict
        for key, data in mock_awards.items():
            if search_title in key:
                return data
        
        # If not found, return generic mock data
        return {
            'oscar_nominations': random.randint(0, 3),
            'oscar_wins': random.randint(0, 1),
            'golden_globe_nominations': random.randint(0, 3),
            'golden_globe_wins': random.randint(0, 1),
            'bafta_nominations': random.randint(0, 2),
            'bafta_wins': 0,
            'festival_appearances': random.sample(['Sundance', 'Cannes', 'Venice', 'Toronto', 'Berlin'], k=random.randint(0, 2)),
            'festival_awards': {}
        }
    
    def analyze_social_media_sentiment(self, film_title, platform='twitter', limit=100):
        """
        Analyze social media sentiment for a film
        Note: In production, this would require Twitter/X API access or similar
        """
        # Generate random sentiment analysis results
        positive = random.uniform(0.4, 0.8)
        negative = random.uniform(0.1, 0.3)
        neutral = 1 - positive - negative
        
        return {
            'film': film_title,
            'platform': platform,
            'sample_size': limit,
            'sentiment': {
                'positive': round(positive, 2),
                'negative': round(negative, 2),
                'neutral': round(neutral, 2)
            },
            'common_keywords': ['amazing', 'visual', 'acting', 'director', 'soundtrack'],
            'engagement_metrics': {
                'likes': random.randint(5000, 50000),
                'shares': random.randint(1000, 10000),
                'comments': random.randint(500, 5000)
            }
        }
    
    def get_company_strategy(self, company_name, sources=None):
        """
        Analyze company strategy based on articles and interviews
        """
        # Mock strategy insights
        strategy_insights = {
            'a24': {
                'key_themes': [
                    'Director-driven approach',
                    'Distinctive visual style',
                    'Strong festival circuit presence',
                    'Targeted marketing campaigns',
                    'Risk-taking on unique concepts'
                ],
                'notable_quotes': [
                    "We're not in the movie business, we're in the filmmaking business.",
                    "Our goal is to connect audiences with filmmakers who have a unique vision.",
                    "We look for films that have a strong point of view."
                ],
                'business_model': [
                    'Low to mid-budget productions',
                    'Theatrical + streaming hybrid strategy',
                    'Strong merchandising component',
                    'Building director relationships across multiple projects'
                ],
                'marketing_approach': [
                    'Distinctive poster art',
                    'Mysterious/cryptic trailers',
                    'Social media virality',
                    'Targeted audience segments'
                ]
            },
            'netflix': {
                'key_themes': [
                    'Data-driven content decisions',
                    'Global content strategy',
                    'High-volume production',
                    'Platform exclusivity',
                    'Diverse content portfolio'
                ],
                'notable_quotes': [
                    "We're not in the movie business, we're in the entertainment business.",
                    "Our competition isn't other streaming services, it's sleep.",
                    "We want to be everyone's second favorite content."
                ],
                'business_model': [
                    'Subscription-based revenue',
                    'High-volume content creation',
                    'Original IP development',
                    'Global distribution strategy'
                ],
                'marketing_approach': [
                    'Personalized recommendations',
                    'Algorithm-driven promotion',
                    'Limited theatrical windows',
                    'Star-driven marketing'
                ]
            },
            'neon': {
                'key_themes': [
                    'International film focus',
                    'Arthouse and prestige cinema',
                    'Awards-oriented strategy',
                    'Auteur-driven approach',
                    'Bold marketing campaigns'
                ],
                'notable_quotes': [
                    "We want to be the home for visionary filmmakers.",
                    "Our goal is to bring the best of global cinema to audiences.",
                    "We're not afraid to take risks on challenging material."
                ],
                'business_model': [
                    'Selective acquisitions',
                    'Festival-focused procurement',
                    'Boutique release strategy',
                    'Awards campaign investment'
                ],
                'marketing_approach': [
                    'Critical acclaim emphasis',
                    'Visually striking campaigns',
                    'Filmmaker-centered promotion',
                    'Cultural conversation creation'
                ]
            }
        }
        
        # Return data if found, otherwise generic insights
        company_key = company_name.lower().replace(' ', '')
        if company_key in strategy_insights:
            return strategy_insights[company_key]
        else:
            return {
                'key_themes': [
                    'Content-focused approach',
                    'Audience targeting',
                    'Competitive positioning',
                    'Brand identity development',
                    'Market expansion'
                ],
                'notable_quotes': [
                    "We're focused on delivering quality content that resonates with audiences.",
                    "Our strategy is to identify opportunities in the evolving media landscape.",
                    "We believe in the power of storytelling."
                ],
                'business_model': [
                    'Diversified revenue streams',
                    'IP development and acquisition',
                    'Strategic partnerships',
                    'Talent relationships'
                ],
                'marketing_approach': [
                    'Targeted campaigns',
                    'Digital-first strategy',
                    'Brand consistency',
                    'Audience engagement'
                ]
            }