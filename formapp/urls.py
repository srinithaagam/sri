from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('accident/', views.accident_register_form, name='accident'),
    path('actionplan/', views.actionplan_register_form, name='actionplan'),
    path('asset/', views.asset_form, name='asset'),
    path('awarness/', views.awareness_register, name='awarness'),
    path('bp_pulse/', views.bp_pulsenote_form, name='bp_pulse'),
    path('case_history/', views.case_history_form, name='case_history'),
    path('counselling/',views.counselling_register_form,name='counselling'),
    path('death/',views.death_register_form,name='death'),
    path('employment_link/', views.employment_link_form, name='employment_link'),
    path('food_menu/', views.food_menu, name='food_menu'),
    path('inspection/', views.inspection_register, name='inspection'),
    path('master_record/', views.master_records, name='master_record'),
    path('medical_camp/', views.medical_camp_form, name='medical_camp'),
    path('medicine/', views.medicine_form, name='medicine'),
    path('night_survey/', views.night_survey_form, name='night_survey'),
    path('performance_appraisal/', views.performance_appraisal_form, name='performance_appraisal'),
    path('provision', views.provision_form, name='provision'),
    path('rehabilitation/', views.rehabilitation_form, name='rehabilitation'),
    path('reintegration/', views.reintegration_form, name='reintegration'),
    path('resident/', views.resident_form, name='resident'),
    path('Salary/', views.Salary_Register, name='Salary'),
    path('skill_training/', views.skill_training_form, name='skill_training'),
    path('smc/', views.smc_register_form, name='smc'),
    path('social_entertainment/', views.social_entertainment_form, name='social_entertainment'),
    path('staff_attendence/', views.staff_attendence_form, name='staff_attendence'),
    path('staff_movement/', views.staff_movement, name='staff_movement'),
    path('stock/', views.stock_form, name='stock'),
    path('visitor/', views.visitor_register_form, name='visitor'),


    path('accident_register_dashboard/', views.accident_register_dashboard, name='accident_register_dashboard'),
    path('action_plan_register_dashboard/', views.action_plan_form_dashboard, name='action_plan_register_dashboard'),
    path('asset_register_dashboard/', views.asset_register_dashboard, name='asset_register_dashboard'),
    path('awareness_register_dashboard/', views.awareness_register_dashboard, name='awareness_register_dashboard'),
    path('bp_form_register_dashboard/', views.bp_form_dashboard, name='bp_form_register_dashboard'),
    path('case_history_register_dashboard/', views.case_history_record_dashboard, name='case_history_register_dashboard'),
    path('counselling_register_dashboard/',views.counselling_register_dashboard,name='counselling_register_dashboard'),
    path('death_register_dashboard/',views.death_register_dashboard,name='death_register_dashboard'),
    path('employment_link_register_dashboard/', views.employment_linkage_form_dashboard, name='employment_link_register_dashboard'),
    path('food_menu_register_dashboard/', views.food_menu_dashboard, name='food_menu_register_dashboard'),
    path('inspection_register_dashboard/', views.inspection_records_dashboard, name='inspection_register_dashboard'),
    path('master_record_dashboard/', views.master_records_dashboard, name='master_record_dashboard'),# no change
    path('medical_camp_register_dashboard/', views.medical_record_form_dashboard, name='medical_camp_register_dashboard'),
    path('medicine_register_dashboard/', views.medicine_register_dashboard, name='medicine_register_dashboard'),
    path('night_survey_register_dashboard/', views.night_survey_dashboard, name='night_survey_register_dashboard'),
    path('performance_appraisal_register_dashboard/', views.performance_appraisal_dashboard, name='performance_appraisal_register_dashboard'),
    path('provision_dashboard', views.provision_dashboard, name='provision_dashboard'),
    path('rehabilitation_register_dashboard/', views.rehabilitation_note_dashboard, name='rehabilitation_register_dashboard'),
    path('reintegration_register_dashboard/', views.reintegration_register_dashboard, name='reintegration_register_dashboard'),
    path('resident_attendance_register_dashboard/', views.resident_attendance_form_dashboard, name='resident_attendance_register_dashboard'),
    path('Salary_register_dashboard/', views.salary_register_dashboard, name='Salary_register_dashboard'),
    path('skill_training_register_dashboard/', views.skill_training_register_dashboard, name='skill_training_register_dashboard'),
    path('smc_register_dashboard/', views.smc_register_dashboard, name='smc_register_dashboard'),
    path('social_entertainment_register_dashboard/', views.social_entertainment_record_dashboard, name='social_entertainment_register_dashboard'),
    path('staff_attendence_register_dashboard/', views.staff_attendance_register_dashboard, name='staff_attendence_register_dashboard'),
    path('staff_movement_register_dashboard/', views.staff_movement_note_dashboard, name='staff_movement_register_dashboard'),
    path('stock_register_dashboard/', views.stock_register_dashboard, name='stock_register_dashboard'),
    path('visitor_register_dashboard/', views.visitor_registration_dashboard, name='visitor_register_dashboard'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)















