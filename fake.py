from faker import Faker
import random
from datetime import datetime, timedelta
from database import SessionLocal, engine, Base
import models

Base.metadata.create_all(bind=engine)

fake = Faker()


def create_fake_tasks(n=50):
    db = SessionLocal()

    for _ in range(n):
        task = models.Task(
            title=fake.sentence(nb_words=4),
            description=fake.text(max_nb_chars=100),
            priority=random.randint(1, 3),
            completed=random.choice([True, False]),
            due_date=datetime.utcnow() + timedelta(days=random.randint(1, 30))
        )
        db.add(task)

    db.commit()
    db.close()
    print(f"{n} fake tasks created.")


if __name__ == "__main__":
    create_fake_tasks(100)
