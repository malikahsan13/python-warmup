from tortoise.models import Model
from tortoise import fields

class PromptRecord(Model):
    id = fields.IntField(pk=True)
    user_id = fields.CharField(max_length=100)
    prompt = fields.TextField()
    response = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
