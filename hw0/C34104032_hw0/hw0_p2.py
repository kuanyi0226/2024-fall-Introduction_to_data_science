# read the input file without leading
def read_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    data = [line.strip().split(',') for line in lines[1:]]
    return data

# Q(1)Top-3 movies with the highest ratings in 2016? 
def top_3_movies_2016(data):
    #read the movies in 2016
    movies_2016 = [row for row in data if row[5] == '2016']  
    #sort movies_2016 by rating
    sorted_movies = sorted(movies_2016, key=lambda x: float(x[7]), reverse=True)  # 7: rating
    # Find the top 3 distinct rating values
    top_ratings = sorted(set(float(movie[7]) for movie in sorted_movies), reverse=True)[:3]

    result = []
    
    for i, rating in enumerate(top_ratings, start=1):
        # Find all movies with the current rating
        movies_with_rating = [movie[1] for movie in sorted_movies if float(movie[7]) == rating]
        
        # Add to the result
        result.append((i, rating, movies_with_rating))
    
    #print the result
    print("Rank    Rating     Movies")
    print("--------------------------------------")
    for rank, rating, movies in result:
        print(f"{rank:<7} {rating:<10} {', '.join(movies)}")

    return

# Q(2)The actor generating the highest average revenue? 
def actor_highest_avg_revenue(data):
    #using a dict to record 
    '''
    The way I define average revenue:
    Sum(the revenues of the movies that the actor worked with) / (number of the movies that the actor worked with)
    note that if the revenue is blank, we should not count the movie in
    '''
    actor_revenue = {}
    
    blank_counter = 0 #used for testing
    for row in data:
        #if blank, set -1
        revenue = float(row[9]) if row[9] else -1  #9: revenue
        #skip the movie if its revenue is blank
        if revenue >= 0:
            actors = row[4].split('|')  # 4: actor
            actors = [str.strip() for str in actors]
            
            #add the revenue to each actor
            for actor in actors:
                if actor not in actor_revenue:
                    actor_revenue[actor] = {'total_revenue': 0, 'movie_count': 0}
                actor_revenue[actor]['total_revenue'] += revenue
                actor_revenue[actor]['movie_count'] += 1
        else:
            blank_counter += 1
    #print(f"blank: {blank_counter}")    
    # Calculate average revenue per actor
    actor_avg_revenue = {actor: info['total_revenue'] / info['movie_count'] for actor, info in actor_revenue.items()}
    # Find the highest average revenue
    highest_avg_revenue = max(actor_avg_revenue.values())
    #print(sorted(actor_avg_revenue,key=actor_avg_revenue.get))
    # Find the actor(s) with the highest average revenue
    highest_avg_actors = [actor for actor, avg_revenue in actor_avg_revenue.items() if avg_revenue == highest_avg_revenue]
    
    #print the result
    for actor in highest_avg_actors:
        print(f"{actor}")
    print(f"(with the highest average revenue: {highest_avg_revenue} Millions)")
    return 

# Q(3)The average rating of Emma Watson’s movies?
def avg_rating_emma_watson(data):
    total_rating = 0
    count = 0
    
    for row in data:
        actors = row[4].split('|')  # 4: actor
        actors = [str.strip() for str in actors]
        #print(actors)
        if 'Emma Watson' in actors:
            #print(actors)
            total_rating += float(row[7])  # 7: rating
            count += 1
    #print(total_rating)
    #print(count)

    #print the result
    print(total_rating / count if count > 0 else 0)
    return 

# Q(4)Top-3 directors who collaborate with the most actors? 
def top_3_directors_most_actors(data):
    director_actor_count = {}
    
    for row in data:
        director = row[3]  # 3: director
        actors = row[4].split('|')  # 4: actor
        actors = [str.strip() for str in actors]
        
        if director not in director_actor_count:
            #use a set to store the actors' name for each director
            director_actor_count[director] = set()
        director_actor_count[director].update(actors)
    
    # Sort by the number of unique actors per director
    sorted_directors = sorted(director_actor_count.items(), key=lambda x: len(x[1]), reverse=True)
    # Find the top 3 distinct values for the number of actors
    top_actor_counts = sorted(set(len(actors) for director, actors in sorted_directors), reverse=True)[:3]
    
    #print(sorted_directors)
    result = []
    for i, count in enumerate(top_actor_counts, start=1):
        # Find directors who have this actor_count
        curr_directors = [director for director, actors in sorted_directors if len(actors) == count]
        result.append((i, count, curr_directors))

    #print the result
    print("Rank    # of Actors     Directors")
    print("--------------------------------------")
    for rank, count, directors in result:
        print(f"{rank:<7} {count:<15} {', '.join(directors)}")
    return 

