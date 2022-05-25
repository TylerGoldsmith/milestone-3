from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
from .models import User_Account, Review, Genre, Game, Publisher, Game_Publisher, Platform, Game_Platform
 
class Custom_User_Account_Form(UserCreationForm):    
    class Meta:        
        model = User_Account        
        fields = ('id', 'username', 'email', 'enc_pw_ua')
        # read_only_field = ['is_active', 'created', 'updated']
class Custom_User_Account_Change_Form(UserChangeForm):    
    class Meta:        
        model = User_Account        
        fields = UserChangeForm.Meta.fields

# class Custom_Review_Form(Review_Creation_Form):  
#     class Meta:
#         model: Review
#         fields: ('id', 'review', 'created_at', 'user_account_id')

# class Custom_Review_Change_Form(Review_Change_Form):   
#     class Meta:
#         model: Review
#         fields = Review_Change_Form.Meta.fields

# class Custom_Genre_Form(Genre_Creation_Form):  
#     class Meta:
#         model = Genre
#         fields = ('id', 'genre_name')

# class Custom_Genre_Change_Form(Genre_Change_Form):   
#     class Meta:
#         model = Genre
#         fields = Genre_Change_Form.Meta.fields

# class Custom_Game_Form(Game_Creation_Form):  
#     class Meta:
#         model = Game
#         fields = ('id', 'genre_id', 'game_name','game_description')

# class Custom_Game_Change_Form(Game_Change_Form):   
#     class Meta:
#         model = Game
#         fields = Game_Change_Form.Meta.fields

# class Custom_Publisher_Form(Publisher_Creation_Form):  
#     class Meta:
#         model = Publisher
#         fields = ('id', 'publisher_name')

# class Custom_Publisher_Change_Form(Publisher_Change_Form):   
#     class Meta:
#         model = Publisher
#         fields = Publisher_Change_Form.Meta.fields

# class Custom_Game_Publisher_Form(Game_Publisher_Creation_Form):  
#     class Meta:
#         model = Game_Publisher
#         fields = ('id', 'game_id', 'game_publisher_id')

# class Custom_Game_Publisher_Change_Form(Game_Publisher_Change_Form):    
#     class Meta:
#         model = Game_Publisher
#         fields = Game_Publisher_Change_Form.Meta.fields

# class Custom_Platform_Form(Platform_Creation_Form):  
#     class Meta:
#         model = Platform
#         fields = ('id', 'platform_name')

# class Custom_Platform_Change_Form(Platform_Change_Form):   
#     class Meta:
#         model = Platform
#         fields = Platform_Change_Form.Meta.fields


# class Custom_Game_Platform_Form(Game_Platform_Creation_Form):  
#     class Meta:
#         model = Game_Platform
#         fields = ('id', 'platform_id', 'release_year')

# class Custom_Game_Platform_Change_Form(Game_Platform_Change_Form):    
#     class Meta:
#         model = Game_Platform
#         fields = Game_Platform_Change_Form.Meta.fields