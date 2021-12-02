from application import app, db
from application.models import Team, Players
from flask import render_template, request, redirect, url_for, Response, jsonify

# @app.route('/create/team'), methods=['POST'])
# def create_team():
#     json= request.json
#     new_team = Teams( team_name="new team")
#     db.session.add(new_team)
#     db.session.commit()
#     return f"Team with teamid {new_team.team_id} added to database"
 
 @app.route('/create/team'), methods=['POST'])
 def create_team():
    json= request.json
    new_team = Teams( 
        name = json["name"],
    )           
    db.session.add(new_team)
    db.session.commit()
    return f"Team '{new_team.name} added to database"   


# @app.route('/create/player'), methods=['POST']) 
# def create_player():
#     new_player = Players(player_name="new player", player_position="ST", team_id= 1)
#     db.session.add(new_player)
#     db.session.commit()
#     return f"Player with playerid {new_player.player_id} added to database"

@app.route('/create/player/<int:team_id>'), methods=['POST']) 
def create_player(team_id):
    json = request.json
    new_player = Players(
       name= json["name"], 
       position= json["position"]
    )   
    db.session.add(new_player)
    db.session.commit()
    return f"Player '{new_player.player}' added to database"

#get all the players related to team players.team
@app.route('/get/allPlayers', methods=['GET']) 
def get_all_players():    
    all_players =Players.query.all()
    json = {"players" : []}
    for players in all_players:      #for loop to go over all the players 
        teams =[]                    # list of team add to empty list then attach list of all the players relate to team
        for teams in players.team:
            teams.append ()
                {
                    "id": team.id.
                    "name":team_name
                }
   
        json["players"].append(          #attach that list to the information of players
            {
               "id": player.player_id
               "name": player.player_name
               "position": position.player_position
            }

        )
    return jsonify(json)             





@app.route('/delete/player/<int:id>', methods=["DELETE"])
def delete_player(id):
    player = player.query.get(id)
    db.session.delete(player)
    return f"player '{player.name}' player deleted "






#
# @app.route('/create/task', methods=['POST'])
# def create_task():
#     package = request.json
#     new_task = Tasks(description=package["description"])
#     db.session.add(new_task)
#     db.session.commit()
#     return Response(f"Added task with description: {new_task.description}", mimetype='text/plain')

# @app.route('/read/allTasks', methods=['GET'])
# def read_tasks():
#     all_tasks = Tasks.query.all()
#     tasks_dict = {"tasks": []}
#     for task in all_tasks:
#         tasks_dict["tasks"].append(
#             {
#                 "id": task.id,
#                 "description": task.description,
#                 "completed": task.completed
#             }
#         )
#     return jsonify(tasks_dict)

# @app.route('/read/task/<int:id>', methods=['GET'])
# def read_task(id):
#     task = Tasks.query.get(id)
#     tasks_dict = {
#                     "id": task.id,
#                     "description": task.description,
#                     "completed": task.completed
#                 }
#     return jsonify(tasks_dict)

# @app.route('/update/task/<int:id>', methods=['PUT'])
# def update_task(id):
#     package = request.json
#     task = Tasks.query.get(id)
#     task.description = package["description"]
#     db.session.commit()
#     return Response(f"Updated task (ID: {id}) with description: {task.description}", mimetype='text/plain')

# @app.route('/delete/task/<int:id>', methods=['DELETE'])
# def delete_task(id):
#     task = Tasks.query.get(id)
#     db.session.delete(task)
#     db.session.commit()
#     return Response(f"Deleted task with ID: {id}", mimetype='text/plain')

# @app.route('/complete/task/<int:id>', methods=['PUT'])
# def complete_task(id):
#     task = Tasks.query.get(id)
#     task.completed = True
#     db.session.commit()
#     return Response(f"Task with ID: {id} set to completed = True", mimetype='text/plain')

# @app.route('/incomplete/task/<int:id>', methods=['PUT'])
# def incomplete_task(id):
#     task = Tasks.query.get(id)
#     task.completed = False
#     db.session.commit()
#     return Response(f"Task with ID: {id} set to completed = False", mimetype='text/plain')
