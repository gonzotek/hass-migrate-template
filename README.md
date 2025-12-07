# Legacy Template Migration Helper

[![hacs_badge](https://img.shields.io/badge/HACS-Ready-blue.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
<br><a href="https://www.buymeacoffee.com/Petro31" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-black.png" width="150px" height="35px" alt="Buy Me A Coffee" style="height: 35px !important;width: 150px !important;" ></a>

This integration helps automatically migrate legacy template sensor issues into modern template entities.

<h1><a class="title-link" name="installation" href="#installation"></a>Installation</h1>

## With HACS

1.  Install the integration through HACS using the mylink button or by adding `https://github.com/Petro31/hass-migrate-template` to HACS.

    [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Petro31&repository=hass-migrate-template&category=integration)
2. Restart Home Assistant
3. Add Legacy Template Migration Helper in integrations

## without HACS
1. Copy the contents of `custom_components/template_migration/` to `<config>/custom_components/template_migration/`
2. Restart Home Assistant
3. Add Legacy Template Migration Helper in integrations

<h1><a class="title-link" name="use" href="#Using the service"></a>Installation</h1>

1.  In **Develper Tools** -> **Actions** tab, select the `template_migration.generate_yaml` action.
2.  Click **Perform action**
3.  A folder will be generated inside your configuration.  This folder will be named `migrated_templates` and it will contain mutliple files.  Each file will be a `domain` and it will contain all templates in that domain.
4.  Add `template migrated: !include_dir_merge_list migrated_templates` inside `configuration.yaml`.
5.  Verify the yaml loads properly by checking the configuration in **Developer Tools** -> **YAML** tab, **Check Configuration** button.
6.  Remove all references to the legacy templates provided by each repair.
7.  Restart home assistant.  Be careful, make sure **Check Configuration** passes before restarting home assistant.