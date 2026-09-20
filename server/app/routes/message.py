from flask import Blueprint,request,make_response
from app.models import Message
from app.db import db

message_bp=Blueprint("message",__name__)
@message_bp.route('/all',methods=["GET","POST"])
def messages():
    if request.method == "GET":
        messages=[]
    
        for message in Message.query.all():
            message_dict=message.to_dict()
            messages.append(message_dict)
        response=make_response(
            messages,
            200
        )
        return response
    elif request.method == "POST":
        data=request.get_json()
        message=Message()
        allowed_fields=["body","username"]
        for attr in data:
            if attr in allowed_fields:
                setattr(message,attr,data[attr])
        db.session.add(message)
        db.session.commit ()

        message_dict=message.to_dict()
        response=make_response(
            message_dict,
            201
        )
        return response



@message_bp.route('/<int:id>',methods=["GET","PATCH","DELETE"])
def message_by_id(id):
    message=Message.query.filter(Message.id == id).first()
    if message is None:
        response={
            "message":"OOPss!!!!The record does not exist in our database!!!!"
        }
        return response,404
    if request.method == "GET":
        message_dict=message.to_dict()
        response=make_response(
            message_dict,
            200
        )
        return response
    elif request.method == "PATCH":
        data=request.get_json()
        allowed_fields=["body"]
        for attr,value in data.items():
            if attr in allowed_fields:
                setattr(message,attr,value)
        db.session.add(message)
        db.session.commit()

        message_dict=message.to_dict()
        response=make_response(
            message_dict,
            200
        )
        return response
    elif request.method == "DELETE":
        db.session.delete(message)
        db.session.commit()

        response={
            "deleted_successfully":True,
            "message":"Message deleted successfully"
        }
        return make_response(response,200)