# Q(5)Top-2 actors playing in the most genres of movies?
def top_2_actors_most_genres(data):
    actor_genres = {}
    
    for row in data:
        actors = row[4].split('|')  # 4: actor
        actors = [str.strip() for str in actors]
        genres = row[2].split('|')  # 2: genre
        genres = [str.strip() for str in genres]
        
        for actor in actors:
            if actor not in actor_genres:
                actor_genres[actor] = set()
            actor_genres[actor].update(genres)
    
    # Sort actors by the number of unique genres
    sorted_actors = sorted(actor_genres.items(), key=lambda x: len(x[1]), reverse=True)
    # Find the top 2 distinct values for the number of genres
    top_genre_counts = sorted(set(len(genres) for actor, genres in sorted_actors), reverse=True)[:2]
    
    #print(sorted_actors)
    result = []
    for i, count in enumerate(top_genre_counts, start=1):
        # Find actors who have this genre count
        actors_with_count = [actor for actor, genres in sorted_actors if len(genres) == count]
        result.append((i, count, actors_with_count))
    #print result
    print("Rank    # of Genres     Actors")
    print("--------------------------------------")
    for rank, count, actors in result:
        print(f"{rank:<7} {count:<15} {', '.join(actors)}")
    return

# Q(6)actors whose movies lead to the largest maximum gap of years?
def max_gap_years(data):
    actor_years = {}
    
    for row in data:
        year = int(row[5])  # 5: year
        actors = row[4].split('|')  # 4: actor
        actors = [str.strip() for str in actors]
        
        #update an actor's years
        for actor in actors:
            if actor not in actor_years:
                actor_years[actor] = set()
            actor_years[actor].add(year)
    
    # calculate the maximum gap of years for each actor
    actor_max_gap = {}
    for actor, years in actor_years.items():
        actor_max_gap[actor] = max(years) - min(years)
    
    # Find all actors with the largest gap
    largest_maximum_gap = max(actor_max_gap.values())
    actors_with_max_gap = [actor for actor, gap in actor_max_gap.items() if gap == largest_maximum_gap]

    #print the result
    for actor in actors_with_max_gap:
        print(actor)
    
    print(F"({len(actors_with_max_gap)} actors with the largest maximum gap of years: {largest_maximum_gap})")
    
    return
# Q(7)Find all actors who collaborate with Johnny Depp in direct and indirect ways
def johnny_depp_collaborators(data):
    actor_collabs = {}
    
    # Build the actor collaboration graph
    for row in data:
        actors = row[4].split('|')  # 4: actor
        actors = [str.strip() for str in actors]
        
        for actor in actors:
            if actor not in actor_collabs:
                actor_collabs[actor] = set()
            actor_collabs[actor].update(actors)
    
    # Perform a breadth-first search to find all collaborators (direct and indirect)
    collaborators = set()
    queue = ['Johnny Depp']
    
    while queue:
        current_actor = queue.pop(0)
        if current_actor in collaborators:
            continue
        collaborators.add(current_actor)
        queue.extend(actor_collabs.get(current_actor, []))
    
    collaborators.remove('Johnny Depp')
    print(len(collaborators))
    return collaborators

# Load the CSV file
folder = 'C34104032_hw0/'
file_path = 'IMDB-Movie-Data.csv'
data = read_csv_file(file_path)
#print(data)

#1
print('Q1:')
top_3_movies_2016(data)
#2
print('Q2:')
actor_highest_avg_revenue(data)
#3
print('Q3:')
avg_rating_emma_watson(data)
#4
print('Q4:')
top_3_directors_most_actors(data)
#5
print('Q5:')
top_2_actors_most_genres(data)
#6
print('Q6:')
max_gap_years(data)
#7
print('Q7:')
#johnny_depp_collaborators(data)
