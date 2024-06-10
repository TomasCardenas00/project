# READ ME
## Introduction
In this project, it will be developed and explained the creation of an social media application/platform where an user can make post about a variety of topics, share multimedia files (images, videos, GIFs, among others), interact with other users from the app, while also having moderation and regulation from the content posted, in order to make a respectful and enjoyable space and make new users more comfortable when joining the app.
## Business Model
The main reason this app will be developed is to give the people another posting social media platform, while attempting to become superior in other spaces these social media platforms have failed. One of the main money income the app will get will be from ad revenue, another income would come from the collaboration between the app and different brands and companies. Most of the money will be redirected onto the app maintenance (app renovations, server maintenance, bug fixing, etc).
### Business Rules
- The users must be over 17 years of age
- Users must not engage in the targeted harassment of someone, or incite other people to do so.
- Users must not promote violence.
- Users may not post or share photos or videos of someone that were produced or distributed without their consent

## User stories
- As a _user_, I want to be able to create a _profile_ with my personal information and a profile picture so that I can personalize my _account_.
- As a _user_, I want to be able to _like_ and _comment_, on other _user_, _user_ so that I can interact with them..
- As a _user_, I want to be able to _post_ short messages so I can share my thoughts with others.
- As a _user_, I want to be able to _repost_ the posts of others so I can share them with my followers.
- As a _user_, I want to be able to _like_ posts so I can show my appreciation for them.
- As a _user_, I want to be able to _user_ to posts so I can engage in discussions with others.
- As a _user_, I want to be able to _mute_ _accounts_ so I can avoid seeing certain content.
- As a _user_, I want to be able to _block_ accounts so I can avoid interaction with certain users.
- As a _user_, I want to be able to _save_ posts so I can easily find them again later.

## Technical definitions
### Tools
In this project, the backend will be done in *python*, in version *3.11.0,* there will be use of some python libraries to help the project
- Json → This library will help as a DataBase for the project (users information, posts made, accounts blocked, among others)
- Faker → This library will be used in order to help the creation of fake user, with also the help of creating different dake post's data.

### Entities
1. _User_: username, get_username()
2. _Autheticator_: new(), authenticate()
3. _Post_: text, likes, comments, saved, reports, to_dict(), like_post(), save_post(), add_comment(), report_post()
4. _TextPost(Post)_
5. _ImagePost(Post)_
6. _VideoPost(Post)_
7. _PostFactory_: create_post()
8. _SocialMediaFacade_: login(), create_post(), add_post(), like_post(), save_post(), add_comment(), report_post(), block_user(), quote_post(), report_user(), repost_post()

### Processes
1. Log in
   ![log-in](https://github.com/TomasCardenas00/project/blob/main/backend/images/log_in-diag.jpg)
     
2. Reset passwrod
   ![reset-password](https://github.com/TomasCardenas00/project/blob/main/backend/images/reset_password-diag.jpg)

3. Create account

   ![create.account](https://github.com/TomasCardenas00/project/blob/main/backend/images/create_acount-diag.jpg)
4. Make a Post{Text, Images, Video, Audio, etc}

   ![post](https://github.com/TomasCardenas00/project/blob/main/backend/images/make_a_post-diag.jpg)
5. Repost a Post

   ![repost](https://github.com/TomasCardenas00/project/blob/main/backend/images/repost_post-diag.jpg)
6. Quote a Post

   ![quote](https://github.com/TomasCardenas00/project/blob/main/backend/images/quote_post-diag.jpg)
7. Like a post:
   
   ![like-post](https://github.com/TomasCardenas00/project/blob/main/backend/images/like_post-diag.jpg)
8. Report account
   
   ![report](https://github.com/TomasCardenas00/project/blob/main/backend/images/report_account-diag.jpg)
9. Block an account
   
   ![block](https://github.com/TomasCardenas00/project/blob/main/backend/images/block_user-diag.jpg)  
   

