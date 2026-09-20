from datetime import datetime
from sqlalchemy.orm import Mapped,mapped_column
from app.db import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import func

class Message(db.Model,SerializerMixin):
    __tablename__="messages"

    id:Mapped[int]=mapped_column(primary_key=True)
    body:Mapped[str]
    username:Mapped[str]
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())

    def __repr__(self):
        return f"<Message ({self.id}): {self.username}, {self.body}>"