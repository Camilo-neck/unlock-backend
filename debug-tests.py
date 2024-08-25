# import src.controllers.auth as auth

# response = auth.singin(
#     email="jorozcove+unlock@unal.edu.co",
#     password="Unlock@123"
# )

# print(response.session.access_token)

from src.controllers.users import get_user_by_id
print(get_user_by_id("dbfa692d-03a2-4557-9668-e8206aa581df"))