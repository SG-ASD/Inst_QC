from django.conf import Settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView


# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# class HardwareUpdateView_second(UpdateView):
#     model = Settings
#     form_class = HardwareUpdateForm_second
#     template_name = 'Hardwareapp/hardware_second.html'
#     context_object_name = 'target_Hardware'
#
#     def get_object(self):
#         object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
#         return object
#
#     @transaction.atomic
#     def get_context_data(self, **kwargs):
#         context = super(HardwareUpdateView_second, self).get_context_data(**kwargs)
#         context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
#         return context
#
#     def get_success_url(self):
#         return reverse("Performanceapp:update_Performance1", kwargs={"Instrument_SN": self.object})