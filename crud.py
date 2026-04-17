from sqlalchemy.orm import Session
import auth
import models 
import schemas 

# --- Categories ---

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def read_categories(db: Session):
    return db.query(models.Category).all()
# --- Items ---
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict()) # Автоматично напасва полетата
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemUpdate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        for key, value in item.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False
# --- Users ---
def create_user(db: Session, user: schemas.UserCreate):
    hashed_pwd = auth.hash_password(user.password) # Хешираме!
    db_user = models.User(username=user.username, hashed_password=hashed_pwd, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

