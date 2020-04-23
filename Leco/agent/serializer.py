from rest_framework import serializers
from agent.models import Agent
from user.models import Profile


class CreateAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'username', 'phone_number', 'city')

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
        agent = None
        if profile_creator.user_type == "agent":
            agent_top = profile_creator.agent
            agent = Agent.objects.create(profile=profile,center=agent_top.center,top_agent= agent_top)

        elif profile_creator.user_type == "center":
            agent = Agent.objects.create(profile=profile,center=profile_creator.center ,top_agent= None)

        agent.save()
        return profile
