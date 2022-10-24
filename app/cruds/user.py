from sqlalchemy.orm import Session

import datetime
import models.models as models
import schemas.user as user_schema

async def create_user(
    db: Session, user_create: user_schema.UserCreate
) -> models.User:
    user = models.User(**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

