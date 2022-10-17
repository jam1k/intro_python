# Write your solution here:
class Series:
    def __init__(self, title:str, season_number:int, genres:list):
        self.title = title
        self.season_number = season_number
        self.genres = genres
        self.rating = []

    def __str__(self):

        genre_string = ", ".join(self.genres)
        first=f"{self.title} ({self.season_number} seasons)\n"
        second = f"genres: {genre_string}\n"
        if len(self.rating) == 0:
            third = "no ratings"
        else:
            third = f"{len(self.rating)} ratings, average {sum(self.rating)/len(self.rating):.1f} points"
        string_to_print= first+second+third
        return string_to_print
    
    def rate(self, rating:int):
        self.rating.append(rating)


def minimum_grade(rating: float, series_list: list):
    result = []
    for series in series_list:

        series_rate = sum(series.rating)/len(series.rating)
        if series_rate > rating:
            result.append(series)
    return result


def includes_genre(genre: str, series_list: list):
    result = []
    for series in series_list:
        if genre in series.genres:
            result.append(series)
    return result


if __name__=="__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)