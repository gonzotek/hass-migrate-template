"""Config flow for template migration component."""

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import DOMAIN


class TemplateMigrationConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for template migration."""

    async def async_step_user(
        self, user_input: dict[str, str] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        return self.async_create_entry(
            title="Legacy Template Migration Helper", data={}
        )
