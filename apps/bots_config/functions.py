


def User_create_or_update(user, Profile):
    try:
        profile = Profile.objects.get(user_id=user.id)
        profile.username = user.username
        profile.fistname = user.first_name
        profile.lastname = user.last_name
        profile.is_bot = user.is_bot
        profile.language_code = user.language_code
        profile.save()

    except:
        new_user = Profile.objects.create(
            user_id=user.id,
            fistname=user.first_name,
            lastname=user.last_name,
            username=user.username,
            is_bot=user.is_bot,
            language_code=user.language_code
        )
        new_user.save()



