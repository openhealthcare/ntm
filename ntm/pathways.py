from pathway import pathways
from ntm import models as ntm_models
from obs import models as obs_models


class AddNTMPatient(pathways.RedirectsToPatientMixin, pathways.PagePathway):
    display_name = "Add Patient"
    slug = "add_ntm_patient"
    steps = (
        pathways.Step(
            title="Add Patient",
            icon="fa fa-user",
            template_url="/templates/pathways/add_ntm_patient.html",
            controller_class="AddNtmPatientCtrl"
        ),
    )
