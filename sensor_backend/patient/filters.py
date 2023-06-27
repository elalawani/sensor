import django_filters
from django.db.models import Q
from .models import Patient


class PatientFilter(django_filters.FilterSet):
    byName = django_filters.CharFilter(method='filter_by_name')
    byBirthdate = django_filters.DateFilter(field_name='date_of_birth', lookup_expr='exact')
    byType = django_filters.CharFilter(field_name='gender', lookup_expr='exact')
    byCreator = django_filters.CharFilter(method='filter_by_creator')
    byMedications = django_filters.CharFilter(method='filter_by_medications')
    byCondition = django_filters.CharFilter(method='filter_by_condition')
    byDoctor = django_filters.CharFilter(method='filter_by_doctor')
    byNurse = django_filters.CharFilter(method='filter_by_nurse')

    class Meta:
        model = Patient
        fields = ['byName', 'byType', 'byBirthdate', 'byDoctor', 'byNurse',
                  'byCondition', 'byMedications', 'byCreator']

    def filter_by_name(self, queryset, name, value):
        names = value.split(' ')
        if len(names) == 1:
            return queryset.filter(Q(first_name__icontains=names[0]) | Q(last_name__icontains=names[0]))
        else:
            return queryset.filter(Q(first_name__icontains=names[0]) & Q(last_name__icontains=names[1]))

    def filter_by_doctor(self, queryset, name, value):
        return queryset.filter(doctors__name__exact=value)

    def filter_by_nurse(self, queryset, name, value):
        return queryset.filter(nurses__name__exact=value)

    def filter_by_creator(self, queryset, name, value):
        return queryset.filter(created_by__name__exact=value)

    def filter_by_condition(self, queryset, name, value):
        return queryset.filter(chronicConditions__name__exact=value)

    def filter_by_medications(self, queryset, name, value):
        return queryset.filter(medications__name__exact=value)
