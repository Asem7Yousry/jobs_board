Job : 
    - title
    - location
    - job type
    - description
    - published at
    - Vacancy
    - salary
    - category
    - experience 
    

    - apply job 
    - post job


Blog : 
    - title
    - description 
    - created_at
    - category
    - tags
    - author

    - search
    - comment
    - recent posts

contact
home


authentication steps:-
    -- create all templates for account authentication 
    -- create profile model for each user 
    -- create signal (create_new_profile) to create profile automaticlly when new user created (sign up)
    -- create form for sign up which inherit from (UserCreationForm) to take username and password and email from new user 
    -- link signup url to accounts app urls in project urls file 
    -- create template for signup process which take signup form 
    -- make signed up user login automaticlly once signed up
    -- start with profile steps :-
        _ create views for show and edit profile 
        _ create template of showing and edit profile in another directory called (accounts) in templates diroctery
        _ by (show_profile) function we could represent all data of user in better way with button for edit 
        _ create form for user data edit (UserEditForm) and another form to profile data edit (EditProfileForm) 
        _ pass the 2 form to edit ui profile to make user able to edit all data 
         

    