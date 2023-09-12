from rest_framework import serializers
from seeker.models import SeekerProfile, SeekerSkillSet, SkillSet, ExperienceDetails, EducationDetail


class SeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeekerProfile
        fields = "__all__"


class EducationDetailGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDetail
        fields = "__all__"


class EducationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDetail
        exclude = ("percentage",)


class ExperienceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceDetails
        fields = "__all__"


class SkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillSet
        fields = "__all__"


class SeekerSkillsetGetSerializer(serializers.ModelSerializer):
    skill_set = SkillSetSerializer()

    class Meta:
        model = SeekerSkillSet
        exclude = ("profile_account",)
