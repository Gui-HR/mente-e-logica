#Restrição de idade para filme
class Movie:
    def __init__(self, name, classification_age, time):
        self.name = name
        self.classification_age = classification_age
        self.time = time

released_movies = [Movie('Duna', 10, '16:30'),
                   Movie('Duna2', 18, '19:15'),
                   Movie('Pokémon', 0, '23:00')]

user_movie = input('Qual filme você deseja assistir? ')
user_age = int(input('Qual sua idade? '))

for i in range(len(released_movies)):
    movie_name = released_movies[i].name
    movie_classification = released_movies[i].classification_age
    movie_time = released_movies[i].time

    if user_movie == movie_name:
        if movie_classification <= user_age:
            print(f'Filme Disponivel, a seção começará as {movie_time}.')
        else:
            print(f'A classificação indicativa deste filme e para maiores de {movie_classification}, portanto você não pode assistir este filme.')

        break
    
    if (len(released_movies) - 1) == i:
        print('Este filme não está disponível no momento.')