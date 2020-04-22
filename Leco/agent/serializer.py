from rest_framework import serializers
from agent.models import Agent
from user.models import Profile


class CreateAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('first_name', 'last_name', 'username', 'phone_number', 'city', 'user_type')

        def to_representation(self, instance):
            """Convert `city` to persian."""
            ret = super().to_representation(instance)
            ret['city'] = instance.get_city_display()
            return ret

        def create(self, validated_data):
            profile_creator = self.context.get("user")
            profile = Profile.objects.create_user(username=validated_data["username"],
                                                  user_type="agent",
                                                  password=validated_data["phone_number"],
                                                  phone_number=validated_data["phone_number"])

            if "city" in validated_data.keys():
                profile.city = validated_data["city"]

            if "first_name" in validated_data.keys():
                profile.first_name = validated_data["first_name"]

            if "last_name" in validated_data.keys():
                profile.last_name = validated_data["last_name"]

            profile.save()
            agent = Agent.objects.create(profile=profile)
            if profile_creator.user_type == "agent":
                agent_top = profile_creator.agent
                agent.center = agent_top.center
                agent.top_agent = agent_top

            elif profile_creator.user_type == "center":
                agent.center = profile_creator.center
                agent.top_agent = None

            agent.save()
            return agent
