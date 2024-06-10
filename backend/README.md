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
- Pandas → This library will help as a DataBase for the project (users information, posts made, post saved, …)
- Faker → This library will be used in order to help the creation of fake data.

### Entities
1. User: account()
2. Profile:name,id,name,actions_s(user),actions_g(user),modift()
3. Account:log_in(),to_register(),request.
4. Comment:id,name,text
5. Like:id,name
6. Post:id,name,informationa,actions_g()
7. Repost:id,name,information,actions_g()
8. Mute:id,name,reason,changer()
9. Block:id,name,reason,changer()
10. Save:profile(user),account(user),


### Processes
1. Log in
   https://github.com/TomasCardenas00/project/blob/main/backend/images/log_in-diag.jpg
     
2. Reset password

   ![reset-password](https://github.com/TomasCardenas00/prueba/assets/163557446/1dd899a4-2d4f-4bea-b456-cb5aeae39ff9)
3. Post{Text, Images, Video, Audio, etc}

   ![post](https://github.com/TomasCardenas00/prueba/assets/163557446/c0e659cb-e736-49ec-9e18-9653425109f3)
4. Repost/Quote Post

   ![repost-quote](https://github.com/TomasCardenas00/prueba/assets/163557446/401c3633-3188-4934-90bd-4636f0c7329a)
5. Like a post()
   
   ![like-post](https://github.com/TomasCardenas00/prueba/assets/163557446/c39cb4d1-c216-4adf-8c95-c5b828131943)
6. Report post/account
   
   ![report](https://github.com/TomasCardenas00/prueba/assets/163557446/520f739d-a95e-4402-95e2-6fe1d5366d02)
7. Block an account
   
   ![block](https://github.com/TomasCardenas00/prueba/assets/163557446/2d9f2fdc-6396-4e70-87d6-3f8076663098)  
   
8. Modify account
   
   ![modify-account](https://github.com/TomasCardenas00/prueba/assets/163557446/053d5ee2-1912-4b8d-bfc0-06f68901d640)
9. Save posts

   ![save](https://github.com/TomasCardenas00/prueba/assets/163557446/15b320a8-a6d3-4853-9972-ca040a605a71)
   
10. Mute Content
   
   ![mute](https://github.com/TomasCardenas00/prueba/assets/163557446/a37a1e09-7ad5-421d-8c8c-05662befc86a)


