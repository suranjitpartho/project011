from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from App_RFA.models import Monthly, Target


# MODELS REGISTER:

@admin.register(Monthly)
class MonthlyAdmin(ImportExportModelAdmin):
    list_display = ('Time_Period', 'Area', 'Sector', 'Project', 'Community', 'Results_Level', 'Frequency', 'Indicator_ID', 'Indicator',
    'Activity', 'Unit', 'Actual', 'Male_Under5', 'Female_Under5', 'Male_Above5', 'Female_Above5', 'Male_PWD', 'Female_PWD')


@admin.register(Target)
class TargetAdmin(ImportExportModelAdmin):
    list_display = ('Time_Period', 'Area', 'Sector', 'Project', 'Community', 'Results_Level', 'Frequency', 'Indicator_ID', 'Indicator',
    'Activity', 'Unit', 'Target')
