from djongo import models as mongo_models


class LogAdditionalInfo(mongo_models.Model):
    module = mongo_models.CharField()
    process = mongo_models.IntegerField()
    msecs = mongo_models.IntegerField()

    class Meta:
        abstract = True


class Log(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    user = mongo_models.CharField(max_length=100)
    message = mongo_models.TextField(max_length=1000)

    created_at = mongo_models.DateTimeField(auto_now_add=True)
    updated_at = mongo_models.DateTimeField(auto_now=True)

    additional_info = mongo_models.EmbeddedField(model_container=LogAdditionalInfo)

    class Meta:
        _use_db = 'nonrel'
        ordering = ("-created_at", )

    def __str__(self):
        return self.message
