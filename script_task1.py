from dcim.models import Site
from extras.scripts import Script, ChoiceVar
import yaml

class FilterSitesScript(Script):
    class Meta:
        name = "Filter Sites by Status"
        description = "Filters sites by their status and outputs info in YAML."

    status = ChoiceVar(
        choices=[
            ('active', 'Active'),
            ('planned', 'Planned'),
        ],
        label="Site Status",
        required=True
    )

    def run(self, data, commit):
        selected_status = data['status']
        results = []

        for site in Site.objects.filter(status=selected_status):
            self.log_info(f"#{site.id}: {site.name} - {site.status}")
            results.append({
                "id": site.id,
                "name": site.name,
                "status": site.status
            })

        return yaml.dump(results, sort_keys=False)
