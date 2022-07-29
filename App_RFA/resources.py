from import_export import resources
from App_RFA.models import Monthly, Target

class MonthlyResource(resources.ModelResource):
    class Meta:
        model = Monthly
        fields = ('Time_Period', 'Area', 'Sector', 'Project', 'Community', 'Results_Level', 'Frequency', 'Indicator_ID', 'Indicator', 'Activity', 'Unit', 'Actual', 'Male_Under5', 'Female_Under5', 'Male_Above5', 'Female_Above5', 'Male_PWD', 'Female_PWD')
        export_order = ('Time_Period', 'Area', 'Sector', 'Project', 'Community', 'Results_Level', 'Frequency', 'Indicator_ID', 'Indicator', 'Activity', 'Unit', 'Actual', 'Male_Under5', 'Female_Under5', 'Male_Above5', 'Female_Above5', 'Male_PWD', 'Female_PWD')


class TargetResource(resources.ModelResource):
    class Meta:
        model = Target
        fields = ('Time_Period', 'Area', 'Sector', 'Project', 'Community', 'Results_Level', 'Frequency', 'Indicator_ID', 'Indicator', 'Activity', 'Unit', 'Target')
        export_order = ('Time_Period', 'Area', 'Sector', 'Project', 'Community', 'Results_Level', 'Frequency', 'Indicator_ID', 'Indicator', 'Activity', 'Unit', 'Target')