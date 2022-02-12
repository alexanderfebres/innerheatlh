from rest_framework import serializers

from .models import Appointment, Doctor, Especiality, Patient
from authentication.serializers import UserSerializer


class EspecialitySerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Especiality
        fields = (
            'pk',
            'name'
        )


class DoctorSerialiazer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    especiality = EspecialitySerialiazer(read_only=True)
    especiality_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Doctor
        fields = (
            'pk',
            'user',
            'user_id',
            'especiality',
            'especiality_id',
            'phone'
        )


class PatientSerialiazer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Patient
        fields = (
            'pk',
            'user',
            'user_id',
            'phone'
        )


class AppointmentSerialiazer(serializers.ModelSerializer):
    doctor = DoctorSerialiazer(read_only=True)
    doctor_id = serializers.IntegerField(write_only=True)

    patient = PatientSerialiazer(read_only=True)
    patient_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Appointment
        fields = (
            'pk',
            'motive',
            'doctor',
            'doctor_id',
            'patient',
            'patient_id',
            'state',
            'due_date'
        )
