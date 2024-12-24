import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def get_ifo(self):
        return self.nickname, self.password

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User (nickname,password,age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} зарегистрирован и вошел в систему')

    def log_out(self):
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user
                return user

    def add(self, *videos:Video):
        for video in videos:
            if video.title not in self. videos:
                self.videos.append(video)

    def get_videos(self, text):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video)
        return list_movie

    def watch_video(self, movie):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for video in self.videos:
                if movie in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def __str__(self):
        return f"{self.videos}"
if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')