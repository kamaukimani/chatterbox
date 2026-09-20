from flask import Blueprint,request,make_response
from app.models import Message

message_bp=Blueprint("message",__name__)
@message_bp.route('/all',methods=["GET"])
def messages():
    messages=[]
    
    for message in Message.query.all():
        message_dict=message.to_dict()
        messages.append(message_dict)
    response=make_response(
        messages,
        200
    )
    return response
@message_bp.route('/<int:id>',methods=["GET"])
def message_by_id(id):
    message=Message.query.filter(Message.id == id).first()
    if message is None:
        response={
            "message":"OOPss!!!!The record does not exist in our database!!!!"
        }
        return response,404
    message_dict=message.to_dict()
    response=make_response(
        message_dict,
        200
    )
    return response