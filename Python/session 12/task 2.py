#Given a list of song titles from Spotify with extra spaces and inconsistent casing, use map() and a lambda function to clean each 
# title so that it is stripped of spaces and converted to title case (e.g., ' shape OF you ' → 'Shape Of You')
songs = [
    " shape OF you ",
    " blinding LIGHTS ",
    "   save your tears ",
    " LeVitaTing ",
    " peaches "
]
print("uncleaned data is:-",songs)
clean_song=list(map(lambda song:song.strip().title(),songs))
print("after cleaning data :-")

print("cleaned data:-",clean_song)
