from django import forms
from .models import Project, ProjectTasks, TaskType, ResourceNames

class ProjectCreateForm(forms.ModelForm):
    order_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    delivery_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    completion_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    launch = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    install_Start = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    install_Finish = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectUpdateForm(forms.ModelForm):
    order_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    delivery_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    completion_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    launch = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    install_Start = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    install_Finish = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectTasksCreateForm(forms.ModelForm):
    start_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    finish_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = ProjectTasks
        fields = '__all__'

class TasksTypeCreateForm(forms.ModelForm):
    
    class Meta:
        model = TaskType
        fields = '__all__'

class ResourceCreateForm(forms.ModelForm):
    
    class Meta:
        model = ResourceNames
        fields = '__all__'