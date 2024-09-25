# read the input file
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
    return [movie[1] for movie in sorted_movies[:3]]  # 1: title

# Q(2)The actor generating the highest average revenue? 
def actor_highest_avg_revenue(data):
    #using a dict to record 
    actor_revenue = {}
    
    for row in data:
        revenue = float(row[9]) if row[9] else 0  # Assuming column 9 is 'Revenue (Millions)'
        actors = row[4].split('|')  # 4: actor
        actors = [str.strip() for str in actors]
        
        for actor in actors:
            if actor not in actor_revenue:
                actor_revenue[actor] = {'total_revenue': 0, 'movie_count': 0}
            actor_revenue[actor]['total_revenue'] += revenue
            actor_revenue[actor]['movie_count'] += 1
    
    # Calculate average revenue per actor
    actor_avg_revenue = {actor: info['total_revenue'] / info['movie_count'] for actor, info in actor_revenue.items()}
    #print(sorted(actor_avg_revenue,key=actor_avg_revenue.get))
    # Find the actor with the highest average revenue
    highest_avg_actor = max(actor_avg_revenue, key=actor_avg_revenue.get)
    
    return highest_avg_actor

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
            total_rating += float(row[7])  # Assuming column 8 is 'Rating'
            count += 1
    #print(total_rating)
    #print(count)
    return total_rating / count if count > 0 else 0
# Q(4)Top-3 directors who collaborate with the most actors? 
def top_3_directors_most_actors(data):
    director_actor_count = {}
    
    for row in data:
        director = row[3]  # Assuming column 3 is 'Director'
        actors = row[4].split('|')  # 4: actor
        actors = [str.strip() for str in actors]
        
        if director not in director_actor_count:
            #use a set to store the actors' name for each director
            director_actor_count[director] = set()
        director_actor_count[director].update(actors)
    
    # Sort by the number of unique actors per director
    sorted_directors = sorted(director_actor_count.items(), key=lambda x: len(x[1]), reverse=True)
    
    return [director[0] for director in sorted_directors[:3]]
# Q(5)Top-2 actors playing in the most genres of movies?
def top_2_actors_most_genres(data):
    actor_genres = {}
    
    for row in data:
        actors = row[4].split('|')  # 4: actor
        actors = [str.strip() for str in actors]
        genres = row[2].split('|')  # 2: genre
        genres = [str.strip() for str in actors]
        
        for actor in actors:
            if actor not in actor_genres:
                actor_genres[actor] = set()
            actor_genres[actor].update(genres)
    
    # Sort actors by the number of unique genres
    sorted_actors = sorted(actor_genres.items(), key=lambda x: len(x[1]), reverse=True)
    
    return [actor[0] for actor in sorted_actors[:2]]
# Q(6)Top-3 actors whose movies lead to the largest maximum gap of years?
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
    
    # Sort by the maximum gap of years
    sorted_actors = sorted(actor_max_gap.items(), key=lambda x: x[1], reverse=True)
    
    return [actor[0] for actor in sorted_actors[:3]]
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
print(top_3_movies_2016(data))
#2
print('Q2:')
print(actor_highest_avg_revenue(data))
#3
print('Q3:')
print(avg_rating_emma_watson(data))
#4
print('Q4:')
print(top_3_directors_most_actors(data))
#5
print('Q5:')
print(top_2_actors_most_genres(data))
#6
print('Q6:')
print(max_gap_years(data))
#7
print('Q7:')
print(johnny_depp_collaborators(data))
