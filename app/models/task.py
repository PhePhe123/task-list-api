from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    # is_complete = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, default=None)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"), nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")


    @classmethod
    def from_dict(cls, task_data):
        new_task = Task(
            title = task_data["title"],
            description = task_data["description"]
        )

        return new_task

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": bool(self.completed_at)
        }

    def to_dict_with_goal(self):
        return {
            "id": self.task_id,
            "goal_id":self.goal_id,
            "title": self.title,
            "description": self.description,
            "is_complete": bool(self.completed_at)
        }