from rest_framework import serializers
from inmuebleslist_app.models import Inmueble, Empresa, Persona, Interesado
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Persona
        fields = "__all__"
    def validate_nombrePersona(self, data):
        if len(data) < 4:
            raise serializers.ValidationError("el nombre es muy corto")
        else:
            return data

class InteresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Interesado
        fields = "__all__"

class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields="__all__"
        #exclude = ['id']
    def validate(self, data):
        if data['direccion']==data['pais']:
            raise serializers.ValidationError("la direccion y el pais deben ser diferentes")
        else:
            return data
    def validate_imagen(self, data):
        if len(data) < 2:
            raise serializers.ValidationError("La url de la imagen es muy corta o no es valida")
        else:
            return data
class EmpresaSerializer(serializers.ModelSerializer):
    Inmueblelist = InmuebleSerializer(many=True, read_only=True)
    class Meta:
        model= Empresa
        fields = "__all__"
    def validate_website(self, data):
        if len(data) < 2:
            raise serializers.ValidationError("La web es muy corta")
        else:
            return data



# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("la direccion es demasiado corta")

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitud])
#     pais = serializers.CharField(validators=[column_longitud])
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
#     caracteristicas = serializers.JSONField(required=False)
#     #crear
#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data)
#     #actulizar
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion',instance.direccion)
#         instance.pais = validated_data.get('pais',instance.pais)
#         instance.descripcion = validated_data.get('descripcion',instance.descripcion)
#         instance.imagen = validated_data.get('imagen',instance.imagen)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
#     def validate(self, data):
#         if data['direccion'] == data['pais']:
#             raise serializers.ValidationError("la direccion y el pais deben ser diferentes")
#         else:
#             return data