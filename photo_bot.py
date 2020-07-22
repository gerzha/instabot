from instapy import InstaPy
from instapy import smart_run

insta_username = "xxx"
insta_password = "xxx"


# get a session!
session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)

# let's go! :>
with smart_run(session):
    other_locale = ['1023936095/', "790750200/minsk/", 'locations/1023936095/',  "229302938/gorky-park-minsk/", "500112008/"]
    locations = ['790750200/minsk/']

    # general settings
    session.set_skip_users(skip_business=True, skip_no_profile_pic=True, skip_private=True)
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=20,
                                 peak_likes_daily=400,
                                 peak_comments_hourly=30,
                                 peak_comments_daily=60,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=50,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)
    session.set_dont_like(['sad', 'rain', 'depression'])
    session.set_do_follow(enabled=True, percentage=80, times=1)
    session.set_do_comment(enabled=True, percentage=80)

    # session.set_comments([
    #                          u'Очень крутое фото! :heart_eyes: Взгляни на '
    #                          u'мои работы',
    #                          u'Это фото огонь :heart_eyes:'
    #                          u'если есть минутка - оцени мои) :wink:',
    #                          u'Очень крутое фото :heart_eyes:  определенно лайк! ',
    #                          u'Классный пост, :heart_eyes: '
    #                          u'оцените мой:wink:',
    #                          u'Отличный снимок :heart_eyes: мне нравится! :wink:',
    #                          u'Удачное фото :heart_eyes: '
    #                          u'Как считаете, мои такие же? :wink:',
    #                          u'Мне нравятся Ваши фото, а Вам мои?) :wink:',
    #                          u'Делайте больше таких постов, это круто! :wink:',
    #                          u'Ради этого стоило заходить на Вашу страничку. :smiley:'
    #                          u'Как Вам моя?) :wink:'],
    #                      media='Photo')
    session.set_comments([
                             u'Это фото огонь! :heart_eyes: Если есть минутка '
                             u'оцени мои :wink:',
                             u'Очень крутое фото, определенно лайка :heart_eyes:'
                             u'если есть минутка - оцени мои) :wink:',
                             u'Очень крутое фото :heart_eyes:  определенно лайк! ',
                             u'Классный пост, :heart_eyes: '
                             u'оцените мой:wink:',
                             u'Отличный снимок :heart_eyes: мне нравится! :wink:',
                             u'Удачное фото :heart_eyes: '
                             u'Как считаете, мои такие же? :wink:',
                             u'Мне нравятся Ваши фото, а Вам мои?) :wink:',
                             u'Делайте больше таких постов, это круто! :wink:',
                             u'Ради этого стоило заходить на Вашу страничку. :smiley:'
                             u'Как Вам моя?) :wink:',
                             u'Какая живая фотография!',
                             u'Классный пост, так держать!',
                             u'Какое фото :heart_eyes: :heart_eyes: :heart_eyes:',
                             u'Красиво :smiley:',
                             u'Прикольно:wink:',
                             u'Однозначно круто!:smiley:',
                             u'Фото классное, фотографу респект!',
                             u'Хорошая фотография получилась на мой взгляд :smiley:',
                             u'Фотография получилась очень даже огонь!:heart_eyes:',
                             u'Прикольное, яркое у вас фото получилось!:ok_hand:',
                             u'Фото класс :raised_hands:! Буду рада, если посмотрите мои',
                             u'Вау, какое фото у вас! Мне нравятся такие. Возможно, Вам мои тоже понравятся :smiley:',
                             u'Очень мило :smiley:',
                             u'Красота в деталях :heart_eyes:',
                             u'Красота в мелочах, здорово у Вас получилось :smiley:',
                             u'За такую фотографию однозначно лайк :heart_eyes:',
                             u'Смотрится очень классно!',
                             u'Хороший кадр :+1:, мне нравятся такие. А как Вам мои?',
                             u'Чудесные фото у вас!:smiley:',
                             u'Хорошие фото у вас в профиле :smiley:',
                             u'Побольше бы таких теплых фото, как у вас в профиле :smiley:'], media='Photo')



    session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max_likes=200, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=2000,
                                    min_followers=50,
                                    min_following=50)


    session.set_user_interact(amount=10, randomize=True, percentage=80)

    # activity
    session.like_by_locations(locations, amount=90)

    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=501)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="all",
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=501)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='general', engagement_mode='no_comments')
