def solution(genres, plays):
    answer = []
    genre_play_dict = {}
    genre_song_dict = {}


    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_play_dict:
            genre_play_dict[genre] = play
            genre_song_dict[genre] = [(i, play)]
        else:
            genre_play_dict[genre] += play
            genre_song_dict[genre].append((i, play))


    sorted_genre_play = sorted(genre_play_dict.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in sorted_genre_play:

        sorted_songs = sorted(genre_song_dict[genre], key=lambda x: x[1], reverse=True)

        answer.extend([song_id for song_id, _ in sorted_songs[:2]])

    return answer
