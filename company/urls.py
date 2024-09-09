from django.urls import path
from . import views as compView

urlpatterns = [
    path('',compView.Branches,name="branches"),
    path('branche/<int:branche_id>',compView.BrancheDetails,name="branchesDetails"),
    path('newbranche',compView.newBranche,name="newBranche"),
    path('branche/<int:branche_id>/newDepartment',compView.newDepartmentToBranche,name="newDepartmentToBranche"),
]