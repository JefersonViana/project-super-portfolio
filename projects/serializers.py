from rest_framework import serializers
from .models import (
    Profile,
    Project,
    CertifyingInstitution,
    Certificate,
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class NestedCertificateSerializer(serializers.ModelSerializer):
    # foi retirado o field profile e funcionou, porque?
    class Meta:
        model = Certificate
        fields = ('id', 'name')


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ('id', 'name', 'url', 'certificates')

    def create(self, validated_data):
        # mostra os dados que chega
        # print(validated_data, 'VALIDADE DATA')

        # retorna uma lista de [{"name": "certificado 1"},
        # {"name": "certificado 2"}]
        certificates_data = validated_data.pop('certificates')

        # criando a instituição certificadora
        certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        # for para criar os certificados e porque não tem o profile?
        for certificate_data in certificates_data:
            # isso aqui funcionaria?
            # Certificate.objects.create(
            #     certifying_institution=certifying_institution,
            #     **certificate_data
            # )
            CertificateSerializer().create(
                {
                    'certifying_institution': certifying_institution,
                    **certificate_data
                }
            )
        return certifying_institution
