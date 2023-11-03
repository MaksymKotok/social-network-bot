import requests
import json
from pathlib import Path
from random import randint
from faker import Faker


if __name__ == "__main__":
    
    path = Path(__file__).with_name("config.json")
    with path.open() as f:
        config = json.loads(f.read())
        
    NUMBER_OF_USERS = randint(1, config["number_of_users"])

    # SIGNING UP USERS
    fake = Faker()
    headers = {"Content-Type": "application/json"}
    users = []
    for i in range(NUMBER_OF_USERS):
        data = {
            "username": fake.user_name(),
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "password": fake.password()
        }
        data["re_password"] = data["password"]
        users.append(data)
        data = json.dumps(data)
        
        response = requests.post(config["sign_up_url"], headers=headers, data=data)
        print(f"WELCOME, {users[i]["username"]}!")
        
    # GENERATING POSTS
    for user in users:
        NUMBER_OF_POSTS = randint(1, config["max_posts_per_user"])
        
        headers = {"Content-Type": "application/json"}
        data = json.dumps({key: user[key] for key in ("email", "password")})
        response = requests.post(config["auth_url"], headers=headers, data=data)
        
        user["access_token"] = response.json()["access"]
        
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {user["access_token"]}"}
        for i in range(NUMBER_OF_POSTS):
            data = json.dumps({
                "name": fake.sentence(),
                "text": fake.text(),
            })
            
            response = requests.post(config["post_url"], headers=headers, data=data)
            print(f"USER {user["username"]} CREATED POST: {response.json()["name"]}")
            
    # LIKING POSTS
    for user in users:
        response = requests.get(config["post_url"])
        
        posts = [p["id"] for p in response.json()]
        
        for user in users:
            NUMBER_OF_LIKES = randint(0, config["max_likes_per_user"])
            
            headers = {"Content-Type": "application/json"}
            data = json.dumps({key: user[key] for key in ("email", "password")})
            response = requests.post(config["auth_url"], headers=headers, data=data)
            
            user["access_token"] = response.json()["access"]
            
            headers = {"Content-Type": "application/json", "Authorization": f"Bearer {user["access_token"]}"}
            for i in range(NUMBER_OF_LIKES):
                post_id = posts[randint(0, len(posts) - 1)]
                
                response = requests.post(config["post_url"] + f"{post_id}/like/", headers=headers)
                print(f"USER {user["username"]} LIKED POST NO. {post_id}")
