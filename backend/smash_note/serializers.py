from rest_framework import serializers
from smash_note.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = ("character_name","image_url")

    def get_image_url(self, obj):
        # /media/mario.jpg を /static/images/mario.jpg に変換
        if obj.image_url:
            filename = obj.image_url.name  # mario.jpg
            return f"/static/images/{filename}"
        return None
